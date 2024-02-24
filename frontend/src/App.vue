<template>
  <div id="app">
    <!-- Include the navigation bar component -->
    <NavBar @pledge-click="displayPledgeComponent"/>
    <!-- Display different components based on user interaction -->
    <div v-if="showPledgeComponent">
      <!-- Include TigerPledge when showPledgeComponent is true -->
      <TigerPledge/>
    </div>
    <div v-else>
      <router-view/>
    </div>
  </div>
</template>

<script>
// Import the navigation bar component
import NavBar from './components/NavBar.vue';
// Import the component you want to display for the Tiger Pledge
import TigerPledge from './components/TigerPledge.vue';

export default {
  name: 'App',
  components: {
    // Register the navigation bar component
    NavBar,
    // Register the Tiger Pledge component
    TigerPledge
  },
  data() {
    return {
      // Flag to determine whether to display TigerPledge
      showPledgeComponent: false
    };
  },
  methods: {
    // Method to handle the click event from NavBar component
    displayPledgeComponent() {
      // Set the flag to true to display TigerPledge
      this.showPledgeComponent = true;
    }
  }
};
</script>

<style>
#app {
  font-family: Arial, Helvetica, sans-serif;
  margin-top: 20px;
}
</style>

