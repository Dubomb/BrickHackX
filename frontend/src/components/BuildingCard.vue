<template>
    <div class="card">
      <h2>{{ location.building }}</h2>
      <p><strong>Code:</strong> {{ location.abbreviation }}</p>
      <p><strong></strong> {{ location.descShort }}</p>
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
  };
  </script>
  
  <style scoped>
  .card {
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 15px;
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
  