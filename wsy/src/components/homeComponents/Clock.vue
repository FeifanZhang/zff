<template>
	<div class="Clock">
		<h2>在一起已经：</h2>
		<div class="Time">
			<div id="day"><span >{{this.days}}</span><span>天</span></div>
			<div id="hour"><span >{{this.hours}}</span><span>小时</span></div>
			<div id="min"><span >{{this.mins}}</span><span>分钟</span></div>
		</div>
	</div>
</template>

<script>
let moment = require('moment-timezone');
moment.locale('zh-cn');
	export default {
		name: 'Clock',
		data() {
			return {
				days:moment(),
				hours:"",
				mins:"",
			}
		},
		created() {
			this.clock();
			setInterval(()=>{this.clock()}, 10000)
		},
		methods:{
			clock:function(){
				this.days = moment().tz("Asia/Shanghai").diff(moment("20180304"), "days");
				this.hours = moment().hours() < 10 ? '0'+moment().hours() : moment().hours();
				this.mins = moment().minutes() < 10 ? '0'+moment().minutes() : moment().minutes();
			},
		},
	}
</script>
<style>
	@media screen and (orientation:portrait){

		.Clock .Time div:last-child span{
			display: none;
		}


		.Clock .Time #hour{
			display: none;
		}

		.Clock .Time div:first-child span{
			width: 96%!important;
		}

		.Time div{
			width: 90%!important;
		}

		.Clock .Time{
			margin-left: 0;
		}
	}

	.Clock{
		text-align: center;
		height: 100%;
		width: 100%;
	}
	.Clock>h2{
		color: #FFF1F0;
		text-align: center;
		font-weight: 800;
		font-size: 5vh;
		letter-spacing: 1vw;
		margin-bottom: 5vh;
	}
	.Time{
		height: 100%;
		width: 100%;

	}
	.Time>div{
		float: left;
		margin-left: 5%;
		width: 25%;
		position: relative;
		-webkit-box-reflect: below 1px linear-gradient(transparent,#0004);
	}
	.Time>div>span{
		width: 16.7vw;
		background-color: rgba(33, 150, 243, .4);
		color: #fff;
		display: flex;
		justify-content: center;
		align-items: center;
		font-size: 9em;
		z-index: 10;
	}

	.Time>div>span:nth-child(2){
		height: 10vh;
		font-size: 2em;
		background-color: rgba(18,127,214, .4);
	}
	.Clock .Time div:last-child span{
		background-color: rgba(236,0,98, .4);
	}
</style>
