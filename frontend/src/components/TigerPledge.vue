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

      <div class="goal-display-container">
        <div v-for="goal in filteredGoals" :key="goal.id">
          <GoalCard @onChangeGoal="updateGoal" :goal="goal" :progress="goal.progress"></GoalCard>
        </div>
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

      async updateGoal(id, start, current, goal) {
        let i;
        for (i = 0; i < this.goals.length; i++) {
          if (this.goals[i].id == id) {
            this.goals[i].start_amount = start;
            this.goals[i].current_amount = current;
            this.goals[i].goal_amount = goal;
            break;
          }
        }

        console.log(this.goals[i]);

        const response = await fetch("http://localhost:8000/api/goals/", {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(this.goals[i]),
        });

        if (!response.ok) {
          console.log("Goal update failed");
        }

      }
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
    padding: 20px;
}
.TigerPledge p {
  font-size: 20px;
  width: 50%;
  margin: auto;
}

.button-container {
  font-size: 25px;
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
}
.food-button {
    background-color: #ED874C;
}
.recycling-button {
  background-color: #279D41;
}

.food-button,
.water-button,
.recycling-button {
  color: #fff;
  border: none;
  padding: 15px;
  margin-right: 30px;
  cursor: pointer;
  border-radius: 12px;
  white-space: nowrap;
  overflow: hidden;
  text-align: center;
  width: 300px;
}

.water-button:hover,
.food-button:hover,
.recycling-button:hover {
  background-color: #3D5A80;
  transition: background-color 1s;
}

.box-container {
  display: flex;
  justify-content: center;
}

.box {
  background-color: #f0f0f0;
  width: 80%;
  padding: 30px;
  margin-top: 48px;
  border-radius: 10px;
}
@media screen and (max-width: 900px) {
  .button-container {
    flex-direction: column;
    align-items: center;
  }

  .water-button,
  .food-button,
  .recycling-button {
    margin: 5px 0;
  }
}
</style>
