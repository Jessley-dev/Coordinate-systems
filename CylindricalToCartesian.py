import numpy as np
print("===CYLINDRICAL COORDINATES TO CARTESIAN COORDINATES===")
try:    
    rho = float(input("Input the rho(ρ): "))
    phi_deg = float(input("Input the phi(φ): "))
    z = float(input("Input the z component: "))
    phi_rad = np.radians(phi_deg)
    x = np.cos(phi_rad)* rho
    y = np.sin(phi_rad)* rho

    print(f"The cartesian coordinates in 2D are ({x:.3f},{y:.3f}) "
        f" and in 3D are ({x:.3f},{y:.3f},{z:.3f})")
except ValueError:
    print("Please input real numbers")