import pickle; import copy; import decimal; import sys; import os

# Bloque 0 - Definciones del programa
CONFIG_NEGOCIO = ("Dark Kitchen Premium", "v2.5-Enterprise", "0.16")
NOMBRE_LOCALIDAD, VERSION_SISTEMA, TASA_IVA_STR = CONFIG_NEGOCIO
TASA_IVA = decimal.Decimal(TASA_IVA_STR)

ARCHIVO_DB = "catalogo_db.pkl"
ARCHIVO_LOGS = "bitacora_transacciones.txt"

def inicializar_catalogo():
    catalogo = {
        'Cafe Chiapas': {'nombre': 'Café Chiapas Altura', 'precio': 52.50, 'stock': 15},
        'Matcha Latte': {'nombre': 'Matcha Latte Ceremonial', 'precio': 68.00, 'stock': 8},
        'Galleta Avena': {'nombre': 'Galleta de Avena y Miel', 'precio': 25.00, 'stock': 20},
        'Latte Vainilla': {'nombre': 'Latte Vainilla Artesanal', 'precio': 58.00, 'stock': 12},
        'Cappuccino': {'nombre': 'Cappuccino Clásico', 'precio': 50.00, 'stock': 14},
        'Matcha Lavanda': {'nombre': 'Matcha Latte con Lavanda', 'precio': 75.00, 'stock': 6},
        'Chai Latte': {'nombre': 'Chai Latte Especiado', 'precio': 62.00, 'stock': 10},
        'Moka': {'nombre': 'Mocha Cacao Orgánico', 'precio': 70.00, 'stock': 9},
        'Panini De Pavo': {'nombre': 'Panini Pavo y Queso Gouda', 'precio': 85.00, 'stock': 7},
        'Croissant': {'nombre': 'Croissant de Mantequilla', 'precio': 38.00, 'stock': 15},
        'Muffin Arandanos': {'nombre': 'Muffin Integral de Arándanos', 'precio': 35.00, 'stock': 12},
        'Jugo Verde': {'nombre': 'Jugo Verde Detox (500ml)', 'precio': 48.00, 'stock': 8},
        'Botella De Agua': {'nombre': 'Agua de Manantial (600ml)', 'precio': 22.00, 'stock': 25},
        }

    if os.path.exists(ARCHIVO_DB):
        with open(ARCHIVO_DB, 'rb') as f:
            print("[Sistema] Cargando catálogo persistente desde disco...")
            return pickle.load(f)
    else:
        print("[Sistema] No se encontró base de datos previa. Creando catálogo inicial...")
        with open(ARCHIVO_DB, 'wb') as f:
            pickle.dump(catalogo, f)
            return catalogo

def auditar_memoria(original, copia):
    print("\n[Auditoría de Memoria]")
    print(f"ID Original: {id(original)} | ID Copia: {id(copia)}")
    print(f"¿Son objetos distintos en memoria?: {original is not copia}\n")


def registrar_en_bitacora(ticket_texto):
    with open(ARCHIVO_LOGS, 'a', encoding='utf-8') as f:
        f.write(ticket_texto + "\n" + ("=" * 45) + "\n")
    ticket_bytes = ticket_texto.encode('utf-8')
    print(f"[Simulación Red] Ticket codificado en bytes (UTF-8): {len(ticket_bytes)} bytes transmitidos.")

def auditar_bitacora_disco():
    print(f"\n--- Auditoría de Bitácora en Disco ({ARCHIVO_LOGS}) ---")
    if not os.path.exists(ARCHIVO_LOGS):
        print("La bitácora aún no ha sido creada.")
        return

    with open(ARCHIVO_LOGS, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
    if not lineas:
        print("La bitácora está vacía.")
    else:
        print(f"Estado: Bitácora activa con {len(lineas)} líneas registradas.")


if __name__ == "__main__":
    print(f"=========================================")
    print(f"  {NOMBRE_LOCALIDAD} ({VERSION_SISTEMA})  ")
    print(f"=========================================\n")


catalogo = inicializar_catalogo()
catalogo_original = copy.deepcopy(catalogo)
auditar_memoria(catalogo_original, catalogo)
catalogo_original = copy.deepcopy(catalogo)

carrito = {}

# Interfaz
print("--- CATÁLOGO DISPONIBLE ---")
for codigo, datos in catalogo.items():
    print(f'- {f'{codigo.title()}':<18} - ${datos['precio']:.2f} | Stock: {datos['stock']}')
print("-" * 30)

# Bloque 1 - Comprando
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

# Bloque 2 - Eligiendo cantidades y actualizando catalogo
lista_de_cantidades = []
for n in carrito.keys():
    while True:
        cantidad = input(f'Cuál es la cantidad de {n} que vas a comprar? ')
        try:
            cantidad = int(cantidad)
        except ValueError:
            print('La cantidad debe representar un número valido')
            continue
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

# Procesamiento de total + IVA
b = decimal.Decimal(sum(lista_de_cantidades)) * decimal.Decimal('0.16')
IVA = b.quantize(decimal.Decimal('0.01'))
Total = decimal.Decimal(sum(lista_de_cantidades)) + decimal.Decimal(IVA)

# Bloque 3 - Impresion de tickets
lineas_ticket = []
lineas_ticket.append(f" {'---- ':<12} TICKET DE COMPRA {'---- ':>12}")
lineas_ticket.append("-" * 45)
for producto, cantidad in carrito.items():
    precio_unit = catalogo[producto]['precio']
    sub_item = precio_unit * cantidad
    lineas_ticket.append(f"{producto:<18} {'-':<1} x{cantidad:>2} {'|':>14} ${catalogo[producto.title().strip()]['precio']}")
lineas_ticket.append(f'IVA {'-':>16} {'|':>18} ${IVA:>}')
lineas_ticket.append("-" * 45)
lineas_ticket.append(f'{f'Total a pagar: {f'${Total}':<3}':>45}')

ticket_final_str = "\n".join(lineas_ticket)
print("\n" + ticket_final_str + "\n")

with open(ARCHIVO_DB, 'wb') as f:
    pickle.dump(catalogo, f)
print("[Sistema] Inventario actualizado guardado en disco (`catalogo_db.pkl`).")

registrar_en_bitacora(ticket_final_str)
auditar_bitacora_disco()

