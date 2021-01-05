"use strict";
exports.__esModule = true;
var vue_1 = require("vue");
var App_vue_1 = require("./App.vue");
var router_1 = require("./router");
var vue_google_charts_1 = require("vue-google-charts");
vue_1["default"].config.productionTip = false;
vue_1["default"].use(vue_google_charts_1["default"]);
new vue_1["default"]({
    router: router_1["default"],
    render: function (h) { return h(App_vue_1["default"]); }
}).$mount('#app');
