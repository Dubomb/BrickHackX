<template>
  <nav>
    <h1><a href="/">EcoRIT</a></h1>
    <a class="tiger-pledge" @click="handlePledgeClick">{{ items[0].text }}</a>
    <ul>
      <!-- You can add more navigation items here if needed -->
    </ul>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      items: [
        { text: 'Tiger Pledge 🐾', url: '/pledge' }
      ]
    };
  },
  methods: {
    handlePledgeClick(event) {
      // Prevent the default behavior of the anchor element
      event.preventDefault();
      // Emit the pledge-click event
      this.$emit('pledge-click');
    }
  }
}
</script>

<style scoped>
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #385A80;
  color: #fff;
  padding: 8px;
  font-size: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline;
  margin-right: 10px;
}

a {
  color: #fff;
  text-decoration: none;
}

.tiger-pledge {
  padding: 15px 30px; /* Adjust padding as needed */
  margin-right: auto; /* Pushes the Tiger Pledge link to the right */
}
</style>


  