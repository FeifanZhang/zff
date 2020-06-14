<template>
	<el-container class="el_container_overall">
		<el-header
				height="18%">
				<div class="ShowTheTime">
					<div>
						<span>张张报时：</span>
					</div>
					<div>
						<span>{{this.myTime.format("HH:mm")}}</span>
					</div>
					<div>
						<span>{{this.myTime.format("YYYY-MM-DD")}}</span>
						<span> {{this.dayNameMapping[this.myTime.weekday()]}}</span>
					</div>
				</div>
				<div class="ShowTheTime">
					<div class="text">
						<span>小猪报时：</span>
					</div>
					<div>
						<span>{{this.piggyTime.format("HH:mm")}}</span>
					</div>
					<div>
						<span>{{this.piggyTime.format("YYYY-MM-DD")}}</span>
						<span> {{this.dayNameMapping[this.piggyTime.weekday()]}}</span>
					</div>
				</div>
		</el-header>
		<el-container >
			<el-aside width="15vw" class="el_container_aside">
				<el-menu
						class="el-menu-aside"
						background-color="rgba(0,0,0, .5)"
						text-color="#fff"
						active-text-color="rgba(0,0,0)"
						:router=true
						>
					<el-menu-item
							class="aside_button"
							:index="this.path[0]+this.$route.query.token"
							>
						<i class="el-icon-picture-outline"></i>
						<span slot="title">照片</span>
					</el-menu-item>
					<el-menu-item
							class="aside_button"
							:index="this.path[1]+this.$route.query.token">
						<i class="el-icon-date"></i>
						<span slot="title">纪念日</span>
					</el-menu-item>
					<el-menu-item
							class="aside_button"
							:index="this.path[2]+this.$route.query.token">
						<i class="el-icon-menu"></i>
						<span slot="title">计时牌</span>
					</el-menu-item>
					<el-menu-item
							class="aside_button"
							:index="this.path[3]+this.$route.query.token">
						<i class="el-icon-chat-line-round"></i>
						<span slot="title">二人语录</span>
					</el-menu-item>
					<el-menu-item
							class="aside_button"
							:index="this.path[4]">
						<i class="el-icon-close"></i>
						<span slot="title">返回</span>
					</el-menu-item>
				</el-menu>
			</el-aside>
			<el-container class="el_container_main">
				<el-main>
					<router-view></router-view>
				</el-main>
			</el-container>
		</el-container>
		<el-footer>
			<el-menu
					class="el-menu-demo"
					mode="horizontal"
					background-color="#545c64"
					text-color="#fff"
					active-text-color="#ffd04b"
					:router=true>
				<el-menu-item
						:index="this.path[0]+this.$route.query.token">
					照片</el-menu-item>
				<el-menu-item
						:index="this.path[1]+this.$route.query.token">
					纪念日</el-menu-item>
				<el-menu-item
						:index="this.path[2]+this.$route.query.token">
					计时牌</el-menu-item>
				<el-menu-item
						:index="this.path[3]+this.$route.query.token">
					二人语录</el-menu-item>
				<el-menu-item
						:index="this.path[4]">
					返回</el-menu-item>
			</el-menu>
		</el-footer>
	</el-container>
</template>

<script>
import Vue from 'vue'
import VueRouter from 'vue-router'
import 'element-ui/lib/theme-chalk/display.css';
Vue.use(VueRouter);
let moment = require('moment-timezone');
moment.locale('zh-cn');
	export default {
		name: 'Heart',
		data() {
			return {
				isCollapsed: true,
				myTime:moment(),
				piggyTime:moment(),
				dayNameMapping:['星期一','星期二','星期三','星期四','星期五','星期六','星期日'],
				path:[
						'/homepage/photos?token=',
						'/homepage/anniversary?token=',
						'/homepage/clock?token=',
						'/homepage/words?token=',
						'/login'
				]
			}
		},
		// mounted() {
		// 	window.onresize=function(){
		// 		// clientWidth > clientHeight时，显示aside 不显示footer 反之则显示footer，不显示aside
		// 		this.isCollapsed = document.documentElement.clientWidth <= document.documentElement.clientHeight;
		// 		console.log(this.isCollapsed)
		// 	}
		// },
		created() {
			if (this.$route.query.token === undefined){
				this.$router.replace('/login');
			}else{
				this.setClock();
				setInterval(()=>{this.setClock()}, 10000);
				// clientWidth > clientHeight时，显示aside 不显示footer 反之则显示footer，不显示aside
				// this.isCollapsed = document.documentElement.clientWidth <= document.documentElement.clientHeight;
				this.$router.replace({ path: '/homepage/clock', query: { token: this.$route.query.token } });
				console.log(this.$route.query.token);
			}
		},
		methods:{
			setClock:function(){
				this.piggyTime = moment().tz("Asia/Shanghai");
				this.myTime = moment().tz("America/Chicago");
			},
			returnToLogin:function(){
				this.$router.replace('/login');
			},
		}
	}
</script>

<style>
	body{
		margin: 0;
	}

	@media screen and (orientation:portrait){
		.el-footer{
			display: block!important;
			width: 100%;
			height: 7%!important;
			padding: 0;
		}
		.el_container_aside{
			display: none;
		}

		.el-menu{
			width: 100%;
		}

		.el-menu-item{
			width: 20%;
		}

		.ShowTheTime{
			font-size: 5vw!important;
			width: 50%!important;
		}
		.el-header{
			height: 13%!important;
		}

		.el-main{
			padding: 0;
		}

	}

	.el-footer{
		display:none;
	}

	.ShowTheTime{
		color: #FFF1F0;
		width: 40%;
		height: 100%;
		float: right;
		font-size: 3vh;
		text-align: left;
	}

	.el-menu-item>span{
		font-size: 2.7vh;
	}

	.el-menu-aside:not(.el-menu--collapse){
		width: 15vw;
	}
	.el_container_overall{
		width: 100vw;
		height: 100vh;
	}

	.el-header {
		width: 100%;
		background-color:rgba(0,0,0, .6);
		opacity: 0.7;
		color: #333;
		text-align: center;
		padding-left: 0;
		padding-right: 0;
	}

	.el-aside {
		text-align: center;
		line-height: 16vh;
	}

	.el-main {
		height: 100%;
		width: 100%;
		background: rgba(0,0,0, .5);
		color: #333;
		text-align: center;
		padding-top: 0;
		padding-bottom: 0;
	}
	.el-menu-aside {
		width: 100%;
		height: 100%;
	}
	.el-menu-item{
		height: 16.4vh;
		line-height: 16vh;
	}
	.el-menu{
		opacity: 0.7;
	}
	.ShowTheTime>div{
		height: 30%;
		margin-top: 0;
		margin-bottom: 0;
	}


</style>
