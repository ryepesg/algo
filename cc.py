def cc(M):
    m, n = len(M), len(M[0])
    ly, lx = [], []
    for j in range(1, m):
        for i in range(n):
            if M[j][i] != M[j-1][i]:
                ly.append(j)
                break
    for i in range(1, n):
        for j in range(m):
            if M[j][i] != M[j][i-1]:
                lx.append(i)
                break
    C = []
    for j in range(len(ly)-1):
        C.append([])
        for i in range(len(lx)-1):
            C[j].append(M[ly[j]][lx[i]])

    print("\n".join("".join(c) for c in C))
    print()

cc(["----------",
    "|....x...|",
    "|....xxxx|",
    "|....x...|",
    "|........|",
    "|........|",
    "----------"])

cc(["XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X                          X               X",
    "X                          X               X",
    "X                          X               X",
    "X                          X               X",
    "X            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X            X             X               X",
    "X            X             X               X",
    "X            X             X               X",
    "X            X             X               X",
    "X       XXXXXXXXXXXXXXX    X               X",
    "X            X             X               X",
    "X            X             X               X",
    "X            X             X               X",
    "X            X             X               X",
    "X            X             X               X",
    "X            X             X               X",
    "X            X             X               X",
    "XXXXXXXXXXXXXX             X               X",
    "X                          X               X",
    "X                          X               X",
    "X                          X               X",
    "X                          X               X",
    "X                          X               X",
    "X                          X               X",
    "X                          X               X",
    "X                          X               X",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"])

cc(["-----|",
    "|O   |",
    "|  XX|",
    "|  X |",
    "|  X |",
    "------"])

cc(["-----------",
    "|H  |     |",
    "| | |     |",
    "|-|-|-----|",
    "| | |     |",
    "| | |     |",
    "| | | W   |",
    "| | |     |",
    "-----------"])
