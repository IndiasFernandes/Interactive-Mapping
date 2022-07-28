import folium
import pandas

data=pandas.read_csv("data/Eco-Villages.csv")
lat=list(data["LAT"])
lon=list(data["LON"])
nam=list(data["NAME"])

html = """<h4>Eco-Village Information:</h4>
Name: %s
"""

map = folium.Map(location=[38.7633800035172, -9.166040024331778], zoom_start=6, tiles="Stamen Terrain")

# Create Feature Group
fg = folium.FeatureGroup(name="Eco Vilas")

# Create Child
for lt, ln, nm in zip(lat, lon, nam):
    iframe = folium.IFrame(html=html % str(nm), width=200, height=100)
    map.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map.html")
