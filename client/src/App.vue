<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Login from './components/Login.vue'
</script>

<template>
  <div >
    <header >
      <div class="header-content">
        <!-- <img class = "logo" src="../header.png" alt="Lontra"/>  -->
        <p class="nomePagina">Wydra</p>
      </div>
    </header>
      <body > 
        <!-- COMPONENTE -->
          <Login/>
          <!-- <RouterLink to="/login">Login</RouterLink> -->
          <RouterView />
      </body>
    <footer >
      <p style=" text-align: center;"> Sua Ágora digital.</p>
      <p style="margin-top: -15px ;text-align: end;margin-right: 10px; font-size: 20px;"> Developed at @UEM </p>
    </footer>
  </div>

</template> 

<style scoped>
  /* #header {
    background-color: rgba(0, 0, 0, 0.834); 
    height: 80px; 
    align-items: center; 
    display: flex;
  } */
  .header-content {
    background-color: rgba(0,0,0,0.834);
}


.header-content img {
  display: block; /* Ensures that the image is centered on its own line */
  margin: 0 auto; /* Centers the image horizontally within its container */
}

/* .header-content p {
  margin-top: 20px; 
  display: flex;
  justify-content: center;
} */


</style>
