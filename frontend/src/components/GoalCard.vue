<template>
    <h2>{{ goal.title }}</h2>
    <p>{{ goal.description }}</p>
    <p>{{ goal.current_amount }} out of {{ goal.goal_amount }}</p>
    <p>{{ goal.category }}</p>
    <ProgressBar :progress="goal.progress"></ProgressBar>
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