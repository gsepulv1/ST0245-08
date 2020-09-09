def seleccion(lista):
    nb = len(lista)
    for actual in range(0,nb):    
        mas_pequeno = actual
        for j in range(actual+1,nb) :
            if lista[j] < lista[mas_pequeno] :
                mas_pequeno = j
        if min is not actual :
            temp = lista[actual]
            lista[actual] = lista[mas_pequeno]
            lista[mas_pequeno] = temp

lista = [5,2,4,1,3]
seleccion(lista)
print(lista)