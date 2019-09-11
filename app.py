import folium
import pandas

map = folium.Map(location=[39, -100], zoom_start=5)

fg = folium.FeatureGroup(name="My Map")

# read from file

file = pandas.read_csv("Volcanoes.txt")
lat = file["LAT"]
lon = file["LON"]
name = file["NAME"]

for nme, lt, ln in zip(name, lat, lon):
    fg.add_child(folium.Marker(location=[
        lt, ln], popup=nme, icon=folium.Icon(color='red')))

map.add_child(fg)
map.save("index.html")
