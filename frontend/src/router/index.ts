import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'

import Login from '../views/Login.vue'
import Dashboard from '../views/Dashboard.vue'
import Activities from '../views/Activities.vue'
import Activity from '../views/Activity.vue'

import LoginService from '../services/LoginService';

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    beforeEnter: (to, from, next) => {
        if(LoginService.isUserLoggedIn()){
            next();
        } else {
            console.log();
            next({ name: 'Login' });
        }
    }
  },
  {
    path: '/activities',
    name: 'Activities',
    component: Activities
  },
  {
    path: '/activity/:id',
    name: 'Activity',
    component: Activity
  }
]

const router = new VueRouter({
  routes
})

export default router
