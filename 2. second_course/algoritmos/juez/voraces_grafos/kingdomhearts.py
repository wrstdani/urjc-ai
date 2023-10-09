def update_components(carreteras, old_id, new_id):
    for i in range(len(carreteras)):
        if carreteras[i] == old_id:
            carreteras[i] = new_id


def kruskal(m, carreteras):
    components = list(range(m))
    count = n
    enemies = 0
    carreteras.sort()

    i = 0
    while count > 1 and len(carreteras) > i:
        e, u, v = carreteras[i]
        if components[u] != components[v]:
            count -= 1
            enemies += e
            update_components(carreteras, components[u], components[v])
        i += 1
    return enemies


n, m = map(int, input().strip().split())
carreteras = []
for i in range(m):
    u, v, e = map(int, input().strip().split())
    carreteras.append((e, u, v))
print(kruskal(m, carreteras))