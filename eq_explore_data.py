import json

filename = 'data/eq_data_1_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags = []
for e in all_eq_dicts:
    mag = e['properties']['mag']
    mags.append(mag)

print(mags[:10])
