l = []
final = []
n = input().split("-1")
n1 = n[0]

for i in n1:
    if i != " ":
        l.append(int(i))

for i in l:
    if l.count(i) >= 3 and final.count(i) < 1:
        final.append(i)

final.sort()

for i in final:
    final[final.index(i)] = str(i)

print(" ".join(final))
