<template>
    <div class="progress-container">
        <h2>Progress</h2>
        <div class="progress-bar" :style="{ width: progress + '%' }"></div>
    <div class="controls">
      <button @click="increment">+</button>
      <button @click="decrement">-</button>
    </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            progress: 0 // all goal progress starts at 0
        };
    },

    methods: {
        increment() {
            if (this.progress < 100) {  // need to replace with actual goal instead of 100
                this.progress += 1; 
            }
        },

        decrement() {
            if (this.progress > 0) {
                this.progress -= 1;
            }
        }
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
