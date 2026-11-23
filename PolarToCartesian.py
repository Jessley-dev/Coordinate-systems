import numpy as np
print("===POLAR COORDINATES TO CARTESIAN COORDINATES===")
<<<<<<< HEAD
try:
    r = float(input("Enter the radius: "))
    theta_deg = float(input("Enter the theta angle: "))
    theta_rad = np.radians(theta_deg)
    x = np.cos(theta_rad) * r
    y = np.sin(theta_rad) * r
    print(f"The cartesian coordinates are ({x:.3f}, {y:.3f})")

except ValueError:
    print("Enter real numbers")
=======
r = float(input("Enter the radius: "))
theta_deg = float(input("Enter the theta angle: "))
theta_rad = np.radians(theta_deg)
x = np.cos(theta_rad) * r
y = np.sin(theta_rad) * r
print(f"The cartesian coordinates are ({x:.3}, {y:.3})")
>>>>>>> 2c7a5a6597ccc3af16ac60289e7a5b634bb52f74
