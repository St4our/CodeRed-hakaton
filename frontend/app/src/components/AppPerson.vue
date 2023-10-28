import { createRouter, createWebHistory } from 'vue-router'
import AppRegister from '../components/AppRegister.vue'
import AppLogin from '../components/AppLogin.vue'
import ListOrganization from '../components/ListOrganization.vue'
import AppMenu from '../components/AppMenu.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/registration',
      name: 'register',
      component: AppRegister,
    },
    {
      path: '/login',
      name: 'login',
      component: AppLogin,
    },
    {
      path: '/list',
      name: 'listorganization',
      component: ListOrganization,
    },
    {
      path: '/menu',
      name: 'menu',
      component: AppMenu,
      alias: "/"
    },
  ]
})

export default router
