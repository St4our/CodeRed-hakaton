import { createRouter, createWebHistory } from 'vue-router';
import AppRegister from '../components/AppRegister.vue';
import AppLogin from '../components/AppLogin.vue';
import ListOrganization from '../components/ListOrganization.vue';
import ListAdmin from '../components/ListAdmin.vue';
import ListUsers from '../components/ListUsers.vue';
import CategoryUser from '../components/CategoryUser.vue';
import AppTests from '../components/AppTests.vue';
import TestCreate from '../create/TestCreate.vue';
import AppMenu from '../components/AppMenu.vue';
import AppProfile from '../components/AppProfile.vue';
import AppMain from '../components/AppMain.vue';
import AppChat from '../components/AppChat.vue';
import AppTest from '../components/AppTest.vue';
import AppLesson from '../components/AppLesson.vue';
import AppPolicy from '../policy/AppPolicy.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: AppMain,
      alias: '/',
    },
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
      path: '/menu/list/organization',
      name: 'listorganization',
      component: ListOrganization,
    },
    {
      path: '/menu/list/admin',
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
    },
    {
      path: '/menu/tests',
      name: 'tests',
      component: AppTests,
    },
    {
      path: '/menu/test/create',
      name: 'testcreate',
      component: TestCreate,
    },
    {
      path: '/menu/chat',
      name: 'chat',
      component: AppChat,
    },
    {
      path: '/menu/tests/test',
      name: 'test',
      component: AppTest,
    },
    {
      path: '/menu/profile',
      name: 'profile',
      component: AppProfile,
    },
    {
      path: '/menu/lesson',
      name: 'lesson',
      component: AppLesson,
    },
    {
      path: '/policy',
      name: 'policy',
      component: AppPolicy,
    },
  ],
});

export default router;
