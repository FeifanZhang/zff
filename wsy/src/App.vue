<template>
  <div id="app">
      <star-background></star-background>
      <transition name="fade">
          <router-view></router-view>
      </transition>
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
    /* 为对应的路由跳转时设置动画效果 */
    .fade-enter-active, .fade-leave-active {
        transition: opacity .5s
    }
    .fade-enter, .fade-leave-to {
        opacity: 0
    }
    #app {
      font-family: Avenir, Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-align: center;
      color: #2c3e50;
      margin-top: 0;
    }
</style>
