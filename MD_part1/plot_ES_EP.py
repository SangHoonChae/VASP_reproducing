import matplotlib.pyplot as plt
xx = []
yy = []
yy2 = []

with open('/home/dein/github_repo/VASP_reproducing/MD_part1/ES_EP_list.dat', 'r') as toten:
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
plt.plot(xx, yy, label="nose kinetic")
plt.plot(xx, yy2, label="nose potential")
plt.xlabel("Step")
plt.ylabel("Energy(eV)")
#plt.axis([0.0,30.0,-0.323,-0.322])
plt.title("nose potential & kinetic")
plt.legend()
plt.grid()
plt.savefig("plot_ES_EP.png")
plt.show() 