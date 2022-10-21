C = str(input().strip())
N = int(input())
abc = str('abcdefghijklmnopqrstuvwxyz')
for i in abc:
    if i == C:
        x = (abc.index(C) + N)
        if 1 <= N <= 25:
            while x > 25:
                x -= 26
            print(abc[x])
