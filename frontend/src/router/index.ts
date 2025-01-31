import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'

import Login from '../views/Login.vue'
import Dashboard from '../views/Dashboard.vue'
import Activities from '../views/Activities.vue'
import Activity from '../views/Activity.vue'

import {User} from '../models/User';

import LoginService from '../services/LoginService';
import DataService from '../services/DataService';

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
    {
        path: '/',
        name: 'Login',
        component: Login
    },
    {
        path: '/logout',
        name: 'Logout',
        component: Login,
        beforeEnter (to, from, next) {
            LoginService.logoutUser();
            next({name: 'Login'});
        }
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: Dashboard,
        beforeEnter: (to, from, next) => {
            if(DataService.getUserData() !== ''){
                const user: User = LoginService.getUserData();

                LoginService.getUserToken(user.id).then(response => {
                    if(response.data === LoginService.getUserData().token){
                        next();
                    } else {
                        next({name: 'Login'});
                    }
                });
            } else {
                next({name: 'Login'});
            }
        }
    },
    {
        path: '/activities',
        name: 'Activities',
        component: Activities,
        beforeEnter: (to, from, next) => {
            if(DataService.getUserData() !== ''){
                const user: User = LoginService.getUserData();

                LoginService.getUserToken(user.id).then(response => {
                    if(response.data === LoginService.getUserData().token){
                        next();
                    } else {
                        next({name: 'Login'});
                    }
                });
            } else {
                next({name: 'Login'});
            }
        }
    },
    {
        path: '/activity/:id',
        name: 'Activity',
        component: Activity,
        beforeEnter: (to, from, next) => {
            if(DataService.getUserData() !== ''){
                const user: User = LoginService.getUserData();

                LoginService.getUserToken(user.id).then(response => {
                    if(response.data === LoginService.getUserData().token){
                        next();
                    } else {
                        next({name: 'Login'});
                    }
                });
            } else {
                next({name: 'Login'});
            }
        }
    }
]

const router = new VueRouter({
  routes
})

export default router
