<template>
    <h2>Create a goal!</h2>
    <form @submit.prevent="onSubmit" @submit="$emit('onCreateGoal', {'title': this.title, 'description': this.description, 'current_amount': 0, 'goal_amount': this.goal_amount})">
        <label>Title:</label>
        <input type="text" required="true" v-model="title"/>
        <label>Description:</label>
        <input type="text" required="true" v-model="description"/>
        <label>Goal amount:</label>
        <input type="number" required="true" min="1" v-model="goal_amount"/>
        <button type="submit">Create</button>
    </form>
</template>

<script>
export default {
    name: "GoalCreateMenu",

    data() {
        return {
            title: "",
            description: "",
            goal_amount: "",
        }
    },

    methods: {
        onSubmit() {
        },
    }
}
</script>