var map = L.map("map", {
  attributionControl : false
}).setView([41.311081, 69.240562], 13);

L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',{
    maxZoom: 18,
    subdomains:['mt0','mt1','mt2','mt3']
}).addTo(map);





