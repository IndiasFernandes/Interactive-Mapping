import folium
import pandas

data=pandas.read_csv("data/Eco-Villages.csv")
lat=list(data["LAT"])
lon=list(data["LON"])
nam=list(data["NAME"])
typ=list(data["TYPE"])
web=list(data["WEBSITE"])

def color_producer(type):
    if type == "Music":
        return 'red'
    else:
        return 'green'

def icon_producer(type):
    if type == "Music":
        return 'glyphicon glyphicon-music'
    else:
        return 'glyphicon glyphicon-leaf'

html = """<h4>Eco-Village Information:</h4>
Name: %s</br>
Type: %s</br>
<a href="%s" target="_blank">Visit their Website!</a><br>
"""
# Create Map Layer
map = folium.Map(location=[38.7633800035172, -9.166040024331778], zoom_start=6, tiles="Stamen Terrain")

# Create Feature Group Layer
fg_ev = folium.FeatureGroup(name="Eco Vilas")



# Create Child
for lt, ln, nm, wb, tp in zip(lat, lon, nam, web, typ):
    iframe = folium.IFrame(html=html % (str(nm),tp, wb), width=200, height=100)
    fg_ev.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_producer(tp), icon=icon_producer(tp))))

# Create Feature Group Layer
fg = folium.FeatureGroup(name="Countries")

fg.add_child(folium.GeoJson(data=open("data/world.json", "r", encoding="utf-8-sig").read(),
 style_function=lambda x:{'fillColor':'green' if x['properties']['NAME'] == 'Portugal' else 'red'}))

map.add_child(fg)
map.add_child(fg_ev)
map.add_child(folium.LayerControl())

map.save("Map.html")
