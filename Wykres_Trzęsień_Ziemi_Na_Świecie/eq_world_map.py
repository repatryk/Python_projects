import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Analiza struktury danych
filename = 'data2/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

#Wyodrębnienie siły trzęsienia ziemi
all_eq_dicts = all_eq_data['features']
mags,lons,lats, hover_text = [],[],[],[]

for eq_dick in all_eq_dicts:
    mag = eq_dick['properties']['mag']
    lon = eq_dick['geometry']['coordinates'][0]
    lat = eq_dick['geometry']['coordinates'][1]



    title = eq_dick['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(title)

#Mapa trzęsień ziemi
data = [{

        'type': 'scattergeo',
        'lon':lons,
        'lat':lats,
        'text':hover_text,
        'marker': {
            'size' :[5*mag for mag in mags],
            'color' : mags,
            'colorscale' : 'Viridis',
            'reversescale' : True,
            'colorbar' : {'title' : 'Siła'},
        },


        }]

my_layouts = Layout(title = "Trzęsienia ziemi na świecie")

fig = {'data':data, 'layout':my_layouts}
offline.plot(fig,filename='global_earthquakes.html')