import matplotlib.pyplot as plt
from die import Die

# Create a D6
die = Die()

# Roll the dice!
for roll_number in range(1000):
    result = die.roll()

# Show results of rolling a 6-sided die 1000 times.
    x_values = list(range(1, 7))
    y_values = [x/6 + die.roll() for x in x_values]

plt.scatter(x_values, y_values, s=50)

# Set chart title and label axes.
plt.title("Results of rolling one D6 1000 times", fontsize=24)
plt.xlabel("Result", fontsize=14)
plt.ylabel("Frequency of Result", fontsize=14)

# Set the range for each axis.
plt.axis([0, 7, -10, 10])

plt.show()
