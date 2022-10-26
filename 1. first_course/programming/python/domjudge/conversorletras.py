c = input().strip()

def capital (c):
    if c.isupper():
        return True
    else:
        return False

if capital(c) == True:
    print(c.lower())
else:
    print(c.upper())