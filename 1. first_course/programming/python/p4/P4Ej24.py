n = int(input())
a = 1
form = 1/a

def serieRec(n, a, form):
    if n == 1:
        return 1
    else:   
        while a < n:
            a += 1
            form += 1/a
            serieRec(n, a, form)
        return form

def serieIter(n, form):
    if n == 1:
        return 1
    else:
        for b in range(2, n + 1):
            form += 1/b
        return form
        
print(serieRec(n, a, form))
print(serieIter(n, form))