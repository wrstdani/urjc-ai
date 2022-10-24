n, m = map(int, input().strip().split())

if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    precio = n * 31

elif m == 4 or m == 6 or m == 9 or m == 11:
    precio = n * 30

else:
    precio = n * 28

print(str(precio))