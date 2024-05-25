import {createRouter, createWebHistory} from "vue-router"
import Test from "@/pages/Test.vue"
import Welcome from "@/pages/Welcome.vue"
import Index from '@/pages/Index.vue'
import Login from "@/pages/Login.vue"
import Register from "@/pages/Register.vue"
import UserList from "@/components/UserList.vue"
import Plaza from "@/components/plaza/Plaza.vue"
import Profile from "@/components/Profile.vue"
import UserListProfile from "@/components/UserListProfile.vue"
import Homepage from "@/components/Homepage.vue"
import Empty from "@/components/Empty.vue"
import tmp2 from "@/pages/tmp2.vue"
import BackgroundSwiper from "@/components/BackgroundSwiper.vue"
import Partcs from "@/pages/Partcs.vue"
import Pacts2 from "@/pages/Pacts2.vue"
import ColorfulBubblesParticles from "@/components/Particles/ColorfulBubblesParticles.vue"
import SnowParticles from "@/components/Particles/SnowParticles.vue"
import userBox from "@/components/user_box/userBox.vue"

const routes =
    [
        {
            path: '/tmp3', name: 'background',
            component: ColorfulBubblesParticles
        },
        {
            path: '/snow', name: 'Snow',
            component: SnowParticles
        },
        {
            path: '/particles', name: 'particles',
            component: Partcs
        },
        {
            path: '/particles2', name: 'particles2',
            component: Pacts2
        },
        {
            path: '/empty', name: 'forRefresh',
            component: Empty
        },
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
                    path: 'userBox', name: 'UserBox',
                    component: userBox
                },
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
        {
            path: '/tmp', name: 'Swiper',
            component: tmp2
        }
    ];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;
