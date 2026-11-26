import numpy as np
try:
    print("===CARTESIAN COORDINATES TO SPHERICAL COORDINATES===")
    print("Cartesian coordinates are written as (x, y, z)")
    x = float(input("Input the x component: "))
    y = float(input("Input the y component: "))
    z = float(input("Input the z component if none input 0: "))

    r = np.sqrt((x**2) + (y**2) +(z**2))
    theta_radians = np.atan2(y, x)
    phi_radians = np.acos(z/r)
    theta_degrees = np.degrees(theta_radians)
    phi_degrees = np.degrees(phi_radians)
    print(f"The spherical coordinates are: ({r:.3f}, {theta_degrees:.3f} degrees, {phi_degrees:.3f}degrees)")

except ValueError:
    print("Please input valid input")