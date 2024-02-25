<template>
    <div class="form-container">
        <h3>Create a goal ⭐</h3>
        <form @submit.prevent="onSubmit" @submit="$emit('onCreateGoal', {'title': this.title, 'description': this.description, 'start_amount': 0, 'current_amount': 0, 'goal_amount': this.goal_amount})">
            <label>Title:</label>
            <input type="text" required="true" v-model="title"/>
            <label>Description:</label>
            <input type="text" required="true" v-model="description"/>
            <label>Goal amount:</label>
            <input type="number" required="true" min="1" v-model="goal_amount"/>
            <button type="submit" class="create-button">Create</button>
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
    color: white;
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    height: 120px;
    z-index: 999;
}

label {
    margin-left: 40px;
    margin-right: 10px;
}

button {
    margin-left: 20px;
}

form {
    margin-top: -10px;
    margin-bottom: -10px;
}

input {
    box-sizing: border-box;
    background-color: gainsboro;
    border: 2px solid gray;
    padding: 5px;
    border-radius: 4px;
}

.create-button {
    font-size: 12px;
    margin-top: 0px;
    font-family: "Mukta";
    border-radius: 8px;
}

.create-button:hover {
    background-color: #3D5A80;
    transition: background-color 1s;
}

#app {
  font-family: Mukta;
  margin-top: -10px;
}
/* cute google font */
.mukta-extralight {
  font-family: "Mukta", sans-serif;
  font-weight: 200;
  font-style: normal;
}

.mukta-light {
  font-family: "Mukta", sans-serif;
  font-weight: 300;
  font-style: normal;
}

.mukta-regular {
  font-family: "Mukta", sans-serif;
  font-weight: 400;
  font-style: normal;
}

.mukta-medium {
  font-family: "Mukta", sans-serif;
  font-weight: 500;
  font-style: normal;
}

.mukta-semibold {
  font-family: "Mukta", sans-serif;
  font-weight: 600;
  font-style: normal;
}

.mukta-bold {
  font-family: "Mukta", sans-serif;
  font-weight: 700;
  font-style: normal;
}

.mukta-extrabold {
  font-family: "Mukta", sans-serif;
  font-weight: 800;
  font-style: normal;
}
</style>