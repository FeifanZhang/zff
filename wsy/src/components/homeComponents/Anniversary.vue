<template>
	<div class="ShowAnn">
		<table>
			<tr v-for="(value, index) in date" :key="index">
				<td ><h2>{{value[0].format("YYYY-MM-DD")}}</h2></td>
				<td align="left"><h2>{{value[1]}}</h2></td>
			</tr>
		</table>
	</div>
</template>

<script>
let moment = require("moment");
moment.locale('zh-cn');
	export default {
		name: 'Clock',
		data() {
			return {
				date:[
						[moment("2018-02-26"), "第1次见面"],
						[moment("2018-03-04"), "在一起第1天"],
						[moment("2018-03-29"),"张张第1个生日"],
						[moment("2018-03-04").add(100, "days"), "在一起100天纪念日"],
						[moment("2019-01-15"), "小猪的第1个生日"],
						[moment("2019-12-31"),"第1次跨年"],	
				]
			}
		},
		created() {
			this.setAnniversary();
			console.log(this.date)
		},
		onLoad() {
	
		},
		methods:{
			setAnniversary:function(){
				const len = this.date.length;
				for (let v=1; v<10; v++){
					for (let i=0; i<len; i++){
						if(i == 0){
							this.date.push(
								[moment("2018-02-26").add(v, "years"), "第1次见面"+v+"年"], 
							);
						}else if(i == 1){
							this.date.push(
								[moment("2018-03-04").add(v, "years"), "在一起第"+(v+1)+"年"], 
							);
						}else if(i == 2){
							this.date.push(
								[moment("2018-03-29").add(v, "years"), "张张第"+(v+1)+"生日"], 
							);
						}else if(i == 3){
							this.date.push(
								[moment("2018-03-04").add((v+1)*100, "days"), "在一起"+(v+1)*100+"天纪念日"], 
							);
						}else if(i == 4){
							this.date.push(
								[moment("2019-01-15").add(v,"years"), "小猪的第"+(v+1)+"生日"],
							);
						}else{
							this.date.push(
								[moment("2019-12-31").add(v,"years"), "第"+(v+1)+"次跨年"],
							);
						}
					}
				}
				this.date.sort(function(a,b){return a[0].diff(b[0], "days")})
			},
		},
	}
</script>
<style>
	.ShowAnn{
		width: 100vw;
		height: 60vh;
		overflow: auto;
	}
	.ShowAnn>table{
		width: 100%;
	}
</style>
