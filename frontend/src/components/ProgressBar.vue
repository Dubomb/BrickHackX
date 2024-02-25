<template>
  <div class="progress-container">
    <h2>Progress</h2>
    <div class="progress-bar" :style="{ width: percent + '%' }"></div>
    <div class="controls">
      <button @click="decrement">-</button>
      <button @click="increment">+</button>
      <p>{{ percent }}%</p>
    </div>
  </div>
</template>

<script>
export default {
  props: ['start', 'current', 'endGoal'],
  data() {
    return {
      start_amount: 0,
      current_amount: 0,
      goal_amount: 0,
      percent: 0,
    };
  },
  mounted() {
    this.start_amount = this.start;
    this.current_amount = this.current;
    this.goal_amount = this.endGoal;
    this.percent = this.calcPercent();
  },
  methods: {
    increment() {
      this.current_amount += 1;
      if (this.current_amount === this.goal_amount) {
        this.goal_amount *= 2;
        this.start_amount = this.current_amount;
      }

      this.percent = this.calcPercent();

      this.changeGoal();
    },
    decrement() {
      if (this.current_amount === this.start_amount) {
        return;
      }

      this.current_amount -= 1;
      this.percent = this.calcPercent();

      this.changeGoal();
    },
    calcPercent() {
      return (this.current_amount - this.start) / (this.endGoal - this.start) * 100;
    },
    changeGoal() {
      this.$emit('onGoalChange', this.start_amount, this.current_amount, this.goal_amount);
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