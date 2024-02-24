<template>
    <h2>{{ goal.title }}</h2>
    <p>{{ goal.description }}</p>
    <p>{{ goal.current_amount }} out of {{ goal.goal_amount }}</p>
    <p>{{ goal.category }}</p>
</template>

<script>
export default {
    name: "GoalCard",
    props: ['goal']
}
</script>

<style scoped>

</style>