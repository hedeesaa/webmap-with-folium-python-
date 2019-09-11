import folium
import pandas

map = folium.Map(location=[39, -100], zoom_start=5)

fg = folium.FeatureGroup(name="My Map")

# read from file
file = pandas.read_csv("Volcanoes.txt")
lat = file["LAT"]
lon = file["LON"]
name = file["NAME"]
elev = file["ELEV"]

html = """<h4> %s </h4>
Height: %s m
<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a>
"""

for nme, lt, ln, el in zip(name, lat, lon, elev):
    iframe = folium.IFrame(html=html % (
        nme, str(el), nme, "More information"), width=200, height=100)

    fg.add_child(folium.Marker(location=[
        lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='red')))

map.add_child(fg)
map.save("index.html")
