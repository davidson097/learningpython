# numero = 1
# while numero < 100:
#     print(numero)
#     numero *= 2

while True:
    comando = input("Ingrese un comando (salir para terminar): ")
    print(f"Comando ingresado: {comando}")
    if comando.lower() == "salir":
        print("Saliendo del programa...")
        break
