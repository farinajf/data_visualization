import json

filename = 'data/eq_data_1_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags = []
lons = []
lats = []
for e in all_eq_dicts:
    mag = e['properties']['mag']
    lon = e['geometry']['coordinates'][0]
    lat = e['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])
