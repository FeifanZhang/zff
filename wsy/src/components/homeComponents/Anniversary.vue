<template>
	<div class="ShowAnn">
		<el-table
				:data="this.date"
				style="width: 100%"
				height="100%"
		>
			<el-table-column
					prop="time"
					label="日期"
					width="180">
			</el-table-column>
			<el-table-column
					prop="info"
					label="纪念日"
					width="180">
			</el-table-column>
			<el-table-column
					prop="countdown"
					label="倒计时"
					width="180">
			</el-table-column>
		</el-table>
	</div>
</template>

<script>
let moment = require("moment");
moment.locale('zh-cn');
	export default {
		name: 'Clock',
		data() {
			return {
				date:[{
					time:moment("2018-02-26"),
					info:"第1次见面",
					countdown:"check!"
				}, {
					time:moment("2018-03-04"),
					info:"在一起第1天",
					countdown:"check!",
				}, {
					time:moment("2018-03-29"),
					info:"张张第1个生日",
					countdown:"check!",
				}, {
					time:moment("2018-03-04").add(100, "days"),
					info:"在一起100天纪念日",
					countdown:"check!",
				}, {
					time:moment("2019-01-15"),
					info:"小猪的第1个生日",
					countdown:"check!",
				}, {
					time:moment("2019-12-31"),
					info:"第1次跨年",
					countdown:"check!",
				},]
			}
		},
		created() {
			this.setAnniversary();
			// console.log(this.date)
		},
		methods:{
			setAnniversary:function(){
				const len = this.date.length;
				for (let v=1; v<10; v++){
					for (let i=0; i<len; i++){
						if(i == 0){
							let time = moment("2018-02-26").add(v, "years");
							let countdown = time.diff( moment().tz("Asia/Shanghai"), "days");
							this.date.push({
								time:time,
								info:"第1次见面"+v+"年",
								countdown: countdown>0 ? "还有"+countdown+"天！": "check!"},
							);
						}else if(i == 1){
							let time = moment("2018-03-04").add(v, "years");
							let countdown = time.diff( moment().tz("Asia/Shanghai"), "days");
							this.date.push({
								time:time,
								info:"在一起第"+(v+1)+"年",
								countdown: countdown>0 ? "还有"+countdown+"天！": "check!"},
							);
						}else if(i == 2){
							let time = moment("2018-03-29").add(v, "years");
							let countdown = time.diff( moment().tz("Asia/Shanghai"), "days");
							this.date.push({
								time:time,
								info:"张张第"+(v+1)+"生日",
								countdown: countdown>0 ? "还有"+countdown+"天！": "check!"},
							);
						}else if(i == 3){
							let time = moment("2018-03-04").add((v+1)*100, "days");
							let countdown = time.diff( moment().tz("Asia/Shanghai"), "days");
							this.date.push({
								time:time,
								info:"在一起"+(v+1)*100+"天纪念日",
								countdown: countdown>0 ? "还有"+countdown+"天！": "check!"},
							);
						}else if(i == 4){
							let time = moment("2018-01-15").add(v, "years");
							let countdown = time.diff( moment().tz("Asia/Shanghai"), "days");
							this.date.push({
								time:time,
								info:"小猪的第"+(v+1)+"生日",
								countdown: countdown>0 ? "还有"+countdown+"天！": "check!"},
							);
						}else{
							let time = moment("2018-12-31").add(v, "years");
							let countdown = time.diff( moment().tz("Asia/Shanghai"), "days");
							this.date.push({
								time:time,
								info:"第"+(v+1)+"次跨年",
								countdown: countdown>0 ? "还有"+countdown+"天！": "check!"},
							);
						}
					}
				}
				this.date.sort(function(a,b){return a.time.diff(b.time, "days")});
				this.date.forEach(element=>{
					element.time = element.time.format("YYYY-MM-DD")
				})
			},
		},
	}
</script>
<style>
	.ShowAnn{
		width: 100%;
		height: 80vh;
		overflow: auto;
	}

	/*与下面的 .el-table结合使得表格头部和身体透明*/
	.el-table th, .el-table tr {
		background-color: transparent;
	}

	.el-table__body, .el-table__header {
		width: 100% !important;
		opacity: 0.7;
	}
	.el-table{
		background-color: transparent;
		color: #000000;
		font-size: larger;
		font-weight: 700;
	}

</style>
