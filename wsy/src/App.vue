<template>
  <div id="app">
	<StarBackground></StarBackground>
	<Login></Login>
	<Nav></Nav>
  </div>
</template>

<script>
import StarBackground from './components/StarBackground.vue'
import Login from './components/Login.vue'
import Nav from './components/homeComponents/Nav.vue'
export default {
  name: 'App',
  components: {
	StarBackground,
	Login,
	Nav,
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
