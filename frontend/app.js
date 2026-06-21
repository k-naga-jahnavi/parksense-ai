const API = "http://127.0.0.1:5000";

let map = null;
let chart = null;


// ---------- API ----------

async function fetchAPI(route){

try{

const res =
await fetch(`${API}/${route}`);

if(!res.ok){

throw new Error()

}

return await res.json()

}

catch(e){

console.log(e)

return []

}

}


// ---------- SUMMARY ----------

async function loadSummary(){

const d =
await fetchAPI("summary")

if(!d.length)
return

document.getElementById("total").textContent =
d[0].total_records || 0

document.getElementById("stations").textContent =
d[0].police_stations || 0

document.getElementById("junctions").textContent =
d[0].junctions || 0

document.getElementById("vehicles").textContent =
d[0].vehicle_types || 0

}


// ---------- TABLE ----------

function updateTable(rows){

const tbody =
document.getElementById("tbody")

tbody.innerHTML=""

rows.forEach(r=>{

tbody.innerHTML+=`

<tr>

<td>

${r.junction_name||
r.vehicle_type||
r.violation_type||
"-"}

</td>

<td>

${r.violations||
r.total||
r.count||
0}

</td>

<td>

${r.latitude||
"-"}

</td>

<td>

${r.longitude||
"-"}

</td>

</tr>

`

})

}


// ---------- CHART ----------

function drawChart(labels,values,title){

const canvas =
document.getElementById("chart")

if(chart){

chart.destroy()

}

chart =
new Chart(

canvas,

{

type:"bar",

data:{

labels,

datasets:[{

label:title,

data:values,

backgroundColor:

"rgba(56,189,248,.8)"

}]

},

options:{

responsive:true,

maintainAspectRatio:false

}

}

)

}


// ---------- HOTSPOTS ----------

async function hotspots(){

const d =
await fetchAPI("hotspots")

updateTable(d)

drawChart(

d.map(
x=>x.junction_name
),

d.map(
x=>x.violations
),

"Parking Hotspots"

)

}


// ---------- VEHICLES ----------

async function vehicles(){

const d =
await fetchAPI("vehicles")

updateTable(d)

drawChart(

d.map(
x=>x.vehicle_type
),

d.map(
x=>x.total
),

"Vehicle Analytics"

)

}


// ---------- VIOLATIONS ----------

async function violations(){

const d =
await fetchAPI("violations")

updateTable(d)

drawChart(

d.map(
x=>x.violation_type
),

d.map(
x=>x.total
),

"Violation Analytics"

)

}


// ---------- MAP ----------

async function loadMap(){

const geo =
await fetchAPI("geo")

const box =
document.getElementById("map")

if(!box)
return

if(map){

map.remove()

}

map =
L.map("map")

map.setView(

[12.9716,77.5946],

11

)

L.tileLayer(

"https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",

{

maxZoom:18

}

)

.addTo(map)


geo
.slice(0,250)
.forEach(

x=>{

if(

x.latitude &&
x.longitude

){

L.circleMarker(

[

parseFloat(x.latitude),

parseFloat(x.longitude)

],

{

radius:8,

color:"#ff4d6d",

fillOpacity:.7

}

)

.addTo(map)

}

}

)

setTimeout(

()=>{

map.invalidateSize()

},

500

)

}


// ---------- INIT ----------

async function init(){

await loadSummary()

await hotspots()

await loadMap()

}


// ---------- BUTTONS ----------

document
.getElementById(
"hotspotBtn"
)
.addEventListener(
"click",
hotspots
)

document
.getElementById(
"vehicleBtn"
)
.addEventListener(
"click",
vehicles
)

document
.getElementById(
"violationBtn"
)
.addEventListener(
"click",
violations
)

window.onload =
init