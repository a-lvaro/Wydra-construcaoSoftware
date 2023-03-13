<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Login from './components/Login.vue'
import Cadastro from './components/Cadastro.vue'
import Busca from './components/Busca.vue'
</script>

<template>
  <div>
    <header>
      <div class="header-content">
        <!-- <img class = "logo" src="../header.png" alt="Lontra"/>  -->
        <p class="nomePagina">Wydra</p>
        <nav>
          <ul class="menu">
            <li>
              <RouterLink to="/cadastro">Cadastro</RouterLink>
            </li>
            <li>
              <RouterLink to="/login">Login</RouterLink>
            </li>
            <li>
              <RouterLink to="/estante">Estante</RouterLink>
            </li>
            <li>
              <RouterLink to="/perfil">Perfil</RouterLink>
            </li>
            <li>
              <RouterLink to="/busca">Busca</RouterLink>
            </li>
            <li>
              <RouterLink to="/Logout">Logout</RouterLink>
            </li>
          </ul>
        </nav>
      </div>
    </header>
    <body>
      <RouterView />
    </body>
    <footer>
      <p style="text-align: center; font-size: 30px;"> Sua Ágora digital.</p>
      <p style="margin-top: -15px ;text-align: end;margin-right: 20px; font-size: 20px; font-family: 'Segoe UI';">
        Developed at @UEM </p>
    </footer>
  </div>
</template> 

<style scoped></style>
