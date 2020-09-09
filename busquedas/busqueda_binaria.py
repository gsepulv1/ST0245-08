# sobre una lista ordenada 
valor = int(input("digite el número a buscar: ") )
def busqueda_binaria(lista,valor):
    encontrado = False
    izquierda =0
    derecha = len(lista)-1 # der guarda el índice fin del segmento
    while izquierda <= derecha:
        medio =(izquierda +derecha)//2
        if lista[medio] == valor:
            encontrado =True
            return encontrado, medio
            
        elif lista[medio]> valor:
            derecha = medio -1
        else:
            izquierda = medio +1

    return encontrado

numeros =[2,3,5,13,31,39]
print(busqueda_binaria(numeros,valor))

