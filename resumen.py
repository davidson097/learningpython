""" Esto es python"""

print("Bienvenidos a ErizoERP")
nombre = "davidson"
apellido = "de los santos"
edad = 28
cargo = "analsita power bi"
mensaje = f"""
Gracias por usar mi calculadora mi nombre es {nombre.capitalize()} {apellido.title()}, tengo {edad} de edad,
trabajo como {cargo.title()}, fue un verdadero placer servirle de ayuda.
"""
app = int(input("Que app desea usar?\n"
                "Opcion#1: Calculadora\n"
                "Opcion#2: Salir\n"))
if app < 1 or app > 2:
    print("Digite las opciones 1 o 2!")
elif app == 2:
    print("Vuelva pronto")
    exit()
elif app == 1:
    print("Bienvenidos a la calculadora")
    op = int(input(
        "Que operacion desea realizar?\n"
        "1-Suma\n"
        "2-Resta\n"
        "3-Multiplicacion\n"
        "4-Division\n"
        "5-Salir:\n"))
    if op < 1 or op > 5:
        print("Digite un numero del 1 al 5!")
    elif op == 1:
        n1 = int(input("Ingrese el primer valor: "))
        n2 = int(input("Ingrese el segundo valor: "))

        suma = n1 + n2
        print(f"La suma de los numeros {n1} y {n2} es {suma}")
        print(mensaje)
    elif op == 2:
        n1 = int(input("Ingrese el primer valor: "))
        n2 = int(input("Ingrese el segundo valor: "))

        resta = n1 - n2
        print(f"La resta de los numeros {n1} y {n2} es {resta}")
        print(mensaje)
    elif op == 3:
        n1 = int(input("Ingrese el primer valor: "))
        n2 = int(input("Ingrese el segundo valor: "))

        multi = n1 * n2
        print(f"La multiplicacion de los numeros {n1} y {n2} es {multi}")
        print(mensaje)
    elif op == 4:
        n1 = int(input("Ingrese el primer valor: "))
        n2 = int(input("Ingrese el segundo valor: "))

        div = n1 / n2
        print(f"La multiplicacion de los numeros {n1} y {n2} es {div}")
        print(mensaje)
    elif op == 5:
        print("Vuelva pronto")
        exit()
# elif app == 2:
    # exit()
