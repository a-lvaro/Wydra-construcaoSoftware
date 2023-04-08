import { createRouter, createWebHistory } from 'vue-router'
import Login from '../components/Login.vue'
import Cadastro from '../components/Cadastro.vue'
import Busca from '../components/Busca.vue'
import Perfil from '../components/Perfil.vue'
import Obra from '../components/Obra.vue'
import Estante from '../components/Estante.vue'
import EstanteConfig from '../components/EstanteConfig.vue'
import Resenha from '../components/Resenha.vue'

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
      path: '/resenha',
      name: 'resenha',
      component: Resenha
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
    {
      path: '/obra',
      name: 'obra',
      component: Obra
    },
    {
      path: '/estante',
      name: 'estante',
      component: Estante
    },
    {
      path: '/estanteConfig',
      name: 'estanteConfig',
      component: EstanteConfig
    },
  ]
})

export default router
