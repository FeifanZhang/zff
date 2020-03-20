import Vue from 'vue'
import App from './App.vue'
import Vuex from 'vuex'

Vue.config.productionTip = false;
Vue.use(Vuex);

const store = new Vuex.Store({
	//global var
	state:{
		pageStatus: 0,
		ip: "localhost",
		front_end_port: "8080",
		back_end_port: "8000",
		token: ""
	},
	//modify attr in state
	mutations:{
		increase(state){
			state.pageStatus += 1;
		},
		decrease(state){
			state.pageStatus -= 1;
		},
		set_token(state, str){
			state.token = str
		}
	},
	getters:{
		get_token(state){
			return state.token
		}
	},
	actions:{
		
	}
});

new Vue({
  render: h => h(App),
  store
}).$mount('#app');
