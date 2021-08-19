#Convierte soles a dolares USD
soles =  input("Cuantos soles peruanos tienes?: ")
soles = float(soles)
valor_dolar = 4.08
dolares = soles / valor_dolar
dolares = round(dolares, 2) #la funcion round devulve la cantidad de decimales indicado en (.,..) en este caso 2 unidades
dolares = str(dolares)
print("Tienes  $" + dolares + " dolares.")

print("******************************************************")
#Convierte dolares a soles peruanos
dolares = input("Cuantos dolares tienes?: ")
dolares = float(dolares)
valor_nuevoSol = 0.24
sol_peruano = dolares / valor_nuevoSol
sol_peruano = round(sol_peruano, 2)
sol_peruano = str(sol_peruano)
print("Tienes S/" + sol_peruano + " nuevo soles.")
