<template>
    <div class="card">
        <h2>{{ goal.title }}</h2>
        <p>{{ goal.description }}</p>
        <p>{{ goal.current_amount }} out of {{ goal.goal_amount }}</p>
        <ProgressBar @onGoalChange="changeGoal"
        :start="goal.start_amount" 
        :current="goal.current_amount" 
        :end-goal="goal.goal_amount"
        ></ProgressBar>
    </div>
</template>


<script>
import ProgressBar from './ProgressBar.vue';
export default {
    name: "GoalCard",

    components: {
        ProgressBar
    },

    methods: {
        changeGoal(start, current, goal) {
            console.log(this.goal.id);
            this.$emit('onChangeGoal', this.goal.id, start, current, goal);
        }
    },

    props: ['goal'],
}
</script>

<style scoped>
.card {
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 15px;
    margin-bottom: 20px;
    color: #3D5A80;
}

h2 {
    margin-top: 0;
}

p {
    margin: 0;
    margin-bottom: 10px;
}
</style>