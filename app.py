import folium
import pandas


def color_height(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev < 3000:
        return 'orange'
    else:
        return 'red'


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

    fg.add_child(folium.CircleMarker(
        location=[lt, ln], radius=7, popup=folium.Popup(iframe), fill_color=color_height(el), color=color_height(el), fill_opacity=0.7))

fg.add_child(folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.save("index.html")
