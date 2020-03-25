<template>
  <div id="app">
	<star-background></star-background>
	<router-view></router-view>
  </div>
</template>

<script>
	import Vue from 'vue'
	import VueRouter from 'vue-router'
	Vue.use(VueRouter);
	import StarBackground from './components/StarBackground.vue'
	export default {
		name: 'App',
		components: {
			StarBackground,
		},
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
