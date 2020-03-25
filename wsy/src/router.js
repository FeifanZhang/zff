import Vue from 'vue'
import VueRouter from 'vue-router'
import Anniversary from "./components/homeComponents/Anniversary";
import Clock from "./components/homeComponents/Clock";
import Photos from "./components/homeComponents/Photos";
import Words from "./components/homeComponents/Words";
Vue.use(VueRouter);
const routes=[
    //单个路由均为对象类型，path代表的是路径，component代表组件
    //特殊情况的代码写在最开始，如果写在最后，后期可能会在后面加代码，特殊情况的代码就难找到了
    {
        path:'',
        redirect:'login'
    },
    {
        path:'/homepage',
        component:() => import('./components/homeComponents/Nav.vue'),
        child:[
            {
                path: 'anniversary',
                component: Anniversary
            },
            {
                path: 'clock',
                component: Clock
            },
            {
                path: 'photos',
                component: Photos
            },
            {
                path: 'words',
                component: Words
            },
        ]
    },
    {
        path:'/login',
        component:() => import('./components/Login.vue')
    },

];

//实例化VueRouter并将routes添加进去
const router=new VueRouter({
//ES6简写，等于routes：routes
    routes,
    // 添加history模式，使得加载的url为html模式（刷新不会出现xxx/#/login的情况）
    mode: 'history'
});

//抛出这个这个实例对象方便外部读取以及访问
export default router