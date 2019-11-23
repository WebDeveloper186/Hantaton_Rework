import requests
import json
import bs4


def _float(value):
    if value:
        return float(value['value'].replace('\xa0', '').replace(',', '.'))
    return 0


def parse(street, house, flat):
    address = {'street': street, 'house': house, 'flat': flat}
    session = requests.Session()

    first_page = session.get(
        'https://pay.rkc-gku.ru/app_main_pay/Account.aspx/AddComm')
    first_page_parse = bs4.BeautifulSoup(first_page.content, "lxml")
    cities = first_page_parse.find(id='cityId')
    city_list = cities.find_all('option')
    for city in city_list:
        print(city['value'], city.text)

    services_by_city = session.post(
        'https://pay.rkc-gku.ru/app_main_pay/Address.aspx/ServicesByCity',
        data={'cityId': 236}
    )
    services = json.loads(services_by_city.content)
    for service in services:
        organization_data = session.post(
            'https://pay.rkc-gku.ru/app_main_pay/Address.aspx/UkByService',
            data={'serviceId': service['Value']})
        organizations = json.loads(organization_data.content)
        for organization in organizations:
            streets_data = session.post(
                'https://pay.rkc-gku.ru/app_main_pay/Address.aspx/'
                'StreetsByCompany',
                data={'companyId': organization['Value']}
            )
            streets = json.loads(streets_data.content)
            for street in streets:
                if street['Text'] == address['street']:
                    houses_data = session.post(
                        'https://pay.rkc-gku.ru/app_main_pay/Address.aspx/'
                        'HousesByCompanyStreet',
                        data={'streetId': street['Value']}
                    )
                    houses = json.loads(houses_data.content)
                    for house in houses:
                        if house['Text'] == address['house']:
                            flats_data = session.post(
                                'https://pay.rkc-gku.ru/app_main_pay/Address.aspx/'
                                'FlatsByHouse',
                                data={'houseId': house['Value']}
                            )
                            flats = json.loads(flats_data.content)
                            for flat in flats:
                                if flat['Text'].strip() == address['flat']:
                                    data = session.post(
                                        'https://pay.rkc-gku.ru/app_main_pay/'
                                        'Account.aspx/AddComm',
                                        data={
                                            'cityId': 236,
                                            'serviceId': service['Value'],
                                            'companyId': organization['Value'],
                                            'LC': '',
                                            'streetId': street['Value'],
                                            'houseId': house['Value'],
                                            'flatId': flat['Value'],
                                            'WebSite': '/app_main_pay/'
                                        },
                                    )
                                    data_parse = bs4.BeautifulSoup(data.content,
                                                                   'lxml')
                                    account_balance = _float(data_parse.find(
                                        id='AccountBalanceInfo'))
                                    account_peni = _float(data_parse.find(
                                        id='AccountPeniInfo'))
                                    account_payed = _float(data_parse.find(
                                        id='AccountCurrMonthPaySumInfo'))
                                    account_payed_peni = _float(data_parse.find(
                                        id='AccountCurrMonthPeniSumInfo'))
                                    response = json.dumps({"service":service['Text'],
                                                           "organization": organization['Text'],
                                                           "balance": account_balance,
                                                           "peni": account_peni,
                                                           "payed": account_payed,
                                                           "payed_peni":account_payed_peni})
                                    return response
