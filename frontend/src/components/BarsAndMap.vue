<template>
    <div class="container">
      <div class="sidebar-left">
        <h2 class="sidebarTitle" >📍 Location List</h2>
        <div class="location-cards">
            <BuildingNameCard v-for="(location, index) in locationSet" :key="index" :location="location" @building-clicked="handleBuildingClicked"/>
        </div>
      </div>
      <div class="content">
        <h2 class="sidebarTitle">🗺️ Find a Water Fountain </h2> 
        <div class="content-inner">
          <div id="map" class="map"></div>
        </div>
        <div class="fun-fact">
          <h2>Did you know?</h2>
          <h3>Reusable water bottles can save hundreds of plastic water bottles every year!</h3>
        </div>
      </div>
      <div class="sidebar-right">
        <h2 class="sidebarTitle">📍 Matched Locations</h2>
        <div class="location-cards">
            <BuildingCard v-for="(location, index) in matchLocations" :key="index" :location="location"/>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import mapboxgl from 'mapbox-gl';
  import BuildingCard from './BuildingCard.vue';
  import BuildingNameCard from './BuildingNameCard.vue';

  export default {
    name: 'BarsAndMap',
    components: {
        BuildingCard,
        BuildingNameCard
    },
    methods: {
        handleBuildingClicked(location) {
            // Do something with the emitted data (buildingName)
    
            this.matchLocations = []
            this.locations.forEach(loc => {
                if (loc.building == location.building) {
                    this.matchLocations.push(loc);
                    this.map.setCenter([location.longitude, location.latitude]);
                    this.map.setZoom(18);
                }
            });
        }
    },
    data() {
    return {
        matchLocations: [],
        locations: [
  {"id":"1","descShort":"Between restrooms outside Gracie's","building":"Grace Watson Hall","abbreviation":"GWH","starRating":4.2,"review":"Refreshing water fountain conveniently located near Gracie's.","buildingEmoji":"🏢"},
  {"id":"2","descShort":"Near west end bathrooms","building":"Crossroads","abbreviation":"CRS","starRating":3.8,"review":"Decent water fountain with good water pressure.","buildingEmoji":"🍽️"},
  {"id":"3","descShort":"Near elevator on first floor at north end of building","building":"Louise Slaughter Hall","abbreviation":"SLA","starRating":2.5,"review":"Water fountain needs maintenance, water flow is weak.","buildingEmoji":"🏢"},
  {"id":"4","descShort":"Near restrooms on A-level at north end of building","building":"Louise Slaughter Hall","abbreviation":"SLA","starRating":4.7,"review":"Excellent water fountain with cold and refreshing water.","buildingEmoji":"🏢"},
  {"id":"5","descShort":"Between restrooms on second floor above Slaughter Hall main entrance","building":"Louise Slaughter Hall","abbreviation":"SLA","starRating":3.9,"review":"Average water fountain, water temperature is inconsistent.","buildingEmoji":"🏢"},
  {"id":"6","descShort":"In a hallway on eastern end of building","building":"Orange Hall","abbreviation":"ORN","starRating":4.1,"review":"Reliable water fountain with filtered water.","buildingEmoji":"🏢"},
  {"id":"7","descShort":"Near restrooms on first floor near east entrance","building":"James E. Gleason Hall","abbreviation":"GLE","starRating":2.9,"review":"Water fountain is often out of order.","buildingEmoji":"🏢"},
  {"id":"8","descShort":"Near elevator on first floor","building":"Max Lowenthal Hall","abbreviation":"LOW","starRating":3.2,"review":"Water fountain is clean and well-maintained.","buildingEmoji":"🏢"},
  {"id":"9","descShort":"In color science lab hallway leading towards Ross building","building":"Munsell Color Science Laboratory","abbreviation":"COL","starRating":4.5,"review":"Great water fountain, always cold and refreshing water.","buildingEmoji":"🔬"},
  {"id":"10","descShort":"Near restrooms on first floor","building":"Hugh L. Carey Hall","abbreviation":"HLC","starRating":3.6,"review":"Water fountain is functional, but water taste could be improved.","buildingEmoji":"🏢"},
  {"id":"11","descShort":"Near first floor restrooms","building":"Engineering Technology Hall","abbreviation":"ENT","starRating":4.3,"review":"Clean and reliable water fountain.","buildingEmoji":"🏢"},
  {"id":"12","descShort":"Near 2nd floor break room","building":"Sustainability Institute Hall","abbreviation":"SUS","starRating":2.7,"review":"Water fountain needs repair, water flow is weak.","buildingEmoji":"🏢"},
  {"id":"13","descShort":"Wiedman fitness center main entrance","building":"Gordon Field House","abbreviation":"GOR","starRating":3.8,"review":"Decent water fountain, could be cleaner.","buildingEmoji":"🏋️"},
  {"id":"14","descShort":"Next to women's accessible restroom","building":"Gordon Field House","abbreviation":"GOR","starRating":4.0,"review":"Good water fountain, water temperature is just right.","buildingEmoji":"🏋️"},
  {"id":"15","descShort":"Near entrance to honors program","building":"Global Village Plaza","abbreviation":"GVP","starRating":4.9,"review":"Excellent water fountain, best on campus.","buildingEmoji":"🏢"},
  {"id":"16","descShort":"On east end of building lobby","building":"Center for Bioscience Education and Technology","abbreviation":"CBT","starRating":3.2,"review":"Average water fountain, could use maintenance.","buildingEmoji":"🏢"},
  {"id":"17","descShort":"Next to women's bathroom on south side of 1st floor","building":"Chester F. Carlson Center for Imaging Science","abbreviation":"CAR","starRating":4.6,"review":"High-quality water fountain, water tastes great.","buildingEmoji":"🏢"},
  {"id":"18","descShort":"Next to elevator on second floor","building":"August Center","abbreviation":"AUG","starRating":3.4,"review":"Decent water fountain, water temperature varies.","buildingEmoji":"🏢"},
  {"id":"19","descShort":"Between gyms on top floor","building":"Hale-Andrews Student Life Center","abbreviation":"HAC","starRating":4.1,"review":"Reliable water fountain, good water pressure.","buildingEmoji":"🏢"},
  {"id":"20","descShort":"Near equipment cage on A level","building":"Hale-Andrews Student Life Center","abbreviation":"HAC","starRating":2.8,"review":"Water fountain needs repair, water flow is weak.","buildingEmoji":"🏢"},
  {"id":"21","descShort":"Next to reception desk at north entrance","building":"Gordon Field House","abbreviation":"GOR","starRating":4.3,"review":"Great water fountain, always cold and refreshing water.","buildingEmoji":"🏋️"},
  {"id":"22","descShort":"Next to \"home women\" locker room ","building":"Gordon Field House","abbreviation":"GOR","starRating":3.9,"review":"Clean and reliable water fountain.","buildingEmoji":"🏋️"},
  {"id":"23","descShort":"Upper floor on east wall, across from trainer desk","building":"Gordon Field House","abbreviation":"GOR","starRating":3.1,"review":"Average water fountain, could be cleaner.","buildingEmoji":"🏋️"},
  {"id":"24","descShort":"Campus center main lobby behind stairs","building":"Campus Center","abbreviation":"CPC","starRating":4.7,"review":"Excellent water fountain, best in the Campus Center.","buildingEmoji":"🏢"},
  {"id":"25","descShort":"Inside entrance from quarter mile","building":"Clark Gymnasium","abbreviation":"CLK","starRating":4.4,"review":"Reliable water fountain, good water pressure.","buildingEmoji":"🏋️"},
  {"id":"26","descShort":"Next to Ritter ice rink entrance from lobby","building":"Frank Ritter Ice Arena","abbreviation":"RIA","starRating":3.5,"review":"Average water fountain, water temperature varies.","buildingEmoji":"🏒"},
  {"id":"27","descShort":"4th floor near north end staircase ","building":"Eastman Hall","abbreviation":"EAS","starRating":3.7,"review":"Decent water fountain, water flow is consistent.","buildingEmoji":"🏢"},
  {"id":"28","descShort":"Right side of large column labeled 'RIT Libraries' in main lobby","building":"Wallace Library","abbreviation":"WAL","starRating":4.8,"review":"Excellent water fountain, always cold and refreshing water.","buildingEmoji":"📚"},
  {"id":"29","descShort":"Bottom floor near staircase","building":"Wallace Library","abbreviation":"WAL","starRating":3.8,"review":"Decent water fountain, could use maintenance.","buildingEmoji":"📚"},
  {"id":"30","descShort":"2nd floor near elevator","building":"Bausch and Lomb Center","abbreviation":"BLC","starRating":4.6,"review":"High-quality water fountain, water tastes great.","buildingEmoji":"🏢"},
  {"id":"31","descShort":"Near restrooms on first floor","building":"University Services Center","abbreviation":"USC","starRating":4.3,"review":"Clean and reliable water fountain.","buildingEmoji":"🏢"}
]
,

        locationSet: [
    {"id": 1, "building": "Clark Gymnasium", "latitude": "43.08455", "longitude": "-77.67388", "buildingEmoji": "🏋️"},
    {"id": 2, "building": "Wallace Library", "latitude": "43.08392", "longitude": "-77.67637", "buildingEmoji": "📚"},
    {"id": 3, "building": "Munsell Color Science Laboratory", "latitude": "43.08247", "longitude": "-77.67834", "buildingEmoji": "🔬"},
    {"id": 4, "building": "Sustainability Institute Hall", "latitude": "43.08524", "longitude": "-77.68129", "buildingEmoji": "🏢"},
    {"id": 5, "building": "Orange Hall", "latitude": "43.08358", "longitude": "-77.67875", "buildingEmoji": "🏢"},
    {"id": 6, "building": "Bausch and Lomb Center", "latitude": "43.08600", "longitude": "-77.67537", "buildingEmoji": "🏢"},
    {"id": 7, "building": "Campus Center", "latitude": "43.08400", "longitude": "-77.67388", "buildingEmoji": "🏢"},
    {"id": 8, "building": "Hale-Andrews Student Life Center", "latitude": "43.08450", "longitude": "-77.67192", "buildingEmoji": "🏢"},
    {"id": 9, "building": "James E. Gleason Hall", "latitude": "43.08432", "longitude": "-77.67811", "buildingEmoji": "🏢"},
    {"id": 10, "building": "Center for Bioscience Education and Technology", "latitude": "43.08554", "longitude": "-77.67857", "buildingEmoji": "🏢"},
    {"id": 11, "building": "Gordon Field House", "latitude": "43.08506", "longitude": "-77.67175", "buildingEmoji": "🏋️"},
    {"id": 12, "building": "Max Lowenthal Hall", "latitude": "43.08289", "longitude": "-77.67714", "buildingEmoji": "🏢"},
    {"id": 13, "building": "August Center", "latitude": "43.08411", "longitude": "-77.67212", "buildingEmoji": "🏢"},
    {"id": 14, "building": "Eastman Hall", "latitude": "43.08468", "longitude": "-77.67546", "buildingEmoji": "🏢"},
    {"id": 15, "building": "University Services Center", "latitude": "43.08335", "longitude": "-77.68024", "buildingEmoji": "🏢"},
    {"id": 16, "building": "Frank Ritter Ice Arena", "latitude": "43.08528", "longitude": "-77.67385", "buildingEmoji": "🏒"},
    {"id": 17, "building": "Hugh L. Carey Hall", "latitude": "43.08258", "longitude": "-77.67886", "buildingEmoji": "🏢"},
    {"id": 18, "building": "Grace Watson Hall", "latitude": "43.08371", "longitude": "-77.66921", "buildingEmoji": "🏢"},
    {"id": 19, "building": "Engineering Technology Hall", "latitude": "43.08502", "longitude": "-77.68035", "buildingEmoji": "🏢"},
    {"id": 20, "building": "Louise Slaughter Hall", "latitude": "43.08490", "longitude": "-77.68226", "buildingEmoji": "🏢"},
    {"id": 21, "building": "Global Village Plaza", "latitude": "43.08291", "longitude": "-77.68078", "buildingEmoji": "🏢"},
    {"id": 22, "building": "Crossroads", "latitude": "43.08261", "longitude": "-77.68009", "buildingEmoji": "🍽️"},
    {"id": 23, "building": "Chester F. Carlson Center for Imaging Science", "latitude": "43.08585", "longitude": "-77.67768", "buildingEmoji": "🏢"}
],
  map: null


    };

    },
    mounted() {
      mapboxgl.accessToken = 'pk.eyJ1IjoiZWp0NzUwOCIsImEiOiJjbHQwcHoyOWoxM2RuMmlvNnZvanhnbXF5In0.F4jjYcRbTHTNPerkaPnNhQ';
      this.map = new mapboxgl.Map({
        container: 'map',
        center: [-77.67515, 43.08448],
        zoom: 14,
        attributionControl: false
      });
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
    width: 350px;
    background-color: #98C1D9;
    border-radius: 20px;
    overflow: auto;
    border: 5px solid #3D5A80; /* Add border style */
    padding: 20px; /* Add padding for spacing */
  }

  .sidebar-left::-webkit-scrollbar {
  width: 0; /* Make the scrollbar width 0 */
}

.sidebar-right::-webkit-scrollbar {
  width: 0; /* Make the scrollbar width 0 */
}
 
.sidebarTitle{
    font-size: 28px;
    color: #293241;
    border-bottom: 1px solid #293241; 
}
  
  .content {
    flex: 1;
    padding: 20px;
    text-align: center;
    color: #293241;
  }
  
  .content-inner {
    background-color: #fff;
    padding: 0px;
    width: 80%;
    height: 60vh;
    margin: auto;
    border: 5px solid #3D5A80;
    margin-bottom: 40px;
  }
  #map {
  width: 100%;
  height: 100%;
  } 
  .fun-fact h2 {
    margin-bottom: 10px;
  }
  .fun-fact h3 {
    margin-top: 0px;
  }
  .fun-fact {
    padding-left: 50px;
    padding-right: 50px;
  }
  
  </style>
  