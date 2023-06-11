import math
import matplotlib.pyplot as plt

# if __name__ == "__main__":
x = [float(i)/100.0 for i in range(1, 300)]
print(x)
y = [math.log(i) for i in x]
plt.plot(x, y, 'r-', linewidth=3, label='log Curve')
print(x[20])
print(x[175])
a = [x[20], x[175]]

b = [y[20], y[175]]
c = [1/i for i in x]
# C = math.log(x)
plt.plot(a, b, 'g-', linewidth=2)
plt.plot(a, b, 'b*', markersize=15, alpha=0.75)
plt.plot(1, 0, 'b*', markersize=5, alpha=0.75)

plt.plot(x, c)
plt.legend(loc='upper left')
plt.grid(True)
plt.xlabel('X')
plt.ylabel('log(x)')

plt.show()
