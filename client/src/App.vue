<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Login from './components/Login.vue'
</script>


<template>
  <div>
    <header class="topo">
      <img class = "lontra" src="../wydra.png" alt="Lontra">
    </header>
      <body > 
          <Login/>
          <!-- <RouterLink to="/login">Login</RouterLink> -->
          <RouterView />
      </body>

  </div>


</template> 

<style scoped>
  

</style>
