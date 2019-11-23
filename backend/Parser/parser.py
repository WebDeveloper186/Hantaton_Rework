from html.parser import HTMLParser
from urllib.request import urlopen


class MyHTMLParser(HTMLParser):
    def read_site_content(self):
        return str(urlopen(self.site_name).read())
    def __init__(self, site_name):
        # список ссылок
        self.links = []
        # имя сайта
        self.site_name = site_name
        # вызываем __init__ родителя
        super().__init__()
        # при инициализации "скармливаем" парсеру содержимое страницы
        
        self.feed(self.read_site_content())
        # записываем список ссылок в файл
        self.write_to_file()

    def handle_starttag(self, tag, attrs):
        # проверяем является ли тэг тэгом ссылки
        if tag == 'a':
            # находим аттрибут адреса ссылки
            for attr in attrs:
                if attr[0] == 'href':
                    # проверяем эту ссылку методом validate() (мы его еще напишем)
                    if not self.validate(attr[0]):
                        # вставляем адрес в список ссылок
                            self.links.append(attr[1])

    def validate(self, link):        
        return link in self.links or '#' in link or 'javascript:' in link


    

    def write_to_file(self):
        # открываем файл
        f = open('links.txt', 'w')
        # записываем отсортированный список ссылок, каждая с новой строки
        f.write('\n'.join(sorted(self.links)))
        # закрываем файл
        f.close()

parser = MyHTMLParser("https://yk-sistema.ru")