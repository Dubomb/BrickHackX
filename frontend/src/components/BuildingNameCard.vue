<template>
    <div class="card" @click="handleCardClick">
      <h2>{{ location.building }}</h2>
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
  