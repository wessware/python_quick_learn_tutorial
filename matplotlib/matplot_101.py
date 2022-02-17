
from matplotlib import dates as mdates
from datetime import datetime as dt
from shutil import which
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox


x_values = list(range(1000))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]

# line graphs
"""

x_values = [0, 1, 2, 3, 4, 5]
squares = [0, 1, 4, 9, 16, 25]

plt.plot(x_values, squares)

plt.show()
"""

# scatter plots
"""
plt.scatter(x_values, squares, s=10)

plt.show()
"""

# plot labels
"""
# customized plots

plt.scatter(x_values, squares, s=10)

plt.title('Sqaured Values', fontsize=24)
plt.xlabel('Value', fontsize=18)
plt.ylabel('Square of Values', fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])

plt.show()
"""

# customizing plots
"""

plt.scatter(x_values, squares, c=squares,
            cmap=plt.cm.Blues, edgecolors='none', s=10)
plt.title('Sqaured Values', fontsize=24)
plt.xlabel('Value', fontsize=18)
plt.ylabel('Square of Values', fontsize=18)

plt.show()
"""
# empasizing points on the plot- first value & last value(s)
"""

plt.scatter(x_values, squares, c=squares,
            cmap=plt.cm.Blues, edgecolors='none', s=10)
plt.scatter(x_values[0], squares[0], c='green', edgecolors='none', s=100)
plt.scatter(x_values[-1], squares[-1], c='red', edgecolors='none', s=100)

plt.title('Sqaured Values', fontsize=24)
plt.xlabel('Value', fontsize=18)
plt.ylabel('Square of Values', fontsize=18)

plt.show()
"""

# axes visibility
"""

plt.scatter(x_values, squares, c=squares,
            cmap=plt.cm.Blues, edgecolors='none', s=10)
plt.scatter(x_values[0], squares[0], c='green', edgecolors='none', s=100)
plt.scatter(x_values[-1], squares[-1], c='red', edgecolors='none', s=100)

plt.title('Sqaured Values', fontsize=24)
plt.xlabel('Value', fontsize=18)
plt.ylabel('Square of Values', fontsize=18)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()
"""
# setting a custom figure size
"""
plt.figure(dpi=128, figsize=(10, 6))
"""

# saving a plot
"""
plt.savefig('value_squares.png', bbox_inches='tight')
"""

# multiple plots
"""
plt.scatter(x_values, squares, c='blue', edgecolors='none', s=20)
plt.scatter(x_values, cubes, c='red', edgecolors='none', s=20)

plt.title('Sqaured Vs Cubed', fontsize=24)
plt.xlabel('Squares', fontsize=18)
plt.ylabel('Cubes', fontsize=18)

plt.axis([0, 11, 0, 1100])

#plt.savefig('x_values_vs_squares_matplotlib_plot7.png', bbox_inches='tight')

plt.show()
"""

# filling between plots
"""
plt.scatter(x_values, squares, c='blue', edgecolors='none', s=20)
plt.scatter(x_values, cubes, c='red', edgecolors='none', s=20)

plt.title('Sqaured Vs Cubed', fontsize=24)
plt.xlabel('Squares', fontsize=18)
plt.ylabel('Cubes', fontsize=18)

plt.axis([0, 11, 0, 1100])
plt.fill_between(x_values, cubes, squares, facecolor='blue', alpha=0.25)

plt.savefig('x_values_vs_squares_matplotlib_plot8.png', bbox_inches='tight')

plt.show()
"""
# temperature plots
"""
dates = [
    dt(2016, 6, 21), dt(2016, 6, 22), dt(2016, 6, 23), dt(2016, 6, 24)
]
highs = [57, 68, 64, 59]

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.title('Daily High Temperatures', fontsize=24)
plt.ylabel('Temp (F)', fontsize=16)

x_axis = plt.axes().get_xaxis()
x_axis.set_major_formatter(mdates.DateFormatter('%B %d %Y'))

fig.autofmt_xdate()

plt.savefig('x_values_vs_squares_matplotlib_plot9.png', bbox_inches='tight')

plt.show()
"""

# multiple plots in one figure
# x-axis
"""
x_values = list(range(11))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]

fig, axarr = plt.subplots(2, 1, sharex=True)

axarr[0].scatter(x_values, squares)
axarr[0].set_title('Squares')

axarr[1].scatter(x_values, cubes, c='red')
axarr[1].set_title('Cubes')

plt.savefig('x_values_vs_squares_matplotlib_plot10.png', bbox_inches='tight')

plt.show()
"""

# y-axis

fig, axarr = plt.subplots(1, 2, sharey=True)

axarr[0].scatter(x_values, squares)
axarr[0].set_title('Squares')

axarr[1].scatter(x_values, cubes, c='red')
axarr[1].set_title('Cubes')

plt.savefig('x_values_vs_squares_matplotlib_plot10.png', bbox_inches='tight')

plt.show()
