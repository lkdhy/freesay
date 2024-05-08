import {createRouter, createWebHistory} from "vue-router";

import Test from "@/pages/Test.vue";
import Welcome from "@/pages/Welcome.vue";
import Index from '@/pages/Index.vue';
import Login from "@/pages/Login.vue";
import Register from "@/pages/Register.vue";
import UserList from "@/components/UserList.vue";
import Plaza from "@/components/Plaza.vue";
import Profile from "@/components/Profile.vue";
import UserListProfile from "@/components/UserListProfile.vue";
import Homepage from "@/components/Homepage.vue";

const routes =
    [
        {
            path: '/index', name: 'Welcome',
            component: Welcome
        },
        {
            path: '/test', name: 'Test',
            component: Test
        },
        {
            path: '/login', name: 'Login',
            component: Login
        },
        {
            path: '/', name: 'Index',
            component: Index,
            children: [
                {
                    path: 'userList', name: 'UserList',
                    component: UserList
                },
                {
                    path: 'user', name: 'UserListProfile',
                    component: UserListProfile
                },
                {
                    path: 'plaza', name: 'Plaza',
                    component: Plaza
                },
                {
                    path: 'test', name: 'Test',
                    component: Test
                },
                {
                    path: 'profile', name: 'Profile',
                    component: Profile
                },
                {
                    path: '/user/:id', name: 'User',
                    component: Homepage
                }
            ]
        },
        {
            path: '/register', name: 'Register',
            component: Register
        },
    ];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;
