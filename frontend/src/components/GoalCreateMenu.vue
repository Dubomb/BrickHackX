<template>
    <div class="form-container">
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
    </div>
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

<style scoped>
.form-container {
    background-color: #385A80;
    padding: 20px;
}

label {
    margin-left: 40px;
    margin-right: 10px;
}

button {
    margin-left: 20px;
}

input {
    box-sizing: border-box;
    background-color: gainsboro;
    border: 2px solid gray;
    padding: 10px;
    border-radius: 4px;
}
</style>