import { createRouter, createWebHistory } from 'vue-router'
import AppRegister from '../components/AppRegister.vue'
import AppLogin from '../components/AppLogin.vue'
import ListOrganization from '../components/ListOrganization.vue'
import ListAdmin from '../components/ListAdmin.vue'
import ListUsers from '../components/ListUsers.vue'
import CategoryUser from '../components/CategoryUser.vue'
import AppMenu from '../components/AppMenu.vue'
import AppPerson from '../components/AppPerson.vue'
import AppChat from '../components/AppChat.vue'

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
      path: '/list/organization',
      name: 'listorganization',
      component: ListOrganization,
    },
    {
      path: '/list/admin',
      name: 'listadmin',
      component: ListAdmin,
    },
    {
      path: '/list/users',
      name: 'listusers',
      component: ListUsers,
    },
    {
      path: '/menu/list/users/category',
      name: 'categoryusers',
      component: CategoryUser,
    },
    {
      path: '/menu',
      name: 'menu',
      component: AppMenu,
      alias: "/"
    },
    {
      path: '/chat',
      name: 'chat',
      component: AppChat,
    },
  ]
})

export default router
