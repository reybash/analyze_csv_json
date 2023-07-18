import csv
from datetime import datetime

from plotly.graph_objs import Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename, encoding="utf8") as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, lons, lats, tracks, frps = [], [], [], [], []

    lons_row = header_row.index('longitude')
    lats_row = header_row.index('latitude')
    dates_row = header_row.index('acq_date')
    track_row = header_row.index('track')
    frp_row = header_row.index('frp')

    for row in reader:
        current_date = datetime.strptime(row[dates_row], "%Y-%m-%d")
        try:
            lon = float(row[lons_row])
            lat = float(row[lats_row])
            track = float(row[track_row])
            frp = float(row[track_row])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            lons.append(lon)
            lats.append(lat)
            tracks.append(track)
            frps.append(frp)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': dates,
    'marker': {
        'size': [5*track for track in tracks],
        'color': frps,
        'colorscale': 'Hot',
        'reversescale': True,
        'colorbar': {'title': 'Track'}
    },
}]

print(lons[:5])
print(lats[:5])
print(dates[:5])

my_layout = Layout(title='Global Fires')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')
