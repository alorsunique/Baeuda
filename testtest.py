# Function defining the differential equation
def f(t, y):
    return t**3 * np.exp(-2*t) - 2*y

import numpy as np

# Initial conditions
t0 = 0
y0 = 1 + 12/50
h = 0.1
n = int(1/h)  # Number of steps

# Arrays to store the values of t and y
t_values = np.arange(t0, t0 + (n+1)*h, h)
y_values = np.zeros(n+1)
y_values[0] = y0

# Runge-Kutta 4th order method
for i in range(n):
    t = t_values[i]
    y = y_values[i]
    
    k1 = h * f(t, y)
    k2 = h * f(t + h/2, y + k1/2)
    k3 = h * f(t + h/2, y + k2/2)
    k4 = h * f(t + h, y + k3)
    
    y_values[i+1] = y + (k1 + 2*k2 + 2*k3 + k4) / 6

# Output the final value of y at t=1 to 9 decimal places and the table of values
y_at_1 = y_values[-1]
y_at_1, t_values, y_values


print(f"Y at 1: {y_at_1}")

for i in range(n):
    print(f"Iteration {i} | t-Value: {format(t_values[i], f'.{1}f')} | y-Value: {format(y_values[i], f'.{9}f')}")

print(f"Iteration 10 | t-Value: {1.0} | y-Value: {format(y_values[i], f'.{9}f')}")

print(f"Y at 1: {y_at_1}")

for i in range(n):
    print(f"Iteration {i} | t-Value: {format(t_values[i], f'.{1}f')} | y-Value: {format(y_values[i], f'.{9}f')}")

print(f"Iteration 10 | t-Value: {1.0} | y-Value: {format(y_values[i], f'.{9}f')}")