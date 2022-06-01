from menuOpciones import menu


m = menu()

while True:
    try:
        lineasMenu = m.datosMenu()
        for lin in lineasMenu:
            print(lin)
        opcion=int(input())
        break
    except ValueError as e:
        print("La opcion solo puede ser numerica entre 1-5.")
        input()

if opcion == 5:
    m.limpiaConsola()
    print("\nBuen viaje! y saludos.\n")
    m.opSalir()

