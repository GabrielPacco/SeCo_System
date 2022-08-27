<template>
  <v-app>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>
<div id="building">
</div>
  
<style>
#building{
background:url("../assets/image/BJ1.jpg");
width:100%;			// El tamaño se establece en 100%
height:100%;			// El tamaño se establece en 100%
position:fixed;
background-size:100% 100%;}
</style>
<script>


export default {
  name: 'App',

  components: {
    
  },

  data: () => ({
    //
  }),
};
</script>
