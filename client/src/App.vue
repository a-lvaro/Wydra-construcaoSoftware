<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Login from './components/Login.vue'
import Cadastro from './components/Cadastro.vue'
</script>

<template>
  <div>
    <header style="margin-bottom: 30px;">
      <div class="header-content">
        <!-- <img class = "logo" src="../header.png" alt="Lontra"/>  -->
        <p class="nomePagina">Wydra</p>
        <nav>
          <ul class="menu">
            <!-- <RouterLink to="/login">Login</RouterLink> -->
            <li><a href="#">Registrar</a></li>
            <li><a href="#">Login</a></li>
            <li><a href="#">Estante</a></li>
            <li><a href="#">Perfil</a></li>
            <li><a href="#">Busca</a></li>
            <li><a href="#">Logout</a></li>
          </ul>
        </nav>
      </div>
    </header>
    <body > 
      <!-- COMPONENTE -->
        <!-- <Login/> -->
        <!-- <Cadastro/> -->
        <!-- <RouterLink to="/login">Login</RouterLink> -->
        <RouterView />
    </body>
    <footer >
      <p style="text-align: center; font-size: 30px;"> Sua Ágora digital.</p>
      <p style="margin-top: -15px ;text-align: end;margin-right: 20px; font-size: 20px; font-family: 'Segoe UI';"> Developed at @UEM </p>
    </footer>
  </div>

</template> 

<style scoped>

</style>
