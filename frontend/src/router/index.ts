import {createRouter, createWebHistory} from "vue-router";

import Test from "@/pages/Test.vue";
import Index from '@/pages/Index.vue';
import Login from "@/pages/Login.vue";
import Register from "@/pages/Register.vue";

const routes =
    [
        {
            path: '/test',
            name: 'Test',
            component: Test
        },
        {
            path: '/',
            name: 'Login',
            component: Login
        },
        {
            path: '/index',
            name: 'Index',
            component: Index
        },
        {
            path: '/register',
            name: 'Register',
            component: Register
        }
    ];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;
