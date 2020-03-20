<template>
	<div class="Words">
		<div class="ShowWords">
			<h2>AAAAAAA</h2>
			<h2>SSSSSSSS</h2>
			<h2>DDDDDDDD</h2>
			<h2>DDDDDDDD</h2>
			<h2>DDDDDDDD</h2>
			<h2>DDDDDDDD</h2>
			<h2>DDDDDDDD</h2>
			<h2>DDDDDDDD</h2>
			<h2>DDDDDDDD</h2>
			<h2>DDDDDDDD</h2>
			<h2>DDDDDDDD</h2>
			<h2>DDDDDDDD</h2>
			<h2>DDDDDDDD</h2>
			<h2>DDDDDDDD</h2>
			<h2>DDDDDDDD</h2>
		</div>
		<form class="InputWords">
			<textarea id="inputBar" placeholder="想说什么就往里面写吧!"></textarea>
			<input id="send" type="submit" value="发送"/>
		</form>
	</div>
</template>

<script>
	import {mapState, mapGetters} from "vuex";
	import axios from "axios"
	let moment = require("moment");
	moment.locale('zh-cn');
	export default {
		name: 'Words',
		data(){
			return{
				words:{

				}
			}
		},
		computed:{
			...mapGetters(["get_token"]),	
		},
		methods: {

		},
		created() {
			
		}
	}

</script>

<style>
	.Words{
		width: 80vw;
		height: 70vh;
	} 
	.ShowWords{
		width: 100%;
		height: 80%;
		overflow: auto;
		margin-bottom: 3vh;
	}
	.InputWords{
		width: 90%;
		height: 10%;
	}
	.InputWords #inputBar{
		width: 80%;
		font-size: 3vh;
		height: 50%;
		background-color: rgba(0, 0, 0, .2);
		border-radius: 20px;
		margin-left: 3vw;
		float: left;
		overflow: hidden;
		color: white;
	}
	.InputWords #send{
		border: 0;
		background: rgba(0,0,0, .4);
		display: block;
		width: 10%;
		padding-top: 1%;
		padding-bottom: 1%;
		font-size: 2vh;
		text-align: center;
		outline: none;
		color: white;
		border-radius: 24px;
		transition: 0.25s;
		float: right;
	}
</style>
