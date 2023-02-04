import matplotlib.pyplot as plot

input_values = [1, 2, 3,  4,  5]
squares      = [1, 4, 9, 16, 25]

#plot.style.use('Solarize_Light2')
#plot.style.use('_classic_test_patch')
#plot.style.use('bmh')
#plot.style.use('classic')
#plot.style.use('dark_background')
#plot.style.use('fast')
#plot.style.use('fivethirtyeight')
#plot.style.use('ggplot')
#plot.style.use('grayscale')
#plot.style.use('seaborn')             +
#plot.style.use('seaborn-bright')
#plot.style.use('seaborn-colorblind')
#plot.style.use('seaborn-dark')
#plot.style.use('seaborn-dark-palette')
plot.style.use('seaborn-darkgrid')
#plot.style.use('seaborn-deep')
#plot.style.use('seaborn-muted')
#plot.style.use('seaborn-notebook')
#plot.style.use('seaborn-paper')
#plot.style.use('seaborn-pastel')
#plot.style.use('seaborn-poster')
#plot.style.use('seaborn-talk')
#plot.style.use('seaborn-ticks')
#plot.style.use('seaborn-white')
#plot.style.use('seaborn-whitegrid')
#plot.style.use('tableau-colorblind10')

fig, ax = plot.subplots()
ax.plot(input_values, squares, linewidth=3)

ax.set_title("Números al cuadrado", fontsize=24)
ax.set_xlabel("Número",             fontsize=14)
ax.set_ylabel("Cuadrado",           fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plot.show()
