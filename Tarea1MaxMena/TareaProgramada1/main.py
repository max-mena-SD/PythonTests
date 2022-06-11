from menuOpciones import menu


m = menu()

while True:
    try:
        lineasMenu = m.datosMenu()
        for lin in lineasMenu:
            print(lin)
        opcion=int(input())
        
        if opcion == 5:
            m.limpiaConsola()
            print("\nBuen viaje! y saludos.\n")
            m.opSalir()
        elif opcion == 1:
            m.limpiaConsola()
            est = True
            while est:
                try:
                    texto = input("Ingrese el texto que desea ingresar: ")

                    if texto != "":
                        m.agregarTexto(texto)
                        est = False
                    else:
                        print("No se ingreso ningun texto vuelva a intentarlo.")
                    
                except BaseException as e:
                    print(e.args)
                    print ("error capturado")
                    break
        elif opcion == 2:
            m.limpiaConsola()
            print(m.mostrarTexto())
            input()

        elif opcion == 3:
            m.limpiaConsola()
            email = input("Ingrese un correo electronico para enviar la información: ")
            m.prepara_correo(email) if m.verifica_correo(email) else print("El correo ingresado no tiene un formato correcto")
            input()
            
        elif opcion == 4:
            m.limpiaConsola()
            email = input("Ingrese un correo electronico para enviar la información: ")
            m.correo_info_logs(email) if m.verifica_correo(email) else print("El correo ingresado no tiene un formato correcto")
            input()

    except ValueError as e:
        print("La opcion solo puede ser numerica entre 1-5.")
        input()




