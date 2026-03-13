import numpy as np
import matplotlib.pyplot as plt

xx = []
yy = []

with open('/home/dein/github_repo/VASP_reproducing/MD_part1/Monitoring_molecular_geometry/monitored_cell_volume.dat', 'r') as f:
    lines = f.readlines()
count = len(lines)
print("count is", count)


for i in range(0,count):
    lines[i] = lines[i].split()
#    print(lines[i])
    xx.append(i+1)
    yy.append(float(lines[i][2]))

#print(xx)
#print(yy)

plt.figure(figsize=(6,4))
plt.plot(xx, yy, '-o', label="cell volume")
plt.xlabel("Number of MD Steps")
plt.ylabel("Volume (Angstrom^3)")
plt.title("Monitoring Cell Volume During MD Simulation")
plt.legend()
plt.savefig("cell_volume.png")
#plt.show()
