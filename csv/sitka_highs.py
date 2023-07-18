import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/san_francisco.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    headers = enumerate(header_row)

    high_row = header_row.index('TMAX')
    low_row = header_row.index('TMIN')

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[high_row])  # Temperature (Celsius) is the 6
            low = int(row[low_row])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs,  c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Daily high and low temperatures - 2018\nSan Francisco", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(0, 150)

plt.savefig('san_francisco.png', bbox_inches='tight')

plt.show()
