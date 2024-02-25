<template>
    <div class="card" @click="handleCardClick">
      <h2>{{ location.buildingEmoji }} {{ location.building }}</h2>
      <span>&rarr;</span>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      location: {
        type: Object,
        required: true
      }
    },
    methods: {
        handleCardClick() {
            this.$emit('building-clicked', this.location);
        }
    }, 
  };
  </script>
  
  <style scoped>
  .card {
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 15px;
    margin-bottom: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #3D5A80;
    transition: box-shadow .5s;
  }
  .card:hover {
    box-shadow: 0px 8px 10px rgba(61, 90, 128, 1);
  }
  
  h2 {
    margin-top: 0;
  }
  
  p {
    margin: 0;
    margin-bottom: 10px;
  }
  
  strong {
    font-weight: bold;
  }
  </style>
  