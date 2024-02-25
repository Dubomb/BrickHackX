<template>
    <div class="container">
      <div class="sidebar-left">
        <div class="location-cards">
            <BuildingNameCard v-for="(location, index) in locationSet" :key="index" :location="location" @building-clicked="handleBuildingClicked"/>
        </div>
      </div>
      <div class="content">
        <p1>Map View</p1>
        <div class="content-inner">
          <p1>Map goes here</p1>
        </div>
      </div>
      <div class="sidebar-right">
        <div class="location-cards">
            <BuildingCard v-for="(location, index) in matchLocations" :key="index" :location="location"/>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import BuildingCard from './BuildingCard.vue';
  import BuildingNameCard from './BuildingNameCard.vue';

  export default {
    name: 'BarsAndMap',
    components: {
        BuildingCard,
        BuildingNameCard
    },
    methods: {
        handleBuildingClicked(buildingName) {
            // Do something with the emitted data (buildingName)
    
            this.matchLocations = []
            this.locations.forEach(loc => {
                if (loc.building == buildingName) {
                    this.matchLocations.push(loc);
                }
            });
        }
    },
    data() {
    return {
        matchLocations: [],
        locations: [
  {id: "1", descShort: "Between restrooms outside Gracie's", building: "Grace Watson Hall", abbreviation: "GWH"},
  {id: "2", descShort: "Near west end bathrooms", building: "Campus Center", abbreviation: "CRS"},
  {id: "3", descShort: "Near elevator on first floor at north end of building", building: "Student Life Center", abbreviation: "SLA"},
  {id: "4", descShort: "Near restrooms on A-level at north end of building", building: "Student Life Center", abbreviation: "SLA"},
  {id: "5", descShort: "Between restrooms on second floor above Slaughter Hall main entrance", building: "Student Life Center", abbreviation: "SLA"},
  {id: "6", descShort: "In a hallway on eastern end of building", building: "Ornamental Horticulture Building", abbreviation: "ORN"},
  {id: "7", descShort: "Near restrooms on first floor near east entrance", building: "Golisano Hall", abbreviation: "GLE"},
  {id: "8", descShort: "Near elevator on first floor", building: "Building 6", abbreviation: "LOW"},
  {id: "9", descShort: "In color science lab hallway leading towards Ross building", building: "James E. Booth Hall", abbreviation: "COL"},
  {id: "10", descShort: "Near restrooms on first floor", building: "Institute Hall", abbreviation: "HLC"},
  {id: "11", descShort: "Near first floor restrooms", building: "Engineering Technology Services", abbreviation: "ENT"},
  {id: "12", descShort: "Near 2nd floor break room", building: "Susanne G. Whittaker Library", abbreviation: "SUS"},
  {id: "13", descShort: "Wiedman fitness center main entrance", building: "Gordon Field House", abbreviation: "GOR"},
  {id: "14", descShort: "Next to women's accessible restroom", building: "Gordon Field House", abbreviation: "GOR"},
  {id: "15", descShort: "Near entrance to honors program", building: "Grace Watson Hall", abbreviation: "GVP"},
  {id: "16", descShort: "On east end of building lobby", building: "College of Business", abbreviation: "CBT"},
  {id: "17", descShort: "Next to women's bathroom on south side of 1st floor", building: "Campus Center", abbreviation: "CAR"},
  {id: "18", descShort: "Next to elevator on second floor", building: "August Center", abbreviation: "AUG"},
  {id: "19", descShort: "Between gyms on top floor", building: "Hale-Andrews Student Life Center", abbreviation: "HAC"},
  {id: "20", descShort: "Near equipment cage on A level", building: "Hale-Andrews Student Life Center", abbreviation: "HAC"},
  {id: "21", descShort: "Next to reception desk at north entrance", building: "Gordon Field House", abbreviation: "GOR"},
  {id: "22", descShort: "Next to \"home women\" locker room ", building: "Gordon Field House", abbreviation: "GOR"},
  {id: "23", descShort: "Upper floor on east wall, across from trainer desk", building: "Gordon Field House", abbreviation: "GOR"},
  {id: "24", descShort: "Campus center main lobby behind stairs", building: "Campus Center", abbreviation: "CPC"},
  {id: "25", descShort: "Inside entrance from quarter mile", building: "Clark Gymnasium", abbreviation: "CLK"},
  {id: "26", descShort: "Next to Ritter ice rink entrance from lobby", building: "Frank Ritter Ice Arena", abbreviation: "RIA"},
  {id: "27", descShort: "4th floor near north end staircase ", building: "Eastman Hall", abbreviation: "EAS"},
  {id: "28", descShort: "Right side of large column labeled 'RIT Libraries' in main lobby", building: "Wallace Library", abbreviation: "WAL"},
  {id: "29", descShort: "Bottom floor near staircase", building: "Wallace Library", abbreviation: "WAL"},
  {id: "30", descShort: "2nd floor near elevator", building: "Building 9", abbreviation: "BLC"},
  {id: "31", descShort: "Near restrooms on first floor", building: "University Services Center", abbreviation: "USC"}
],
        locationSet: [
    {"id": 1, "building": "Clark Gymnasium"},
    {"id": 2, "building": "Wallace Library"},
    {"id": 3, "building": "James E. Booth Hall"},
    {"id": 4, "building": "Susanne G. Whittaker Library"},
    {"id": 5, "building": "Ornamental Horticulture Building"},
    {"id": 6, "building": "Building 9"},
    {"id": 7, "building": "Campus Center"},
    {"id": 8, "building": "Hale-Andrews Student Life Center"},
    {"id": 9, "building": "Golisano Hall"},
    {"id": 10, "building": "College of Business"},
    {"id": 11, "building": "Gordon Field House"},
    {"id": 12, "building": "Building 6"},
    {"id": 13, "building": "August Center"},
    {"id": 14, "building": "Eastman Hall"},
    {"id": 15, "building": "University Services Center"},
    {"id": 16, "building": "Frank Ritter Ice Arena"},
    {"id": 17, "building": "Institute Hall"},
    {"id": 18, "building": "Grace Watson Hall"},
    {"id": 19, "building": "Engineering Technology Services"},
    {"id": 20, "building": "Student Life Center"}
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
    width: 300px;
    background-color: #98C1D9;
    padding: 30px;
    border-radius: 20px;
    overflow: auto;
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
  