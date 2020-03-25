<template>
	<keep-alive>
		<div class="Nav">
			<div class="NavButtons">
				<h1>HomePage</h1>
				<div><input type="submit" name="" value="照    片" @click="toPhoto"></div>
				<div><input type="submit" name="" value="纪念日" @click="toAnn"></div>
				<div><input type="submit" name="" value="计    时" @click="toClock"></div>
				<div><input type="submit" name="" value="想说的话" @click="toWords"></div>
				<div><input type="button" name="" value="返    回" @click="returnToLogin"/></div>	
			</div>
			<div class="ShowTimes">
				<div class="ShowTheTime">
					<h2>张张报时：</h2>
					<h6>{{this.myTime.format("YYYY-MM-DD")}} {{this.dayNameMapping[this.myTime.weekday()]}}</h6>
					<h1>{{this.myTime.format("HH:mm")}}</h1>
				</div>
				<div class="ShowTheTime">
					<h2>小猪报时:</h2>
					<h6>{{this.piggyTime.format("YYYY-MM-DD")}} {{this.dayNameMapping[this.piggyTime.weekday()]}}</h6>
					<h1>{{this.piggyTime.format("HH:mm")}}</h1>
				</div>
			</div>
			<keep-alive>
				<div class="ShowSubPage">
					<Photos v-show="this.subPageStatus==0"></Photos>
					<Anniversary v-show="this.subPageStatus==1"></Anniversary>
					<Clock v-show="this.subPageStatus==2"></Clock>
					<Words v-show="this.subPageStatus==3"></Words>
				</div>
			</keep-alive>
		</div>
	</keep-alive> 
</template>

<script>
import Photos from './Photos.vue';
import Anniversary from './Anniversary.vue';
import Clock from './Clock.vue'
import Words from './Words.vue'
let moment = require('moment-timezone');
moment.locale('zh-cn');
	export default {
		name: 'Heart',
		data() {
			return {
				showPop: false, 
				subPageStatus: 2,
				myTime:moment(),
				piggyTime:moment(),
				dayNameMapping:['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
			}
		},
		components: {
			Photos,
			Clock,
			Anniversary,
			Words,
		},
		created() {
			this.setClock();
			setInterval(()=>{this.setClock()}, 10000)
		},
		computed:{
			token(){
				// $route所拿到的路由是目前正活跃的路由
				// $router是获取路由列表内所有的路由
				// params.后面跟的参数要和router.js 设置的路由参数一样
				return this.$route.query.token
			}
		},
		methods:{
			setClock:function(){
				this.piggyTime = moment().tz("Asia/Shanghai");
				this.myTime = moment().tz("America/Chicago");
			},
			returnToLogin:function(){
				this.$router.replace('/login');
				this.toClock();
			},
			toPhoto:function(){
				this.subPageStatus = 0
			},
			toAnn:function(){
				this.subPageStatus = 1
			},
			toClock:function(){
				this.subPageStatus = 2
			},
			toWords:function(){
				this.subPageStatus = 3
			}
		}
	}
</script>

<style>
	.Nav{
		width: 100vw;
		height: 100vh;
	}
	.NavButtons{
		font-family: sans-serif;
		width: 35vw;
		height: 100vh;
		position: absolute;
		top: 50%;
		left: 5%;
		transform: translate(-50%, -50%);
		background: rgba(0,0,0, .5);
		opacity: 50;
		text-align: right;
		transition: 0.5s;
		float: right;
		font-size: 20px;
		padding-top: 10vh;
	}
	.NavButtons>h1{
		padding-right: 3vw;
		padding-bottom: 5vh;
		color: #FFF7F8;
	}
	.Nav input[type = "submit"]{
		margin-top: -2px;
		padding-top: 5vh;
		padding-bottom: 5vh;
		/*强制设定内容宽度使得button不会因为字符长短而改变宽度*/
		width: 15vw;
		color: #FFFFFF;
		background-color: rgba(0,0,0,0);
		border: 2px solid #FFFFFFFF;
		border-left: none;
		border-right: none;
		transition: 0.25s;
		font-size: 20px;
	}
	.Nav input[type = "button"]{
		color: #FFFFFF;
		font-size: 20px;
		margin-top: 15vh;
		margin-right: 10vw;
		background-color: rgba(0,0,0, 0);
		border: none;
		transition: 0.25s;
	}
	.NavButtons input[type = "submit"]:hover{
		/*background: #FFFFFFFF;*/
		background: rgba(0,0,0,0.4);
	}
	.NavButtons input[type = "submit"]:focus{
		background-color: rgba(0,0,0, 0.8);
	}
	.NavButtons input[type = "button"]:hover{
		color: #000000;
	}
	.ShowTimes{
		width: 100vw;
		height: 23.5vh;
		background: rgba(0,0,0, .3);
		float: right;
		top: 0;
		left: 0;
		position: absolute;
		color: #000000;
	}
	.ShowTheTime{
		color: #FFF1F0;
		width: 32vw;
		float: right;
		font-size: 25px;
		text-align: left;
	}
	.ShowTheTime>h2{
		margin-top: 2vh;
		margin-bottom: 2vh;
	}
	.ShowTheTime>div{
		text-align: center;
	}
	.ShowTheTime>h6{
		margin-top: 0;
		margin-bottom: 0;
	}
	.ShowTheTime>h1{
		margin-top: 2vh;
		margin-bottom: 2vh;
	}
	.ShowSubPage{
		margin-left: 25vw;
		margin-top: 20vh;
		margin-right: 10vh;
	}
</style>
