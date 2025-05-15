#Confeccionar una función que le enviemos un número de mes como parámetro y nos retorne una 
#tupla con todos los nombres de meses que faltan hasta fin de año

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
         "Noviembre", "Diciembre"]

def numero_mes():
    mes=int(input("Dame un número de mes: "))
    meses_faltantes = meses[mes-1:]
    return tuple(meses_faltantes)

print(numero_mes())

