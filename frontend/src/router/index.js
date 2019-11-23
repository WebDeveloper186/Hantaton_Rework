import Vue from 'vue'
import VueRouter from 'vue-router'
import Payment from '@/components/Payment'
import Index from '@/components/Index'

Vue.use(VueRouter)

export default new VueRouter({
    mode: "history",
    routes: [{
        path: "/",
        name: "Index",
        component: Index
    }, {
        path: '/payment',
        component: Payment,
        name: 'Payment'
    }]
})