import folium
import pandas

mapp = folium.Map(location=[38, -99], zoom_start=5)
fg = folium.FeatureGroup(name="MYMAP")
dd = pandas.read_csv("Volcanoes.txt")
s1 = list(dd["LAT"])
s2 = list(dd["LON"])
el = list(dd["ELEV"])

for i in range(len(dd)):
    fg.add_child(folium.Marker(location=[s1[i], s2[i]], popup="Elevation of this place : " + str(el[i]) + " m", icon=folium.Icon(color="blue")))

mapp.add_child(fg)

mapp.save("map.html")