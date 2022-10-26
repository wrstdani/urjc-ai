n = int(input())

def quality(n):
    if 0 <= n <= 10:
        return "CRUZCAMPO"
    elif 11 <= n <= 20:
        return "MALA"
    elif 21 <= n <= 35:
        return "REGULAR"
    elif 36 <= n <= 46:
        return "BUENA"
    elif n >= 46:
        return "MUY BUENA"

print(quality(n))