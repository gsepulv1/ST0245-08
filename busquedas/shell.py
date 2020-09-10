def shellSort(lista):
    mitad = len(lista)//2
    while mitad > 0:
      for posicion_inicial in range(mitad):#ir al esta el rango que se llama mitad
        reducir_busqueda(lista, posicion_inicial, mitad)

      print("antes de la pasada",mitad, "nueva lista", palabras)

      mitad = mitad // 2


def reducir_busqueda(nlist,start,gap):
    for i in range(start+gap,len(nlist),gap): #gap es el salto que se va dar 

        current_value = nlist[i]
        posicion = i

        while posicion>=gap and nlist[posicion-gap]>current_value:
            nlist[posicion]=nlist[posicion-gap]
            posicion = posicion-gap

        nlist[posicion]=current_value


palabras= ["ana","aaa", "zzzz", 'Bebe']
shellSort(palabras)
print(palabras)