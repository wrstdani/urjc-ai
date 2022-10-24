t = int(input())
g = float(input())
s = float(input())

cond1 = t > 5
cond2 = g > 1500 and s > 1.2

if cond1 or cond2 or (cond1 and cond2):
    print('1')
else:
    print('0')
