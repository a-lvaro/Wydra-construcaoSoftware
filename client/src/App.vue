<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <div class="App">
    <RouterView />
    <Footer />
  </div>
</template> 

<style scoped></style>

<script>
export default{
  mounted() {
    localStorage.setItem('mostrarItem', 'false');
    localStorage.setItem('token', null);
    localStorage.setItem('usuario', null);
  },
}
</script>
