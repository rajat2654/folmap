import folium
import pandas

mapp = folium.Map(location=[38, -99], zoom_start=5)
fg = folium.FeatureGroup(name="MYMAP")
dd = pandas.read_csv("Volcanoes.txt")
s1 = list(dd["LAT"])
s2 = list(dd["LON"])
el = list(dd["ELEV"])

html = """<h4>Volcano info</h4>
Height = %s m
"""

for i in range(len(dd)):
    ifr = folium.IFrame(html=html %str(el[i]), height=100, width=200)
    fg.add_child(folium.Marker(location=[s1[i], s2[i]], popup=folium.Popup(ifr), icon=folium.Icon(color="blue")))

mapp.add_child(fg)

mapp.save("map_simple_html.html")