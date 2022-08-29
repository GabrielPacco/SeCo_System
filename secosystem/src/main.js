import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

import VueRouter from 'vue-router'
Vue.use(VueRouter);

import Home from './components/Home';
import Admin from './components/Admin';
import User from './components/User';
import AboutUs from './components/AboutUs';
import Concurso from './components/Concurso';
import Edicion from './components/Edicion';
import Panel from './components/Panel';
import Ponencia from './components/Ponencia';

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    {
      path: '/login',
      component: Home
    },
    {
      path: '/admin',
      component: Admin
    },
    {
      path: '/',
      component: User
    },

    { 
      path: '/aboutus',
      component: AboutUs
    },
    {
      path: '/concurso',
      component: Concurso
    },
    {
      path: '/edicion',
      component: Edicion
    },
    {
      path: '/panel',
      component: Panel
    },

    {
      path: '/ponencia',
      component: Ponencia
    }
  ]
});

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
