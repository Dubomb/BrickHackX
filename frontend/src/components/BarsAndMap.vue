<template>
    <div class="container">
      <div class="sidebar-left">
        <ul>
            <li v-for="(location, index) in locations" :key="index">{{ location.building }}</li>
            
         </ul>
      </div>
      <div class="content">
        <p1>Map View</p1>
        <div class="content-inner">
          <p1>Map goes here</p1>
        </div>
      </div>
      <div class="sidebar-right">
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'BarsAndMap',
    data() {
    return {
        locations: [
        {id: "1", descShort: "Between restrooms outside Gracie's", building: "Grace Watson Hall"},
        {id: "2", descShort: "Near west end bathrooms", building: "Campus Center"},
        {id: "3", descShort: "Near elevator on first floor at north end of building", building: "Student Life Center"},
        {id: "4", descShort: "Near restrooms on A-level at north end of building", building: "Student Life Center"},
        {id: "5", descShort: "Between restrooms on second floor above Slaughter Hall main entrance", building: "Student Life Center"},
        {id: "6", descShort: "In a hallway on eastern end of building", building: "Ornamental Horticulture Building"},
        {id: "7", descShort: "Near restrooms on first floor near east entrance", building: "Golisano Hall"},
        {id: "8", descShort: "Near elevator on first floor", building: "Building 6"},
        {id: "9", descShort: "In color science lab hallway leading towards Ross building", building: "James E. Booth Hall"},
        {id: "10", descShort: "Near restrooms on first floor", building: "Institute Hall"},
        {id: "11", descShort: "Near first floor restrooms", building: "Engineering Technology Services"},
        {id: "12", descShort: "Near 2nd floor break room", building: "Susanne G. Whittaker Library"},
        {id: "13", descShort: "Wiedman fitness center main entrance", building: "Gordon Field House"},
        {id: "14", descShort: "Next to women's accessible restroom", building: "Gordon Field House"},
        {id: "15", descShort: "Near entrance to honors program", building: "Grace Watson Hall"},
        {id: "16", descShort: "On east end of building lobby", building: "College of Business"},
        {id: "17", descShort: "Next to women's bathroom on south side of 1st floor", building: "Campus Center"},
        {id: "18", descShort: "Next to elevator on second floor", building: "August Center"},
        {id: "19", descShort: "Between gyms on top floor", building: "Hale-Andrews Student Life Center"},
        {id: "20", descShort: "Near equipment cage on A level", building: "Hale-Andrews Student Life Center"},
        {id: "21", descShort: "Next to reception desk at north entrance", building: "Gordon Field House"},
        {id: "22", descShort: "Next to \"home women\" locker room ", building: "Gordon Field House"},
        {id: "23", descShort: "Upper floor on east wall, across from trainer desk", building: "Gordon Field House"},
        {id: "24", descShort: "Campus center main lobby behind stairs", building: "Campus Center"},
        {id: "25", descShort: "Inside entrance from quarter mile", building: "Clark Gymnasium"},
        {id: "26", descShort: "Next to Ritter ice rink entrance from lobby", building: "Frank Ritter Ice Arena"},
        {id: "27", descShort: "4th floor near north end staircase ", building: "Eastman Hall"},
        {id: "28", descShort: "Right side of large column labeled 'RIT Libraries' in main lobby", building: "Wallace Library"},
        {id: "29", descShort: "Bottom floor near staircase", building: "Wallace Library"},
        {id: "30", descShort: "2nd floor near elevator", building: "Building 9"},
        {id: "31", descShort: "Near restrooms on first floor", building: "University Services Center"}
      ]
    };
    }
}
  </script>
  
  <style scoped>
  .container {
    display: flex;
    height: 100vh;
    padding: 20px;
  }
  
  .sidebar-left,
  .sidebar-right {
    width: 200px;
    background-color: #f0f0f0;
    padding: 30px;
  }
  
  .content {
    flex: 1;
    padding: 20px;
  }
  
  .content-inner {
    background-color: #fff;
    padding: 20px;
  }
  </style>
  