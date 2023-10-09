def isFeasible(deck, nextCandIdx, riskLeft):
    return riskLeft - deck[nextCandIdx][1] >= 0


def greedyDeck(deck, maxRisk):
    finalDeck = []
    isSol = False
    n = len(deck)
    nextCandIdx = 0
    riskLeft = maxRisk
    benefit = 0
    while not isSol and nextCandIdx < n:
        card = deck[nextCandIdx]
        if isFeasible(deck, nextCandIdx, riskLeft):
            riskLeft -= card[1]
            benefit += card[2]
            finalDeck.append(card[3])
        else:
            value = riskLeft / card[1]
            benefit += value * card[2]
            finalDeck.append(card[3])
            isSol = True
        nextCandIdx += 1
    return finalDeck



n, m = map(int, input().strip().split())
cartas = []
for i in range(n):
    c, r, b = map(str, input().strip().split())
    cartas.append((int(r)/int(b), int(r), int(b), c, i))
cartas.sort()

print(" ".join(greedyDeck(cartas, m)))