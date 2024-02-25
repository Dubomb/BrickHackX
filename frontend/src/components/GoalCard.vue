<template>
    <h2>{{ goal.title }}</h2>
    <p>{{ goal.description }}</p>
    <p>{{ goal.current_amount }} out of {{ goal.goal_amount }}</p>
    <ProgressBar @onGoalChange="changeGoal"
      :start="goal.start_amount" 
      :current="goal.current_amount" 
      :end-goal="goal.goal_amount"
    ></ProgressBar>
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

</style>