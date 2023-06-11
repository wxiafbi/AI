import numpy as np
import matplotlib.pyplot as plt
import random

a = random.randint(1, 20)
b = []

for i in range(0, 20):
    b.append(i)
    print(i)

y = [i*i for i in b]

fg, ax = plt.subplots()

linge, = ax.plot([], [])
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ay = ax.twiny()
ay.set_xlim(-10,1)
for c in range(len(b)):
    linge.set_data(b[:c+1], y[:c+1])
    plt.draw()
    plt.pause(0.5)


plt.show()
