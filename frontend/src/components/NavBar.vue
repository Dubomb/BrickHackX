<template>
  <nav>
    <h1><a href="/">EcoRIT</a></h1>
    <a class="tiger-pledge" @click="handlePledgeClick">{{ items[0].text }}</a>
    <ul>
      <!-- You can add more navigation items here if needed -->
    </ul>
    <button class="login-button">Login</button>
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

<style>
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: white;
  color: #385A80;
  font-size: 20px;
  border-bottom: #385A80 solid 2px;
  box-sizing: border-box; /* Include padding and border in the element's total width and height */
  width: 100%; 
  padding-left: 20px;
  padding-right: 20px;

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
  color: #385A80;
  text-decoration: none;
}
a:hover {
  color: #98C1D9;
  transition: color .5s;
}

.login-button {
  color: #385A80;
  font-size: 20px;
  background-color: transparent;
  cursor: pointer;
  border: none;
  padding: 30px;

}

.tiger-pledge {
  padding: 15px 30px; /* Adjust padding as needed */
  margin-right: auto; /* Pushes the Tiger Pledge link to the right */
  cursor: pointer;
}
</style>


  