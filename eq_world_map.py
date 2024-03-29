from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

import json

# https://github.com/ehmatthes/pcc_2e/tree/master/chapter_16/mapping_global_data_sets/data

filename = 'data/eq_data_30_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags        = []
lons        = []
lats        = []
hover_texts = []
for e in all_eq_dicts:
    mag = e['properties']['mag']
    lon = e['geometry']['coordinates'][0]
    lat = e['geometry']['coordinates'][1]

    title = e['properties']['title']

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

data      = [Scattergeo(lon=lons, lat=lats)]
data      = [
{
 'type' : 'scattergeo',
 'lon'  : lons,
 'lat'  : lats,
 'text' : hover_texts,
 'marker' : {
    'size'        : [5*mag for mag in mags],
    'color'       : mags,
    'colorscale'  : 'Viridis',
    'reversescale': True,
    'colorbar'    : {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
