with open("OUTCAR", "r") as f:
    step = 0
    etotal = 0.0
    ion_el = 0.0  

    print(f"{'Step':<5} {'ETOTAL':<15} {'Ion-Electron':<15}")
    print("-" * 40)

    for line in f:
        # 1. 먼저 나오는 데이터를 변수에 저장만 해둠
        if "ion-electron   TOTEN" in line:
            ion_el = line.split()[4]

        # 2. 나중에 나오는 데이터를 만났을 때 'step'을 올리고 'print' 실행
        if "ETOTAL" in line:
            step += 1
            etotal = line.split()[4]
            # 이제 두 데이터가 모두 현재 스텝의 값으로 채워진 상태입니다.
            print(f"{step:<5} {etotal:<15} {ion_el:<15}")

# 파일로 저장 python3 extract_energy.py > energy_list.dat
