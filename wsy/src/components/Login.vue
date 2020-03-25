<template>
	<div>
		<keep-alive>
			<form class="Login" v-show="!showPop" @submit.prevent="login">
				<h1>没奖竞猜</h1>
				<input type="yourbirth" v-model="yourbirth" name="" placeholder="你的生日是什么时候?">
				<input type="mybirth" v-model="mybirth" name="" placeholder="我的生日是什么时候?">
				<input type="submit" name="" value="Login">
			</form>
		</keep-alive> 
		<div class = "pop" v-show="showPop" @click="showPop = !showPop">{{this.popMsg}}</div>
	</div>
</template>

<script>
//import {mapState} from "vuex";
import axios from "axios"
	export default {
		name: 'Login',
		data: function() {
			return {
				yourbirth: "",
				birthy: "19960115",
				mybirth: "",
				showPop: false,
				popMsg: "",
			}
		},
		computed:{
		},
		onLoad() {
	
		},
		methods: {
			login:function(){
				if (this.yourbirth != this.birthy){
					this.popMsg = "啥？咋连自己的生日也忘啦？";
					this.showPop = true;
				}else{
					axios({
						url: 'http://127.0.0.1:8000/api/login/confirmAuth/',
						method:'post',
						header:{
							"Content-Type": "application/json"
						},
						data: {
							"username": this.yourbirth,
							"password": this.mybirth,
						}
					}).then(res =>{
						console.log(res.status);
						if (res.status == 200){
							this.$router.replace({path: '/homepage', query: {token: res.data.token}})
							//this.$router.replace("/homepage/"+res.data.token);
						}
					}).catch(res => {
						console.log(res);
						this.popMsg = "哈？竟然连我的生日也弄错了？";
						this.showPop = true;
					})
				}
			},
		},
	}
</script>

<style>
	/* pop style */
	.pop{
		color: white;
		font-family: sans-serif;
		width: 150px;
		padding: 150px;
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		background: rgba(0,0,0, .8);
		opacity: 50;
		text-align: center;
		border-radius: 24px;
	}
	/*login form*/
	.Login{
		font-family: sans-serif;
		width: 300px;
		padding: 40px;
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		background: rgba(0,0,0, .8);
		opacity: 50;
		text-align: center;
		border-radius: 24px;
		transition: 0.5s;
	}
	/*login form h1*/
	.Login h1{
		color: white;
		text-transform: uppercase;
		font-weight: 500;
		background: rgba(0,0,0,0);
	}
	/*inputs*/
	.Login input[type = "mybirth"], .Login input[type = "yourbirth"]{
		background: rgba(0,0,0, .4);
		display: block;
		margin: 20px auto;
		text-align: center;
		border: 2px solid #3498db;
		padding: 14px 10px;
		width: 200px;
		outline: none;
		color: white;
		border-radius: 24px;
		transition: 0.25s;
	}
	/*submit*/
	.Login input[type = "submit"]{
		background: rgba(0,0,0, .4);
		display: block;
		margin: 20px auto;
		text-align: center;
		border: 2px solid #2ecc71;
		padding: 14px 40px;
		outline: none;
		color: white;
		border-radius: 24px;
		transition: 0.25s;
	}
	/*input focus*/
	.Login input[type = "mybirth"]:focus, .Login input[type = "yourbirth"]:focus{
		width: 280px;
		border-color: #2ecc71;
	}
	/*input hover*/
	.Login input[type = "mybirth"]:hover, .Login input[type = "yourbirth"]:hover{
		border-color: #2ecc71;
	}
	/*submit*/
	.Login input[type = "submit"]:hover{
		background: #2ecc71;
	}
</style>
