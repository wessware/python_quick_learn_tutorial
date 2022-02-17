
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
