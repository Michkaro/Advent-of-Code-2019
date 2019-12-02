codes = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,9,23,27,1,5,27,31,1,5,31,35,1,35,13,39,1,39,9,43,1,5,43,47,1,47,6,51,1,51,13,55,1,55,9,59,1,59,13,63,2,63,13,67,1,67,10,71,1,71,6,75,2,10,75,79,2,10,79,83,1,5,83,87,2,6,87,91,1,91,6,95,1,95,13,99,2,99,13,103,1,103,9,107,1,10,107,111,2,111,13,115,1,10,115,119,1,10,119,123,2,13,123,127,2,6,127,131,1,13,131,135,1,135,2,139,1,139,6,0,99,2,0,14,0]

for x in range(99):
    for y in range(99):
        c = [c for c in codes]
        c[1] = x
        c[2] = y
        ip = 0
        while True:
            opcode = c[ip]
            i1, i2, i3 = c[ip + 1], c[ip + 2], c[ip + 3]
            if opcode == 1:
                c[i3] = c[i1] + c[i2]
            elif opcode == 2:
                c[i3] = c[i1] * c[i2]
            else:
                assert opcode == 99
                break
            ip += 4
        if c[0] == 19690720:
            print(x, y)
