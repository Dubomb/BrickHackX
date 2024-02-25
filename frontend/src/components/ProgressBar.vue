<template>
  <div class="progress-container">
    <h3>Progress</h3>
    <div class="progress-background">
      <div class="progress-bar" :style="{ width: percent + '%' }"></div>
    </div>
    <div class="controls">
      <button @click="decrement"><strong>-</strong></button>
      <button @click="increment"><strong>+</strong></button>
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
        this.percent = 0;
      } else {
        this.percent = this.calcPercent();
      }

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

.progress-background {
  background-color: rgb(227, 224, 224);
}

.progress-bar {
  height: 20px;
  background-color: #42b983; 
}

.controls {
  margin-top: 10px;
}

button {
  width: 30px;
  height: 30px;
  background-color: rgb(253, 250, 250);
  border-radius: 5px;
  border: none;
  box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.2);
  margin: 0px 10px;
}

button:hover {
  background-color: rgb(222, 220, 220);
  transition: background-color 0.3s;
}
</style>