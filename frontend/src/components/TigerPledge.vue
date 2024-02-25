<template>
    <div class="TigerPledge">
      <h1>{{ msg }}</h1>
      <p>
        Welcome to your very own sustainability journal! Start your EcoRIT pledge today by setting 
        your own personal goals. Let's make our pledge to the planet a reality 🌎
      </p>

      <div class="button-container">
        <Cbutton class="water-button" @click="displayBox('water')">Water</Cbutton>
        <Cbutton class="food-button" @click="displayBox('food')">Food</Cbutton>
        <Cbutton class="recycling-button" @click="displayBox('recycle')">Recycling</Cbutton>
      </div>

      <div class="box-container" v-if="showBox">
        <div class="box">
      <div v-if="selectedBox === 'water'">
        Water sustainability tracker
      </div>
      <div v-else-if="selectedBox === 'food'">
        Food sustainability tracker
      </div>
      <div v-else-if="selectedBox === 'recycle'">
        Recycling sustainability tracker
      </div>

      <div v-for="goal in filteredGoals" :key="goal.id">
        <GoalCard :goal="goal" :progress="goal.progress"></GoalCard>
      </div>

    </div>
    </div>
    <GoalCreateMenu @onCreateGoal="createGoal"></GoalCreateMenu>
  </div>
</template>
  
<script>
import GoalCard from './GoalCard.vue';
import GoalCreateMenu from './GoalCreateMenu.vue';

//import {uniqueId} from 'lodash';

export default {
  name: 'TigerPledge',

  components: {
    GoalCard,
    GoalCreateMenu
  },

  props: {
    msg: String,
  },

  data() {
    return {
      showBox: false,
      selectedBox: '',
      goals: [],
      filteredGoals: [],
    };
  },

  methods: {
      displayBox(boxType) {
        this.selectedBox = boxType;
        this.showBox = true;

        this.filteredGoals = this.goals.filter((g) => g.category === this.selectedBox)
      },

      async getGoals() {
        const response = await fetch("http://localhost:8000/api/goals");
        
        const result = await response.json();

        this.goals = result.message;
      },

      async createGoal(goal) {
        goal.id = this.goals.length + 1;
        goal.category = this.selectedBox;

        const response = await fetch("http://localhost:8000/api/goals/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(goal),
        });

        if (!response.ok) {
          console.log("Goal creation failed.");
          return;
        }

        this.goals.push(goal);
        this.displayBox(this.selectedBox);
      },
  },

  async mounted() {
    this.selectedBox = 'water';
    await this.getGoals();
    this.displayBox(this.selectedBox);
  }
}
</script>

  <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.TigerPledge {
    text-align: center;
}

.button-container {
  text-align: center;
  margin-top: 48px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.water-button {
  background-color: #98C1D9;
  color: #fff;
  border: none;
  padding: 15px 150px;
  margin-right: 30px;
  cursor: pointer;
  border-radius: 12px;
}

.food-button {
  background-color: #ED874C;
  color: #fff;
  border: none;
  padding: 15px 150px;
  margin-right: 30px;
  cursor: pointer;
  border-radius: 12px;
}

.recycling-button {
  background-color: #279D41;
  color: #fff;
  border: none;
  padding: 15px 150px;
  margin-right: 30px;
  cursor: pointer;
  border-radius: 12px;
}

.water-button:hover {
  background-color: #3D5A80;
}

.food-button:hover {
  background-color: #3D5A80;
}

.recycling-button:hover {
  background-color: #3D5A80;
}

.box-container {
  display: flex;
  justify-content: center;
}

.box {
  background-color: #f0f0f0;
  width: 1180px;
  height: 350px;
  padding: 30px;
  margin-top: 48px;
  border-radius: 10px;
}
</style>
