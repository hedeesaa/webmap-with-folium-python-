import folium

map = folium.Map(location=[39, -100], zoom_start=5)

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[
             38.2, -99.1], popup="Hi, I am a Marker", icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("index.html")
