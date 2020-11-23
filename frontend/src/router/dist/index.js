"use strict";
exports.__esModule = true;
var vue_1 = require("vue");
var vue_router_1 = require("vue-router");
var Login_vue_1 = require("../views/Login.vue");
var Dashboard_vue_1 = require("../views/Dashboard.vue");
var Activities_vue_1 = require("../views/Activities.vue");
vue_1["default"].use(vue_router_1["default"]);
var routes = [
    {
        path: '/',
        name: 'Login',
        component: Login_vue_1["default"]
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: Dashboard_vue_1["default"]
    },
    {
        path: '/activities',
        name: 'Activities',
        component: Activities_vue_1["default"]
    }
];
var router = new vue_router_1["default"]({
    routes: routes
});
exports["default"] = router;
