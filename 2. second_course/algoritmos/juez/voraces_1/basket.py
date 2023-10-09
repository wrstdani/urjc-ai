rep = int(input())
altmin = int(input())
nmin = 0
l = []

inp = input()

for i in inp.split(" "):
    l.append(int(i))
    if int(i) >= altmin:
        nmin += 1

print(l.index(min(l)), l.index(max(l)), nmin)