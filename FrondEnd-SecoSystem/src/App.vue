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
<<<<<<< HEAD:FrondEnd-SecoSystem/src/App.vue
<div id="building">
</div>
  
<!-- <style>
#building{
background:url("../assets/image/BJ1.jpg");
width:100%;			// El tamaño se establece en 100%
height:100%;			// El tamaño se establece en 100%
position:fixed;
background-size:100% 100%;}
</style> -->
<script>
=======

<script>
import Home from './components/Home';
import Admin from './components/Admin';
import User from './components/User';
import AboutUs from './components/AboutUs';
import Concurso from './components/Concurso';
import Edicion from './components/Edicion';
import Panel from './components/Panel';
import Ponencia from './components/Ponencia';

>>>>>>> 803294bcf01e7cdca3990a93120cc345c1241145:secosystem/src/App.vue
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
