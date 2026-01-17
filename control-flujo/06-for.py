buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break
else:
    print("No encontre el numero buscado", buscar)

for char in "Ultimate Python":
    print(char)
