import { createRouter, createWebHistory } from 'vue-router'
import Login from '../components/Login.vue'
import Cadastro from '../components/Cadastro.vue'
import Busca from '../components/Busca.vue'

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
  ]
})

export default router
