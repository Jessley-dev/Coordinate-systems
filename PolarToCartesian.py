import numpy as np
print("===POLAR COORDINATES TO CARTESIAN COORDINATES===")
r = float(input("Enter the radius: "))
theta_deg = float(input("Enter the theta angle: "))
theta_rad = np.radians(theta_deg)
x = np.cos(theta_rad) * r
y = np.sin(theta_rad) * r
print(f"The cartesian coordinates are ({x:.3}, {y:.3})")