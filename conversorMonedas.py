def conversor(valor_dolar):
    dolares = moneda / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dolares.")

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
    moneda = float(input("Cuantos soles peruanos tienes?: "))
    conversor(4.094)
   
elif opcion == 2:
    moneda =  float(input("Cuantos pesos colombianos tienes?: "))
    conversor(3866.4)
elif opcion == 3:
    moneda = float(input("Cuantos pesos chilenos tienes?: "))
    conversor(786.51)
elif opcion == 4:
    moneda =  float(input("Cuantos bolivares bolivianos tienes?: "))
    conversor(6.84)

elif opcion == 5:
    moneda =  float(input("Cuantos pesos argentinos tienes?: "))
    conversor(97.28)
elif opcion == 6:
    moneda =  float(input("Cuantos bolivares venezolanos tienes?: "))
    conversor(4031330.00)
else:
    print("Elige una de las opciones mencionadas")

