<template>
  <div id="app">
    <!-- Include the navigation bar component -->
    <NavBar/>
    <BarsAndMap/>
    <!-- Your main content here -->
    <router-view/>
  </div>
</template>

<script>
// Import the navigation bar component
import BarsAndMap from './components/BarsAndMap.vue';
import NavBar from './components/NavBar.vue';

export default {
  name: 'App',
  components: {
    // Register the navigation bar component
    NavBar,
    BarsAndMap
}
}
</script>

<style>
#app {
  font-family: Arial, Helvetica, sans-serif;
  margin-top: 20px;
}
</style>
