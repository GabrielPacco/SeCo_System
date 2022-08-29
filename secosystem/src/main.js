import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

import VueRouter from 'vue-router'
Vue.use(VueRouter);


import Home from './components/Home'
import Admin from './components/Admin'
import User from './components/User'
import AboutUs from './components/AboutUs'

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { // primero muestra el componente Inicio
      path: '/',
      component: Home
    },
    {
      path: '/admin',
      component: Admin
    },
    {
      path: '/user',
      component: User
    },
    { // About Us
      path: '/aboutus',
      component: AboutUs
    }
  ]
});

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
