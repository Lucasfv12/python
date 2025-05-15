lista = []
for i in range(5):
    num = int(input("Ingresá un numero :"))
    lista.append(num)
print("Lista cargada: ", lista)

menor = lista[0]
pos = 0

for j in range(1,5):
    if lista[j]<menor:
        menor = lista[j]
        pos = j

print("el menor numero es ",menor)
print("la posicion es :", pos)


