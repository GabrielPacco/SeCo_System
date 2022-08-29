<template>
  <v-app>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>
<div id="building">
</div>

<script>
import Home from './components/Home';
  //import Admin from './components/Admin';
  //import User from './components/User';
  import AboutUs from './components/AboutUs';
  
  export default {
    name: 'App',
  
    components: {
      Home,
      //Admin,
      //User,
      AboutUs
    },
  };
  </script>
