import matplotlib.pyplot as plt
import numpy as np

# 生成数据
x = np.linspace(-10, 10, 100)
y = x**2-2*x+1

# 绘制图形
plt.plot(x, y)
plt.ylim(-80,80)
plt.xlim(-10,10)

# 计算导数
dx = x[1] - x[0]
dydx = np.gradient(y, dx)

# 将导数绘制成一条红色的线
plt.plot(x, dydx, 'r')

# 显示图形
plt.show()
