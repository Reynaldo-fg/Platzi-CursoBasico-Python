menu = """Bienvenido al conversor de monedas 💰

Para Sol peruano eliga la opcion [1]
Para peso colombiano eliga la opcion [2]
Para peso chileno eliga la opcion [3]
Para boliviano eliga la opcion [4]
Para peso argentino eliga la opcion [5]
Para boliviar venezolano eliga la opcion [6]

Escoge una opcion: """

opcion = int(input(menu))

if opcion == 1:
    soles =  input("Cuantos soles peruanos tienes?: ")
    soles = float(soles)
    valor_dolar = 4.094
    dolares = soles / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dolares.")
elif opcion == 2:
    pesos =  input("Cuantos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3866.4
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dolares.")
elif opcion == 3:
    pesos =  input("Cuantos pesos chilenos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 786.51
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dolares.")
elif opcion == 4:
    bolivianos =  input("Cuantos bolivares bolivianos tienes?: ")
    bolivianos = float(bolivianos)
    valor_dolar = 6.84
    dolares = bolivianos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dolares.")
elif opcion == 5:
    pesos =  input("Cuantos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 97.28
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dolares.")
elif opcion == 6:
    bolivares =  input("Cuantos bolivares venezolanos tienes?: ")
    bolivares = float(bolivares)
    valor_dolar = 4031330.00
    dolares = bolivares / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dolares.")
else:
    print("Elige una de las opciones mencionadas")

