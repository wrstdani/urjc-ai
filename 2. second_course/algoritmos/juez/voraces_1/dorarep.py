def greedydorarep(pedidos):
    waittime = 0
    nextelement = 0
    n = len(pedidos)
    while nextelement < n:
        pedido = pedidos[nextelement]
        waittime += pedido[0]
        nextelement += 1
    return waittime

n = int(input())
pedidos = []
for i in range(n):
    c, t = map(int, input().strip().split())
    pedidos.append((t, c))
pedidos.sort()
print(greedydorarep(pedidos))
