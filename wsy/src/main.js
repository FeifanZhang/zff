import Vue from 'vue'
import App from './App.vue'
import Vuex from 'vuex'
import axios from 'axios'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import router from './router.js'

// 将vuex注册进入vue内
Vue.use(Vuex);
Vue.use(ElementUI);
Vue.prototype.axios = axios;
Vue.config.productionTip = false;
// const store = new Vuex.Store({
// 	// state用来声明变量并初始化
// 	state:{
//
// 	},
// 	// state内的变量不能直接修改，通过调取mutations内的方法进行修改
// 	// mutation内实现了三个方法：pageStatus的加，减以及字符串token的赋值
// 	mutations:{
//
// 	},
// 	// state内的变量不能直接获取，要通过getters方法声明
// 	getters:{
//
// 	},
// 	actions:{
//
// 	}
// });

new Vue({
	render: h => h(App),
	// 将router挂载进app.vue
	router,
}).$mount('#app');
