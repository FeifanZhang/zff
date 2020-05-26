<template>
	<div class="Words">
		<div class="ShowWords">
			<h2 v-for="word in this.words" :key="word.id">{{word.word}}</h2>
		</div>
		<textarea id="inputBar" v-model="this.word_insert" @keydown.enter="this.postWord" placeholder="想说什么就往里面写吧!"></textarea>
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
				words: [],
				word_insert: '',
			}
		},
		methods: {
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
					this.words = res.data.words
				}).catch(res => {
					console.log(res);
				})
			}
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

	#inputBar{
		width: 80%;
		font-size: 3vh;
		height: 5%;
		background-color: rgba(0, 0, 0, .2);
		border-radius: 20px;
		margin-left: 3vw;
		float: left;
		overflow: hidden;
		color: white;
	}
</style>
