<template>
	<body>
	<div class="starBackground">
		<div v-for="(item, index) in star_num" :key="index"  class="stars" ref="stars"></div>
	</div>
	</body> 
</template>

<script>
	export default {
		name: 'StarBackground',
		data: function(){
			return {
				star_num: 800,
				dist: 800,
			}
		},
		mounted(){
			var _this = this;
			var starArr = _this.$refs.stars;
			starArr.forEach(item => {
				var speed = 0.2 + (Math.random() * 1);
				var thisDist = _this.dist + (Math.random() * 300);
				item.style.transformOrigin = `0 0 ${thisDist}px`;
				item.style.transform =`translate3d(0,0,-${thisDist}px) rotateY(${(Math.random() * 360)}deg) rotateX(${(Math.random() * -50)}deg) scale(${speed},${speed})`
			})
		}
		
	}
</script>

<style lang="less" >
		body{
			background: radial-gradient(200% 100% at bottom center, #f7f7b6, #e96f92, #1b2947);
			background: radial-gradient(220% 105% at top center, #1b2947, 10%, #75517d, 40%, #e96f92 65%, #f7f7b6);
			background-attachment: fixed;
			overflow: hidden;
		}
		@keyframes rotate{
			0%{
				transform: perspective(400px) rotateZ(20deg) rotateX(-40deg) rotateY(0);
			}
			100%{
				transform: perspective(400px) rotateZ(20deg) rotateX(-40deg) rotateY(-360deg);
			}
		}
		.starBackground{
			transform: perspective(500px);
			transform-style: preserve-3d;
			position: absolute;
			perspective-origin: 50% 100%;
			left: 50%;
			animation: rotate 90s infinite linear;
			bottom: 0;
		}
		.stars{
			width: 2px;
			height: 2px;
			background: #f7f7b8;
			position: absolute;
			color: #000000;
			top: 0;
			left: 0;
			backface-visibility: hidden;
		}
</style>
