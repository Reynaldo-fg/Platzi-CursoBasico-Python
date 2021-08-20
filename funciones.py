"""
def imprimir_mensaje():
    print('Mensaje especial: ')
    print('¡Estoy aprendiendo a usar funciones!')

imprimir_mensaje()
imprimir_mensaje()
imprimir_mensaje()
imprimir_mensaje()

"""

def conversion(mensaje):
    print('Hola')
    print('Como estas')
    print('Elegistes la opcion: '+str(mensaje))
    print('Adios')

opcion = int(input('Elegistes una opcion (1, 2, 3): '))
if opcion == 1:
    conversion(1)
elif opcion == 2:
    conversion(2)
elif opcion == 3:
    conversion(3)
else:
    conversion(1)