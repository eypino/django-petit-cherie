function initMap(){
    const petit = {lat:-41.470225083332004, lng:-72.92581729632133};
    const map = new google.maps.Map(document.getElementById("map"),{
        zoom : 15,
        center : petit,
    });
    const marker = new google.maps.Marker({
        position: petit,
        map : map,
    });
}

window.initMap = initMap;
