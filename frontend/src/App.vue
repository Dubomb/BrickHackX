<template>
  <div id="app">
    <!-- Include the navigation bar component -->
    <NavBar/>
    <!-- Your main content here -->
    <router-view/>
  </div>
</template>

<script>
// Import the navigation bar component
import NavBar from './components/NavBar.vue';

export default {
  name: 'App',
  components: {
    // Register the navigation bar component
    NavBar
  }
}
</script>

<style>
#app {
  font-family: Arial, Helvetica, sans-serif;
  margin-top: 20px;
}
</style>
