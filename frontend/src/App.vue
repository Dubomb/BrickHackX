<template>
  <div id="app">
    <div v-html="linkTags"></div>
    <!-- Include the navigation bar component -->
    <NavBar @pledge-click="displayPledgeComponent"/>
    <!-- Display different components based on user interaction -->
    <div v-if="showPledgeComponent">
      <!-- Include TigerPledge when showPledgeComponent is true -->
      <TigerPledge/>
    </div>
    <div v-else>
      <BarsAndMap/>
      <router-view/>
    </div>
  </div>
</template>

<script>
// Import the navigation bar component
import BarsAndMap from './components/BarsAndMap.vue';
import NavBar from './components/NavBar.vue';
// Import the component you want to display for the Tiger Pledge
import TigerPledge from './components/TigerPledge.vue';

export default {
  name: 'App',
  components: {
    // Register the navigation bar component
    NavBar,
    // Register the Tiger Pledge component
    TigerPledge,
    BarsAndMap
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
  },
  computed: {
    linkTags() {
      return `
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Mukta:wght@200;300;400;500;600;700;800&display=swap" rel="stylesheet">
      `;
    }
  }
};
</script>

<style>
#app {
  font-family: Mukta;
  margin-top: 20px;
}
/* cute google font */
.mukta-extralight {
  font-family: "Mukta", sans-serif;
  font-weight: 200;
  font-style: normal;
}

.mukta-light {
  font-family: "Mukta", sans-serif;
  font-weight: 300;
  font-style: normal;
}

.mukta-regular {
  font-family: "Mukta", sans-serif;
  font-weight: 400;
  font-style: normal;
}

.mukta-medium {
  font-family: "Mukta", sans-serif;
  font-weight: 500;
  font-style: normal;
}

.mukta-semibold {
  font-family: "Mukta", sans-serif;
  font-weight: 600;
  font-style: normal;
}

.mukta-bold {
  font-family: "Mukta", sans-serif;
  font-weight: 700;
  font-style: normal;
}

.mukta-extrabold {
  font-family: "Mukta", sans-serif;
  font-weight: 800;
  font-style: normal;
}

</style>

