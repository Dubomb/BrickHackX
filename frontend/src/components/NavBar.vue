<template>
    <nav>
      <h1><a href="/">EcoRIT</a></h1>
      <a class="tiger-pledge" :href="items[0].url">{{ items[0].text }}</a>
      <ul>
        <!-- You can add more navigation items here if needed -->
      </ul>
    </nav>
  </template>
  
  <style scoped>
  nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #385A80;
    color: #fff;
    padding: 10px;
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
    padding: 5px 30px; /* Adjust padding as needed */
    margin-right: auto; /* Pushes the Tiger Pledge link to the right */
  }
  </style>
  
  <script>
  export default {
    data() {
      return {
        items: [
          { text: 'Tiger Pledge', url: '/pledge' }
        ]
      };
    }
  }
  </script>
  