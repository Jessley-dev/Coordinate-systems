import numpy as np
print("CARTESIAN COORDINATES TO CYLINDRICAL COORDINATES")
try:
    x = float(input("Input the x component: "))
    y = float(input("Input the y component: "))
    z = float(input("Input the z component if you have one if not input 0: "))

    rho = np.sqrt(x**2 + y**2)
    phi = np.degrees(np.arctan2(y, x))
    print(f"The cylindrical coordinates are ({rho}, {phi}, {z})")

except ValueError:
    print("Please enter real numbers")