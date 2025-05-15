lista=[3,55,2,1]

def suma(lista):
    total=1
    for i in range(len(lista)):
        total=total+lista[i]
    return total

print(suma(lista))