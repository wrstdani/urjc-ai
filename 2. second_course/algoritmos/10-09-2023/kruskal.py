def update_components(components, old_id, new_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id


def kruskal(n, edges):
    components = list(range(n))
    count = n
    mst = 0
    edges.sort()

    i = 0
    while count > 1 and len(edges) > i:
        w, u, v = edges[i]
        if components[u] != components[v]:
            count -= 1
            mst += w
            update_components(components, components[u], components[v])
        i += 1
    return mst


n, m = map(int, input().stirp().split())
edges = []
for _ in range(n):
    u, v, w = map(int, input().strip().split())
    edges.append((w, u, v))

mst = kruskal(n, edges)
print(mst)
