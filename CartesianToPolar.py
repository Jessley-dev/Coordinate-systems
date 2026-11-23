import numpy as np
print("===CARTESIAN COORDINATES TO POLAR COORDINATES===")
<<<<<<< HEAD
try:
    x = float(input("Enter the x-coordinate: "))
    y = float(input("Enter the y-coordinate: "))

    r = np.sqrt(x**2 + y**2)
    theta = np.degrees(np.arctan2(y, x))
    print(f"The polar coordinates are ({r:.3f}, {theta:.3f})")

except ValueError:
    print("Please enter real numbers")
=======
x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)
print(f"The polar coordinates are ({r:.3}, {theta:.3})")
>>>>>>> 2c7a5a6597ccc3af16ac60289e7a5b634bb52f74
