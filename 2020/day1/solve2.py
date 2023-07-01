import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

ints = [int(l) for l in lines]

for i in range(len(ints)-1):
    for j in range(i+1,len(ints)):
        for k in range(i+1,len(ints)):
            v1, v2, v3 = ints[i], ints[j], ints[k]
            if v1 + v2 + v3 == 2020:
                print(v1*v2*v3)
                exit()


