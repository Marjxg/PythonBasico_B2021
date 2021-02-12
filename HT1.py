print('Bienvenido al programa.')
b = int(input("Por favor, ingrese un número entero: "))

for i in range(b):
    for j in range(i+1):
        print("*", end="")
    print("")