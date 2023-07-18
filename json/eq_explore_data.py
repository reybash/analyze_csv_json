import json

from plotly.graph_objs import Layout
from plotly import offline

filename = 'data/latest_eq_data.json'
with open(filename, encoding="utf8") as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    },
}]

# Create a layout object for the figure and set some properties like title etc.
my_layout = Layout(title=all_eq_data['metadata']['title'])

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthqukes.html')

print(mags[:10])
print(lons[:5])
print(lats[:5])

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
