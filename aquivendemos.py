'''
Stock de tienda aqui vendemos
'''
import os
print('**************************************************')
print('************ADMINISTRACION DE STOCK***************')
print('**************************************************')
productos = {'Escoba': 5, 'Huevos': 25, 'leche': 9}
menup = ['Ver producto stock del producto', 'Añadir nuevo producto', 'Ajustar stock', 'Eliminar producto', 'Salir']

while True:
    for ind in range(len(menup)):
        print(f'{ind+1}. {menup[ind]}')
        ans = input('¿Que quieres hacer?\n')
    if ans == '1':
        os.system ('cls')
        for a, b in productos.items():
            print(f'{a.center (20)}: {b}')
            print()
    elif ans == '2':
        os.system('cls')
        while True:
            nom = input('ingrese el nombre del nuevo producto\n')
            if nom.replace('',' ').isalpha():
                break
            if nom.lower in productos:
                os.system('cls')
                print('error: el producto ya existe\n')
                continue
            else:
                os.system('cls')
                productos [nom.lower] = 0
                print('Producto agregado correctamente!\n')
    elif ans == '3':
        print('¿que cproducto desea ajustar el stock?\n')
    elif ans == '4':
        os.system('cls')
        while True:
            nom = input('Ingrese el nombre del producto que quiere eliminar\n')
            if nom.replace('', ' ').isalpha():
                break
            if nom.lower in productos:
                os.system('cls')
                del productos [nom.lower]
                print('Producto eliminado correctamente!\n')
            else: 
                os.system('cls')
                print('Error: el producto no existe\n')
    elif ans == '5':
        os.system('cls')
        exit('Gracias, Adios!\n')
    else:
        os.system('cls')
        print('Error: opción no valida\n')