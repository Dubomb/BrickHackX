<template>
  <div class="progress-container">
    <h2>Progress</h2>
    <div class="progress-bar" :style="{ width: progress + '%' }"></div>
    <div class="controls">
      <button @click="decrement">-</button>
      <button @click="increment">+</button>
      <p>{{ progress }}%</p>
    </div>
  </div>
</template>

<script>
export default {
  props: ['start', 'current', 'endGoal'],
  data() {
    return {
      progress: 0 // Local data property for progress
    };
  },
  mounted() {
    this.progress = this.start;
  },
  methods: {
    increment() {
      if (this.progress < 100) {
        this.progress += 10;
      }
    },
    decrement() {
      if (this.progress > 0) {
        this.progress -= 10;
      }
    },
  }
};
</script>

<style scoped>
.progress-container {
  width: 100%;
}

.progress-bar {
  height: 20px;
  background-color: #42b983; 
}

.controls {
  margin-top: 10px;
}

button {
  margin-right: 10px;
}
</style>