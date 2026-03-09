with open("OUTCAR", "r") as f:
    step = 0
    nose_kin = 0.0
    nose_pot = 0.0  # 변수 추가

    print(f"{'Step':<5} {'nose kinetic':<15} {'nose potential':<15}")
    print("-" * 40)

    for line in f:
        # 1. 먼저 나오는 데이터를 변수에 저장만 해둠
        if "nose potential ES" in line:
            nose_pot = line.split()[4]

        # 2. 나중에 나오는 데이터를 만났을 때 'step'을 올리고 'print' 실행
        if "nose kinetic   EPS" in line:
            step += 1
            nose_kin = line.split()[4]
            # 이제 두 데이터가 모두 현재 스텝의 값으로 채워진 상태입니다.
            print(f"{step:<5} {nose_kin:<15} {nose_pot:<15}")
# 파일로 저장 python3 extract_ES_EP.py > ES_EP_list.dat