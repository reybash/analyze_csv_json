import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, precipitations = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            precipitation = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            precipitations.append(precipitation)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precipitations,  c='blue', alpha=0.5)

plt.title("Daily precipitations", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitations", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
