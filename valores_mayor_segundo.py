def factoria(lista):
    if len(lista)<2:
        return False

    nuevalista=[]
    for valor in lista:
        if valor > lista[1]:
            nuevalista.append(valor)
    print(f'Son {len(nuevalista)} valores mayores al segundo que es {lista[1]}')
    return nuevalista

print(factoria([5,2,3,2,1,4]))
print(factoria([5]))