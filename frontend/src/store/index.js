import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        icons: [{
                id: "snow",
                name: "Уборка снега",
                icon: "https://psv4.userapi.com/c856528/u171284348/docs/d4/a5e8a4c3308c/snow-flake.png?extra=OkfHvizxA37hCmFHxncNXLEZmgCPiBaBvEKpFR29SVpNZCbNDcFhnSBx5gQ7fJFJ2rAoYl5FgzMBvbjnss7cANO5_tHDf6AXs0bDYMwgkbPYbhRw-R6Xbkgl7G38m6jXOxfgsR8BQ8_3JzEAZSP7xMk67w&dl=1"
            },
            {
                id: "bench",
                name: "Проблемы с лавочками",
                icon: "https://psv4.userapi.com/c856528/u171284348/docs/d10/629b602e7dc4/1649.png?extra=2gwkHup1Zc_3j4cz-mNUkitVMlCxxrWGqa_tgg0o6apFotEUrQ1f5SjQsl1hNHvyAe2SzHWSR3CAdCoeOkX4Rpq4rmIsEq_1JpfJ0Xx7x2VdCk_ONJnAXmot1WPNQTWqzn5ky4c0JDo03PyuylkmJC5GQQ&dl=1"
            },
            {
                id: "ligt",
                name: "Проблемы с освещением",
                icon: "https://psv4.userapi.com/c856528/u171284348/docs/d2/0e98720c383c/160px-Crystal_Clear_app_ktip_svg.png?extra=vt12BaEDRD27-rPKm1LZxGVuE2BWakWTcukHT2asVUsjf0v3WuqBNaK39nhN6k6SBJhG6rGmxlkQMVURsGRch66S0yN2TV_-otaWcD_3gdmZZ_0qr-9xogna4aMSKY2_ZStFKGCYaegmQqpiCZeyS6l8vA&dl=1"
            }
        ]
    },
    getters: {},
    mutations: {},
    actions: {}
})