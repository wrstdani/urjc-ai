


n, m = map(int, input().strip().split())
pasillos = []
for i in range(m):
    h1, h2, c = map(int, input().strip().split())
    pasillos.append((c, h1, h2))
pasillos.sort()
