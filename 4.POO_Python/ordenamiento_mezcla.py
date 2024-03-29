import random

def ordenamiento_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista)//2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        print(izquierda,'-'*4,derecha)

        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        
        print(f'derecha {derecha} , izquierda {izquierda}')
        print(lista)
        print('-'*25)
    return lista


if __name__ == '__main__':
    tamanio_lista = int(input('De que tamaño sera la lista: '))
    lista = [random.randint(0,100) for i in range(tamanio_lista)]
    print(f'Listado desordenado {lista}')
    lista = ordenamiento_mezcla(lista)
    print(f'Listado ordenado {lista}')