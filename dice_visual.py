from plotly.graph_objs import Bar, Layout
from plotly            import offline

from die import Die

die1 = Die()
die2 = Die()

results = []
for roll_num in range(100_000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides
for v in range(2, max_result + 1):
    frequency = results.count(v)
    frequencies.append(frequency)


x_values = list(range(2, max_result + 1))
data     = [Bar(x=x_values, y = frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frecuency of Result'}

my_layout = Layout(title='Results of rolling two D6 dice 100.000 times', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
