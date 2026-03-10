import matplotlib.pyplot as plt
xx = []
yy = []
yy2 = []

with open('/home/dein/VASP_dein/md-part1/MD/energy_list2.dat', 'r') as toten:
    lines = toten.readlines()

count =len(lines)
print("count is" ,count)

for i in range(2,count):
    lines[i] = lines[i].split()
    print(lines[i])
    xx.append(int(lines[i][0]))
    yy.append(float(lines[i][1]))
    yy2.append(float(lines[i][2]))

print(xx)
print(yy)
print(yy2)

plt.figure(figsize=(6,4))
plt.plot(xx, yy, label="total energy")
#plt.plot(xx, yy2, label="ion-Electron")
plt.xlabel("Step")
plt.ylabel("Energy(eV)")
#plt.axis([0.0,30.0,-0.323,-0.322])
plt.title("energy change during MD simulation")
plt.legend()
plt.grid()
#plt.savefig("plot_energy.png")
plt.show() 