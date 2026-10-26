import sys

catalogo = {
    "Americano": {"nombre": "Café Americano", "precio": 45.50, "stock": 10},
    "Matcha Latte": {"nombre": "Matcha Latte", "precio": 68.00, "stock": 5},
    "Galleta Avena": {"nombre": "Galleta de Avena", "precio": 25.00, "stock": 15},
    "Cold Brew": {"nombre": "Cold Brew", "precio": 55.00, "stock": 8}
}

carrito = {}

print("--- CATÁLOGO DISPONIBLE ---")
for codigo, datos in catalogo.items():
    print(f"- {codigo.title()} (${datos['precio']:.2f} | Stock: {datos['stock']})")
print("-" * 30)

# Bloque 1 de anidación al carrito
decision1 = 'si'
while decision1 == 'si':
    producto = input('Qué quieres comprar?')
    try:
        catalogo[producto.title().strip()]
    except KeyError:
        print('Producto inexistente o fuera de stock')
        continue
    decision1 = input('Deseas agregar otro producto? ')
    while decision1.lower().strip() != 'si' and decision1.lower().strip() != 'no':
        decision1 = input('La decision tiene que ser si o no ')
    if decision1 == 'no':
        carrito[producto.title().strip()] = None
        if len(carrito) == 0:
            print('Muy bien, programa finalizado')
            sys.exit()
        else:
            print('Procesando su orden... ')

    if decision1 == 'si':
        carrito[producto.title().strip()] = None
        continue

# Bloque 2 escogiendo cantidades

lista_de_cantidades = []
for n in carrito.keys():
    while True:
        cantidad = input(f'Cuál es la cantidad de {n} que vas a comprar? ')
        try:
            cantidad = int(cantidad)
        except ValueError:
            print('La cantidad debe representar un número')
        if cantidad <= 0:
            print('La cantidad no puede ser igual o menor a 0')
            continue
        elif cantidad > catalogo[n]['stock']:
            print('La cantidad excede el número de stock que tenemos')
            continue
        carrito[n] = cantidad
        lista_de_cantidades.append(catalogo[n]['precio'] * cantidad)
        catalogo[n]['stock'] = catalogo[n]['stock'] - cantidad
        break

# Bloque 3 - Procesando la compra
print(f'''
{'-'* 45}''')
for producto, cantidad in carrito.items():
    print(f'{producto:<18} {'-':<1} x{cantidad:>2} {'|':>8} ${catalogo[producto.title().strip()]['precio']} ')
print(f'{'-'* 45}')
print(f'{f'Total a pagar: {f'${sum(lista_de_cantidades)}':<3}':>45}')



