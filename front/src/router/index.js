import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/verGraficas',
    name: 'VerGraficas',
    component: () => import('../views/verGraficas.vue')
  },
  {
    path: '/nueva',
    name: 'Nueva',
    component: () => import('../views/Nueva.vue')
  },
  {
    path: '/grafica/:id',
    name: 'Grafica',
    component: () => import('../views/Grafica.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
