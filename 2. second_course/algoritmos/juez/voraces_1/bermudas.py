def funct(ang):
    res = 0
    for i in ang.split(" "):
        if int(i) < 0:
            return "ERROR"
        else:
            res += int(i)
    if res == 180:
        return "SI"
    else:
        return "NO"

ang = input()
print(funct(ang))