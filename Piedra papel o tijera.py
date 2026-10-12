import random

# Interfaz
print('''Vamos a jugar piedra papel o tijera
Estas listo? (si/no)''')
Interfaz = input()

if Interfaz.lower().strip() == 'si':
    print('Excelente! Elige tu pieza: ')
else:
    print('Ni modo!, vamos a darle')

# La maquina selecciona
opciones = ('piedra', 'papel', 'tijera')
rival = random.choice(opciones)

## Inicio del juego
juego = 'si'
while juego == 'si':
    # Decision del juego
    print('''
Piedra --- Le ganas a tijera, pierdes contra papel
Papel --- Le ganas a piedra, pierdes contra tijera
Tijera --- Le ganas a papel, pierdes contra piedra''')
    Decision = input()

    # Secuecia de decisiones
    match Decision.lower().strip():
        case 'piedra':
           if rival == 'piedra':
             print(f'Empatamos! Yo había escogido {rival}')
           elif rival == 'papel':
             print(f'Perdiste! Yo había escogido {rival}')
           elif rival == 'tijera':
             print(f'Ganaste! Yo había escogido {rival}')
        case 'tijera':
           if rival == 'piedra':
             print(f'Perdiste! Yo había escogido {rival}')
           elif rival == 'papel':
             print(f'Ganaste! Yo había escogido {rival}')
           elif rival == 'tijera':
             print(f'Empatamos! Yo había escogido {rival}')
        case 'papel':
           if rival == 'piedra':
             print(f'Ganaste! Yo había escogido {rival}')
           elif rival == 'papel':
             print(f'Empatamos! Yo había escogido {rival}')
           elif rival == 'tijera':
             print(f'Perdiste! Yo había escogido {rival}')
        case _:
             print('No ingresaste una opcion correcta\nIntentalo de nuevo')
             continue
    juego = input('Quieres jugar de nuevo (si/no)') # Reinicio

# Pantalla final
print('FIN DEL JUEGO')



