import numpy as np
try:
    print("===SPHERICAL COORDINATES TO CARTESIAN COORDINATES===")
    r = float(input("Input the radius: "))
    theta_deg = float(input("Input the theta angle: "))
    phi_deg = float(input("Input the phi angle: "))
    theta_rad = np.radians(theta_deg)
    phi_rad = np.radians(phi_deg)

    x = np.sin(phi_rad) * np.cos(theta_rad) * r
    y = np.sin(phi_rad) * np.sin(theta_rad) * r
    z = np.cos(phi_rad) * r

    print(f"The cartesian coordinates are ({x:.3f}, {y:.3f}, {z:.3f})")

except ValueError:
    print("Input valid input")