def update_components(components, old_id, new_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id


def attack_on_kruskal(conexions, M):
    components = list(range(M))
    count = M
    mst = 0
    
    i = 0
    while count > 1 and len(conexions) > i:
        d, n1, n2 = conexions[i]
        if components[n1] != components[n2]:
            count -= 1
            mst += d
            update_components(components, components[n1], components[n2])
        i += 1
    return mst



N, M = map(int, input().strip().split())
conexions = []
for i in range(M):
    n1, n2, d = map(int, input().strip().split())
    conexions.append((d, n1, n2))
conexions.sort()
distancia_total = attack_on_kruskal(conexions, M)
if distancia_total % 5 != 0:
    coste_total = int(distancia_total/5) + 1
else:
    coste_total = distancia_total/5
print(coste_total)
