import numpy as num
import matplotlib.pyplot as p

# array creation this is the size of the 2 arrays we use
x = num.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = num.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

# calculating the mean using the two arrays
mean_x = num.mean(x)
mean_y = num.mean(y)

# calculating the numerator and denomanator
n = num.sum((x-mean_x)*(y-mean_y))
d = num.sum(pow((x-mean_x), 2))

slope = n/d

intercept = mean_y -(slope*mean_x)

# this is the output to show you the slope and intercept
print("slope", slope)
print("intercept", intercept)

val = (slope*x) + intercept

# this is the actual plot and uses the lbrary matplotlib
p.plot(x, y)
p.plot(x, val)
p.show()
