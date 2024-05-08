import {createRouter, createWebHistory} from "vue-router";

import Test from "@/pages/Test.vue";
import Index from '@/pages/Index.vue';
import Login from "@/pages/Login.vue";
import Register from "@/pages/Register.vue";
import UserList from "@/components/UserList.vue";
import Plaza from "@/components/Plaza.vue";
import Profile from "@/components/Profile.vue";

const routes =
    [
        {
            path: '/test', name: 'Test',
            component: Test
        },
        {
            path: '/', name: 'Login',
            component: Login
        },
        {
            path: '/index', name: 'Index',
            component: Index,
            children: [
                {
                    path: 'userList', name: 'UserList',
                    component: UserList
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
                }
            ]
        },
        {
            path: '/register', name: 'Register',
            component: Register
        }
    ];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;
