import matplotlib.pyplot as plot

from random_walk import RandomWalk

while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plot.style.use('classic')

    fig, ax = plot.subplots(figsize=(15, 9), dpi=128)

    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plot.cm.Blues, edgecolors='none', s=1)

    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #Remove axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plot.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break