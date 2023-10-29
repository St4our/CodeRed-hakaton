import { createRouter, createWebHistory } from 'vue-router';
import AppRegister from '../components/AppRegister.vue';
import AppLogin from '../components/AppLogin.vue';
import ListOrganization from '../components/ListOrganization.vue';
import ListAdmin from '../components/ListAdmin.vue';
import ListUsers from '../components/ListUsers.vue';
import CategoryUser from '../components/CategoryUser.vue';
import AppTest from '../components/AppTest.vue';
import TestCreate from '../create/TestCreate.vue';
import AppMenu from '../menu/AppMenu.vue';
import AdminMenu from '../menu/AdminMenu.vue';
import SuperMenu from '../menu/SuperMenu.vue';
import AppMain from '../components/AppMain.vue';
import AppChat from '../components/AppChat.vue';
import AppForm from '../components/AppForm.vue';
import AppPolicy from '../policy/AppPolicy.vue';
import CreateOrganization from '../create/CreateOrganization.vue';
import CreateCategory from '../create/CreateCategory.vue';
import AppTests from '../components/AppTests.vue';
import AppProfile from '../components/AppProfile.vue';
import AppLesson from '../components/AppLesson.vue';
import AppLessons from '../components/AppLessons.vue';
import LessonCreate from '../create/LessonCreate.vue';

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
      path: '/supermenu/list/organization',
      name: 'listorganization',
      component: ListOrganization,
    },
    {
      path: '/menu/list/admin',
      name: 'listadmin',
      component: ListAdmin,
    },
    {
      path: '/adminmenu/list/users/category/users',
      name: 'listusers',
      component: ListUsers,
    },
    {
      path: '/adminmenu/list/users/category',
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
      path: '/supermenu',
      name: 'supermenu',
      component: SuperMenu,
    },
    {
      path: '/adminmenu',
      name: 'adminmenu',
      component: AdminMenu,
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
      path: '/menu/lessons/lesson',
      name: 'lesson',
      component: AppLesson,
    },
    {
      path: '/policy',
      name: 'policy',
      component: AppPolicy,
    },
    {
      path: '/menu/lessons',
      name: 'lessons',
      component: AppLessons,
    },
    {
      path: '/menu/lesson/create',
      name: 'lesson-create',
      component: LessonCreate,
    },
    {
      path: '/form',
      name: 'form',
      component: AppForm,
    },
    {
      path: '/supermenu/list/organization/create',
      name: 'createorganization',
      component: CreateOrganization,
    },
    {
      path: '/adminmenu/list/users/category/create',
      name: 'createcategory',
      component: CreateCategory,
    },
  ],
});

export default router;
