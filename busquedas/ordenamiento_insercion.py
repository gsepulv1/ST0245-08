def Insercion(lista_a): #numeros es una lista
  for i in range(1,len(lista_a)):
    valor_a_ordenar =lista_a[i]
    while lista_a[i-1] > valor_a_ordenar and i >0:
      lista_a[i], lista_a[i-1]= lista_a[i-1], lista_a[i]
      i = i-1
  return lista_a
lista = [8,9,2,15]  
print(Insercion(lista))