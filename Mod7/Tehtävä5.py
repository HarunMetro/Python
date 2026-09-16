def parittomat(lista):
    karsittu = []

    for luku in lista:
        if luku % 2 == 0:
            karsittu.append(luku)
    return karsittu

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
karssittu = parittomat(lista)

print("alkuperäinen lista", lista)
print("karsittu lista", karssittu)