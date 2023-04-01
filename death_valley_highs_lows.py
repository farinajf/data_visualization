import csv
import matplotlib.pyplot as plot
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        d = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            h = int(row[4])
            l = int(row[5])
        except ValueError:
            print(f"Missing data for {d}!!")
        else:
            dates.append(d)
            highs.append(h)
            lows.append(l)

plot.style.use('seaborn-darkgrid')
fig, ax = plot.subplots()

ax.plot(dates, highs, c='red',  alpha=0.5)
ax.plot(dates, lows,  c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title ("Daily high and low temperatures - 2018\nDeath Valley, CA", fontsize=20)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

fig.autofmt_xdate()

plot.show()
