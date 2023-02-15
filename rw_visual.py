import matplotlib.pyplot as plot

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plot.style.use('classic')

fig, ax = plot.subplots()

ax.scatter(rw.x_values, rw.y_values, s=15)
plot.show()
