import './App.css'; 
import { load } from '@2gis/mapgl';


function App() {
  return (
    <div className="App">
      
      <div id="map-container"></div>
      
        
      
    </div>
  );
}

export default App;
load().then((mapglAPI) => {
  const map = new mapglAPI.Map('map-container', {
      center: [55.31878, 25.23584],
      zoom: 13,
      key: 'c89bc682-f895-406d-8f9b-80e3c712c18a',
      zoomControl: false,
       })
      })