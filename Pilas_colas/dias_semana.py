semana=['lunes', 'martes', 'miércoles', 'jueves', 
       'viernes', 'sábado']
print(type(semana))       
for n in range(len(semana)):
    print(n+1, semana[n])

semana.append('domingo')
print("apilamos el dia domingo")
for i in range(len(semana)):
    print(i+1, semana[i])
