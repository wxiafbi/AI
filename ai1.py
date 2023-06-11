import openpyxl as op
import datetime
import matplotlib.pyplot as plt
import numpy as np


data = op.load_workbook('历史数据.xlsx')
print(data)
sheet1 = data.worksheets[0]
print(sheet1)
# T=sheet1[0]
timestamps = []
values = []
for row in sheet1.iter_rows(min_row=2, values_only=True):
    timestamp = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
    value = float(row[1])
    timestamps.append(timestamp.timestamp())
    values.append(value)

print(timestamps)


fg, ax = plt.subplots()
line, = ax.plot([], [])


ax2 = ax.twinx()
line1, = ax2.plot([], [], 'r')
xx = []
# for t in range(len(timestamps)):

# tx = timestamps[t+1]-timestamps[t]
tx = timestamps[1]-timestamps[0]
xx.append(tx)
dy = np.gradient(values, xx[0])

ax.set_ylim(48, 55)
ax2.set_ylim(-0.25, 0.25)
ax.set_xlim(timestamps[0], timestamps[-1])
for i in range(len(timestamps)):

    line.set_data(timestamps[:i+1], values[:i+1])
    line1.set_data(timestamps[:i+1], dy[:i+1])
    plt.draw()
    plt.pause(0.05)
# plt.plot(timestamps, values)

print(dy)
# plt.plot(timestamps, dy, 'r')
# plt.draw()
plt.show()
