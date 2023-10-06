def contador (n):
    resultado = []
    for numero in range(n,-1,-1):
        resultado.append(numero)
    return resultado
print(contador(10))