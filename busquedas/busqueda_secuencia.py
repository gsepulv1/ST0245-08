# busqueda secuencia
llave = int(input("digite el numero a buscar: ") )
def busqueda_secuencial(lista, valor):
    posicion = 0
    encontrado = False
    while posicion < len(lista) and not encontrado:
        if lista[posicion] == valor:
            encontrado = True
        else:
            posicion  +=1
    if encontrado == True:
       return encontrado, posicion 
    else:
        return encontrado

numeros =[2,7,3,5,13,31,29,17,19]
print(busqueda_secuencial(numeros,llave))