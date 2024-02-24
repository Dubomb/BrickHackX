<template>
    <div class="TigerPledge">
      <h1>{{ msg }}</h1>
      <p>
        Welcome to your very own sustainability journal! Start your EcoRIT pledge today by setting 
        your own personal goals. Let's make our pledge to the planet a reality 🌎
      </p>

      <div class="button-container">
      <Cbutton class="water-button">Water</Cbutton>
      <Cbutton class="food-button">Food</Cbutton>
      <Cbutton class="recycling-button">Recycling</Cbutton>
      </div>
    </div>

  </template>
  
  <script>
  export default {
    name: 'TigerPledge',
    props: {
      msg: String
    }
  }
  </script>

  <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.TigerPledge {
    text-align: center;
}

.button-container {
  text-align: center;
  margin-top: 30px;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.water-button {
  background-color: #98C1D9;
  color: #fff;
  border: none;
  padding: 15px 150px;
  margin-right: 30px;
  cursor: pointer;
  border-radius: 12px;
}

.food-button {
  background-color: #ED874C;
  color: #fff;
  border: none;
  padding: 15px 150px;
  margin-right: 30px;
  cursor: pointer;
  border-radius: 12px;
}

.recycling-button {
  background-color: #279D41;
  color: #fff;
  border: none;
  padding: 15px 150px;
  margin-right: 30px;
  cursor: pointer;
  border-radius: 12px;
}

.water-button:hover {
  background-color: #3D5A80;
}

.food-button:hover {
  background-color: #3D5A80;
}

.recycling-button:hover {
  background-color: #3D5A80;
}
</style>
