# def summa(lista):
#     return sum(lista)

def summa(lista):
    tulos = 0 

    for luku in lista:
        tulos += luku
    return tulos 

lista = [1, 2, 3, 4, 5]
# tulos = summa(lista)
print(summa(lista))

