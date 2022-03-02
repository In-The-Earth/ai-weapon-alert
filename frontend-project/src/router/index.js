
import Home from '@/components/HelloWorld.vue'
import About from '@/components/page2.vue'
import Alert from '@/components/alert.vue'


import { createWebHistory, createRouter } from "vue-router";


const routes = [
  {
    path: "/HelloWorld",
    name: "home",
    component: Home,
  },
  {
    path: "/page2",
    name: "lab1",
    component: About,
  },
  {
    path: "/alert",
    name: "alert",
    component: Alert,
  },
  
];

const router = createRouter({
  history: createWebHistory(),routes
});

export default router;

  
