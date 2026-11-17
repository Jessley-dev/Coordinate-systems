import numpy as np
print("===CARTESIAN COORDINATES TO POLAR COORDINATES===")
x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)
print(f"The polar coordinates are ({r:.3}, {theta:.3})")