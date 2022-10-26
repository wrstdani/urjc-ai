grados_cent = int(input())
grados_faren = int(input())

def cels_to_farenheit(grados_cent):
    grados_farenheit = (grados_cent * 9/5) + 32
    return grados_farenheit

def farnheit_to_cels(grados_faren):
    grados_centigrados = ((grados_faren - 32) * 5/9)
    return grados_centigrados

print("{:.2f}".format(cels_to_farenheit(grados_cent)), "{:.2f}".format(farnheit_to_cels(grados_faren)))