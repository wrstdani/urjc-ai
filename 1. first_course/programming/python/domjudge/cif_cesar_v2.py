l, d = map(str, input().strip().split())
x = ord(l) + int(d)
while ord('z') < x:
    x -= 26
print(chr(x))
