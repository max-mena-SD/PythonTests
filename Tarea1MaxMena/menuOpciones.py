import os

class menu:

    #lambda limpia pantalla, no recibe, no devuelve nada
    def __init__(self):
        self.limpiaConsola = lambda: os.system('cls' if os.name in ('nt','dos') else 'clear')

    # def limpiaConsola():
    #     os.system('cls' if os.name in ('nt', 'dos') else 'clear')

    #datosMenu, limpia pantalla y tiene una lista de las opciones del menu, no recibe nada, retorna una lista.
    def datosMenu(self,):
        self.limpiaConsola()
        menu= ["Menu",
        "1. Ingresar texto.",
        "2. Ver la informacion del archivo.",
        "3. Enviar textos ingresados por correo electronico.",
        "4. Enviar informacion y logs por email.",
        "5. Salir",]
        
        return menu
    
    #opSalir, termina el programa, no recibe nada, no retorna nada
    def opSalir(self):
        exit()
