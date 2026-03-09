with open("OUTCAR", "r") as f:
    step = 0
    temperature = 0.0
    KE = 0.0  # 변수 추가

    print(f"{'Step':<5} {'temperature':<15} {'kinetic energy':<15}")
    print("-" * 40)

    for line in f:
        # 1. 먼저 나오는 데이터를 변수에 저장만 해둠
        if "kinetic energy EKIN" in line:
            KE = line.split()[4]

        # 2. 나중에 나오는 데이터를 만났을 때 'step'을 올리고 'print' 실행
        if "kin. lattice  EKIN_LAT=" in line:
            step += 1
            temperature = line.split()[5]
            # 이제 두 데이터가 모두 현재 스텝의 값으로 채워진 상태입니다.
            print(f"{step:<5} {temperature:<15} {KE:<15}")
# 파일로 저장 python3 extract_KE_temperature.py > temperature_list.dat               