<template>
  <v-app>
    
    <v-app-bar app>
      <v-row
        align="center"
        justify="space-around"
        class="text-h4 font-weight-bold"
      >
      <img
        class="my-1"
        height = "50"
        width = "230"
        src="@/img/logobarra.png"
        alt="secosystem"
        link @click="$router.push({ path: '/' })"
      >
      &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj;
        <v-btn
          elevation="2"
          link @click="$router.push({ path: '/login' })"
        >
        Ingresa aquí
        </v-btn>

        <v-btn
          right
          x-small
          height=28
          link @click="$router.push({ path: '/aboutus' })"
          >
            Sobre nosotros
        </v-btn>

      </v-row>
      
    </v-app-bar>
    <v-main>
      <router-view></router-view>
    </v-main>

  </v-app>
</template>

<script>
import Home from './components/Home';
import Admin from './components/Admin';
import User from './components/User';
import AboutUs from './components/AboutUs';
import Concurso from './components/Concurso';
import Edicion from './components/Edicion';
import Panel from './components/Panel';
import Ponencia from './components/Ponencia';

export default {
  name: 'App',
  
  Components: {
    Home,
    Admin,
    User,
    Concurso,
    Edicion,
    Panel,
    AboutUs,
    Ponencia
  },
};
</script>
