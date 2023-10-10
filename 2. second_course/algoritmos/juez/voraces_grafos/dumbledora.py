def update_components(components, old_id, new_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id


def add_cost_to_room(cost_per_room, c, h1, h2):
    cost_per_room[h1] += c
    cost_per_room[h2] += c


def the_prisoner_of_kruskaban(pasillos, M, N):
    components = list(range(M))
    cost_per_room = N * [0]
    count = M
    CT = 0

    i = 0
    while count > 1 and len(pasillos) > i:
        c, h1, h2 = pasillos[i]
        if components[h1] != components[h2]:
            count -= 1
            CT += c
            add_cost_to_room(cost_per_room, c, h1, h2)
            update_components(components, components[h1], components[h2])
        i += 1

    return f"Coste total: {CT}", cost_per_room
    


N, M = map(int, input().strip().split())
pasillos = []
for i in range(M):
    h1, h2, c = map(int, input().strip().split())
    pasillos.append((c, h1, h2))
pasillos.sort()
total_cost, cost_per_room = the_prisoner_of_kruskaban(pasillos, M, N)
print(total_cost)
for i in range(len(cost_per_room)):
    print(f"H{i}: {cost_per_room[i]}")
