import vue from 'vue'
import VueRouter from 'vue-router'
import List from '@/components/List'

const router = new VueRouter({
    routes: [{
        path: '/list',
        component: List,
        name: 'List'
    }]
})