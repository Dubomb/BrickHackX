<template>
    <h2>{{ goal.title }}</h2>
    <p>{{ goal.description }}</p>
    <p>{{ goal.current_amount }} out of {{ goal.goal_amount }}</p>
    <p>{{ goal.category }}</p>
    <ProgressBar 
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
    props: ['goal']
}
</script>

<style scoped>

</style>