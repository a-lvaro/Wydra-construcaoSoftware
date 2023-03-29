import { createRouter, createWebHistory } from 'vue-router'
import Login from '../components/Login.vue'
import Cadastro from '../components/Cadastro.vue'
import Busca from '../components/Busca.vue'
import Perfil from '../components/Perfil.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/cadastro',
      name: 'cadastro',
      component: Cadastro
    },
    {
      path: '/busca',
      name: 'busca',
      component: Busca
    },
    {
      path: '/perfil',
      name: 'perfil',
      component: Perfil
    },
  ]
})

export default router
