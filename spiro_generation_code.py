import numpy as np
import matplotlib.pyplot as plt

# Given parameters
R = 90
r = 36
a = 44
center_long, center_lat = -118.28563, 34.02051  # Tommy Trojan's coordinates

n = 10 
t = np.arange(0, n * np.pi, 0.01)

x = (R + r) * np.cos((r / R) * t) - a * np.cos((1 + r / R) * t)
y = (R + r) * np.sin((r / R) * t) - a * np.sin((1 + r / R) * t)

x *= .0001
y *= .0001


spiro_long = y + center_long
spiro_lat = x + center_lat 

coordinate_data = ""

for lon, lat in zip(spiro_long, spiro_lat):
    coordinate_data += f"{lon},{lat},\n"

print(coordinate_data)
# coordinate_data is used to populate the <coordinates> field in the KML