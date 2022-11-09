def cifras(x):
    num_cif = 1
    while x // (10 ** num_cif) > 0:
        num_cif += 1
    return num_cif

print(cifras(135))