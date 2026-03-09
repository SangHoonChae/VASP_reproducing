import matplotlib.pyplot as plt
xx = []
yy = []
yy2 = []

with open('/home/dein/VASP_dein/md-part1/MD/temperature_list.dat', 'r') as toten:
    lines = toten.readlines()



for i in range(2,32):
    lines[i] = lines[i].split()
    print(lines[i])
    xx.append(int(lines[i][0]))
    yy.append(float(lines[i][1]))
    yy2.append(float(lines[i][2]))

print(xx)
print(yy)
print(yy2)

plt.figure(figsize=(6,4))
plt.plot(xx, yy, label="temperature")
plt.plot(xx, yy2, label="kinetic energy")
plt.xlabel("Step")
plt.ylabel("Temperature(K)")
#plt.axis([0.0,30.0,-0.323,-0.322])
plt.title("EKIN, temperature")
plt.legend()
plt.grid()
#plt.savefig("energy_plot.png")
plt.show() 