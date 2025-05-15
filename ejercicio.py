#Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
#Obtener el promedio de las mismas.

alturas = []

for i in range(5):
    altura = float(input(f"ingresá la primer altura {i+1}: "))
    alturas.append(altura)

altura_max = max(alturas)

print(altura_max)
