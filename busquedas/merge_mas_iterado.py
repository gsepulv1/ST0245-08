# caso base: si la longitud de la lista es menor o igual a 1 la lista ya esta ordenada
# el caso base estara establecido por: Len(lista)>1
# si la longitud de la lista es  impar. no importa porque las logitudes de las sublitas seran diferentes a lo sumo en 1
def Omerge(unaLista):
    print("Dividir ",unaLista)
    if len(unaLista)>1:
        mitad = len(unaLista)//2
        mitadIzquierda = unaLista[:mitad]
        mitadDerecha = unaLista[mitad:]
        ## LLamada recursiva para cada lista 
        Omerge(mitadIzquierda)
        Omerge(mitadDerecha)
        i=0
        j=0
        k=0
        while i < len(mitadIzquierda) and j < len(mitadDerecha):
            if mitadIzquierda[i] < mitadDerecha[j]:
                unaLista[k]=mitadIzquierda[i]
                i=i+1
            else:
                unaLista[k]=mitadDerecha[j]
                j=j+1
            k=k+1
        while i < len(mitadIzquierda):
            unaLista[k]=mitadIzquierda[i]
            i=i+1
            k=k+1

        while j < len(mitadDerecha):
            unaLista[k]=mitadDerecha[j]
            j=j+1
            k=k+1
    print("Mezclar ",unaLista)

unaLista = [54,26,93,17,77,31,44,55,20]
Omerge(unaLista)
print(unaLista)
