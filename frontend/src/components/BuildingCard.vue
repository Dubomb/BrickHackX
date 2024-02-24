<template>
    <div class="BuildingCard">
      <h2>{{ location.descShort }}</h2>
      <p><strong>Building:</strong> {{ location.building }}</p>
      <p><strong>Abbreviation:</strong> {{ location.abbreviation }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      location: {
        type: Object,
        required: true
      }
    }
  };
  </script>
  
  <style scoped>
  .card {
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-bottom: 20px;
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
  