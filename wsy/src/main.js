import Vue from 'vue'
import App from './App.vue'
import Vuex from 'vuex'

// 将vuex注册进入vue内
Vue.use(Vuex);
import router from './router.js'
Vue.config.productionTip = false;
const store = new Vuex.Store({
	// state用来声明变量并初始化
	state:{
		ip: "localhost",
		front_end_port: "8080",
		back_end_port: "8000",
		token: ""
	},
	// state内的变量不能直接修改，通过调取mutations内的方法进行修改
	// mutation内实现了三个方法：pageStatus的加，减以及字符串token的赋值
	mutations:{
		// 将token赋值，注意要声明输入的参数str
		set_token(state, str){
			state.token = str
		}
	},
	// state内的变量不能直接获取，要通过getters方法声明
	getters:{
		// 获取 token
		get_token(state){
			return state.token
		}
	},
	actions:{
		
	}
});

new Vue({
	render: h => h(App),
	// 将router挂载进app.vue
	router,
	// 将store挂载进app.vue
	store
}).$mount('#app');
