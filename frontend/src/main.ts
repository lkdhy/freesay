import {createApp} from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import router from './router';
import {createPinia} from "pinia";
import Particles from "@tsparticles/vue3";
import { loadFull } from "tsparticles";
import { loadSlim } from "@tsparticles/slim";

const app = createApp(App)
const pinia = createPinia()

app.use(ElementPlus)
app.use(router)
app.use(pinia)
app.use(Particles, {
    init: async engine => {
        await loadFull(engine);
        // you can load the full tsParticles library from "tsparticles" if you need it
        // await loadSlim(engine)
        // or you can load the slim version from "@tsparticles/slim" if don't need Shapes or Animations
        // await loadBubblePreset(engine)
    }
})

app.mount('#app')