import matplotlib.pyplot as plt

xx = []
yy = []
yy2 = []

with open('/home/dein/VASP_dein/md-part1/MD/temperature_list.dat', 'r') as toten:
    lines = toten.readlines()

for i in range(2, 32):
    line_split = lines[i].split()
    print(line_split)
    xx.append(int(line_split[0]))
    yy.append(float(line_split[1]))
    yy2.append(float(line_split[2]))

print(xx)
print(yy)
print(yy2)

# 그림과 첫 번째 축(ax1) 생성
fig, ax1 = plt.subplots(figsize=(6, 4))

# --- 첫 번째 축 (왼쪽 y축): yy (temperature) ---
color1 = 'tab:blue'
ax1.set_xlabel("Step")
ax1.set_ylabel("Temperature(K)", color=color1)
# 이중축의 핵심은 범례를 합치는 것. 선은 그려졌고,선에 대한 리스트가 line1에 저장됨.
line1 = ax1.plot(xx, yy, color=color1, label="temperature", linewidth=4, alpha=0.5)
ax1.tick_params(axis='y', labelcolor=color1)
ax1.grid(True)

# --- 두 번째 축 (오른쪽 y축): yy2 (kinetic energy) ---
ax2 = ax1.twinx()  # ax1과 x축을 공유하는 ax2 생성
color2 = 'tab:red'
ax2.set_ylabel("Kinetic Energy", color=color2)
line2 = ax2.plot(xx, yy2, color=color2, label="kinetic energy", linewidth=2, linestyle='--', alpha=1.0)
ax2.tick_params(axis='y', labelcolor=color2)

# --- 범례(Legend) 합치기 ---
# ax1과 ax2의 그래프(line)들을 하나의 리스트로 합칩니다.
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='best')

plt.title("EKIN, temperature")
fig.tight_layout() # 라벨이나 축이 잘리지 않도록 여백 자동 조정
plt.savefig("plot_temperature_2layer.png")
plt.show()