def nuggets(n):
    if n == 0:
        return True
    elif n < 6:
        return False
    else:
        return nuggets(n-20) or nuggets(n-9) or nuggets(n-6)

for i in range(0, 10000):
    if nuggets(i) is False:
        print(i)