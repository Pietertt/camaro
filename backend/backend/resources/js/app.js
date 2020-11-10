import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

import DashboardComponent from './components/dashboard/DashboardComponent'
import ActivitiesOverviewComponent from './components/activities/ActivitiesOverviewComponent'
import LoginComponent from './components/login/LoginComponent'

Vue.component('menu-component', require('./components/dashboard/MenuComponent.vue').default)
Vue.component('monthly-component', require('./components/dashboard/MonthlyComponent.vue').default)
Vue.component('actions-component', require('./components/dashboard/ActionsComponent.vue').default)
Vue.component('activities-component', require('./components/dashboard/ActivitiesComponent.vue').default)
Vue.component('statistics-component', require('./components/dashboard/StatisticsComponent.vue').default)
Vue.component('dashboard-component', require('./components/dashboard/DashboardComponent.vue').default)

Vue.component('login-component', require('./components/login/LoginComponent.vue').default)

Vue.component('activities-overview-component', require('./components/activities/ActivitiesOverviewComponent.vue').default)

Vue.component('line-component', require('./components/charts/LineComponent.vue').default)
Vue.component('pie-component', require('./components/charts/PieComponent.vue').default)

const router = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/dashboard',
            component: DashboardComponent
        },
        {
            path: '/dashboard/activiteiten',
            component: ActivitiesOverviewComponent
        },
        {
            path: '/',
            component: LoginComponent
        }
    ],
});

const app = new Vue({
    el: '#app',
    router,
});