<template>
	<div class="Words">
		<el-container class="el-container-word">
			<el-main width="20%" class="avatar">
				<img src="../../assets/photos/wsy.png"/>
			</el-main>
			<el-aside width="80%" class="words-aside">
				<el-table class="words-table"
						:data="this.wsywords"
						style="width: 100%"
						height="100%">
					<el-table-column
							prop="word"
							label="小猪说过的话"
							width="180">
					</el-table-column>
					<el-table-column
							prop="date_created"
							label="时间"
							width="180">
					</el-table-column>
				</el-table>
			</el-aside>
		</el-container>
		<el-container class="el-container-word">
			<el-aside width="80%" class="words-aside">
				<el-table
						class="words-table"
						:data="this.zffwords"
						style="width: 100%"
						height="100%">
					<el-table-column
							prop="word"
							label="张张说过的话"
							width="180">
					</el-table-column>
					<el-table-column
							prop="date_created"
							label="时间"
							width="180">
					</el-table-column>
				</el-table>
			</el-aside>
			<el-main width="20%" class="avatar">
				<img src="../../assets/photos/zff.png"/>
			</el-main>
		</el-container>
	</div>
</template>

<script>
	//import {mapState} from "vuex";
	import {wordRequest} from "../../request.js";
	let moment = require("moment");
	moment.locale('zh-cn');
	export default {
		name: 'Words',
		data(){
			return{
				token: '',
				wsywords: [],
				zffwords:[],
				word_insert: '',
			}
		},
		methods: {
			initwords(words){
				words.forEach(element=>{
					element.date_created = moment(element.date_created).format("YYYY-MM-DD")
				})
			},
			postWord(){
				wordRequest({
					method: 'post',
					data:{
						owner: true,
						word: this.word_insert,
					}
				}).then(res=>{
					this.words.push({id:res.data.id, owner: res.data.owner, date_created: res.data.date_created, word: res.data.word})
				}).catch(res=>{
					console.log(res)
				})
			},
		},
		created() {
			if (this.$route.query.token === undefined){
				this.$router.replace({path:'/login'})
			}else{
				this.token = this.$route.query.token;
				wordRequest({
					method: 'get',
					params: {
						token: this.token
					}
				}).then(res =>{
					this.initwords(res.data.wsywords);
					this.initwords(res.data.zffwords);
					this.wsywords = res.data.wsywords;
					this.zffwords = res.data.zffwords;
				}).catch(res => {
					console.log(res);
				})
			}
		}
	}

</script>

<style>
	@media screen and (orientation:portrait){
		.Words .el-container .el-main{
			display: none;
		}

		.Words.el-container.el-aside{
			display: block!important;
		}

		.words-aside{
			width: 100%!important;
		}

		.el-container-word{
			margin-top: 3vh;
			margin-bottom: 3vh;
		}

		.el-table__header {
			font-size: 2.5vw;
		}

		.el-table__body{
			font-size: 1.5vw;
		}

		/*.el-table{*/
		/*	width: 100%;*/
		/*}*/
	}

	.el-table th, .el-table tr,.words-table  {
		background-color: transparent;
	}
	/*.words-table{*/
	/*	background-color: transparent;*/
	/*}*/

	.words-aside{
		line-height: 0 !important;
	}

	.avatar{
		background-color: transparent !important;
		padding: 0;
	}

	img{
		width: 80%;
		height: 100%;
	}
	.Words{
		width: 100%;
		height: 100%;
	}

	.el-table{
		color: black;
		/*font-size: large;*/
	}

	.el-table__body, .el-table__header {
		width: 100% !important;
		background-color: transparent;
		font-size: 2.5vh;
	}

	.el-container-word{
		height: 45% ;
		margin-bottom: 2vh;
		margin-top: 2vh;
	}

</style>
