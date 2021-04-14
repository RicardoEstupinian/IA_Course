import random

def ordenamiento_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j] #Notacion Swaping en python para intercambian valores
    return lista
                


if __name__ == '__main__':
    lista = [13,7,9,15,3,10,5,10,8,2,9,9,11,7,9,7,7,7,13,11,14,9,8,13,10,16,12,12,8,6,7,8,8,13,9,7,9,8]
    suma = 0
    for i in lista:
        suma +=i
    print(suma)
    lista = ordenamiento_burbuja(lista)
    print(f'Listado ordenado {lista}')