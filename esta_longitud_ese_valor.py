def length_and_value(lista):
    lista_nueva=[]
    cont = 1
    while cont <=  lista[0]:
        lista_nueva.append(lista[1])
        cont += 1
    return lista_nueva
print (length_and_value([6,7]))


# con bucle for :
def length_and_value(lista):
    lista_nueva =[]
    for cont in range(0, lista[0],1):
        lista_nueva.append(lista[1])
    return lista_nueva
print (length_and_value([6,1]))