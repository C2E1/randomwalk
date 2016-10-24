import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
currentstate = 1
currenttime = 1
ymax = 5
ymin = -5
ax.set_ylim(ymin, ymax)
ax.set_xlim(0, 10)
ax.set_xlabel('Time')
ax.set_ylabel('State')
ax.plot(currenttime, currentstate)
plt.pause(1.5)
while (currentstate != -100 or currentstate != 100):
    # Discrete Uniform Between 0 and 1
    r = np.random.random_integers(low=0, high=1)
    # Move Foward
    if r == 0:
        currentstate += 1
    # Move Backwards
    else:
        currentstate -= 1
    if currenttime >= 10:
        ax.set_xlim(0, currenttime + 1)
    if(currentstate >= ymax):
        ymax = currentstate + 1
        ax.set_ylim(ymin, ymax)
    if(currentstate <= ymin):
        ymin = currentstate - 1
        ax.set_ylim(ymin, ymax)
    ax.plot(currenttime, currentstate, marker='o', linestyle='None', c="lime", ms=4.0)
    currenttime += 1
    plt.pause(1.5)
print("Done")
