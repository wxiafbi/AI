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

# 生成数据
x = timestamps
y = values

# 绘制图形
fig, ax = plt.subplots()
ax.set_xlim(timestamps[0], timestamps[-1])
ax.set_ylim(40, 60)
plt.ion()

# 动态绘制点
for i in range(len(timestamps)):
    # 绘制点
    ax.plot(x[i], y[i], 'bo')
    # 更新图像
    plt.draw()
    plt.pause(0.05)
    # plt.flush_events()

# 显示图形
plt.ioff()
plt.show()
