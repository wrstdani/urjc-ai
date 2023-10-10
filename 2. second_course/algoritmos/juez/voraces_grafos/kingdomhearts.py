def update_components(components, old_id, new_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id


def kruskal_hearts(roads, M):
    components = list(range(M))
    count = M
    enemies = 0

    i = 0
    while count > 1 and len(roads) > i:
        e, u, v = roads[i]
        if components[u] != components[v]:
            count -= 1
            enemies += e
            update_components(components, components[u], components[v])
        i += 1
    return enemies


N, M = map(int, input().strip().split())
roads = []
for i in range(M):
    u, v, e = map(int, input().strip().split())
    roads.append((e, u, v))
roads.sort()
total_enemies = kruskal_hearts(roads, M)
print(total_enemies)