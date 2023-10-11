def greedyrep(pedidos):
    ltiempo = []
    tiempo = 0
    n = len(pedidos)
    nextelement = 0
    while nextelement < n:
        pedido = pedidos[nextelement]
        tiempo += pedido[0]
        ltiempo.append(tiempo)
        nextelement += 1
    return sum(ltiempo)


n = int(input())
pedidos = []
for i in range(n):
    c, t = map(int, input().strip().split())
    pedidos.append((t, c))
pedidos.sort()
print(greedyrep(pedidos))
