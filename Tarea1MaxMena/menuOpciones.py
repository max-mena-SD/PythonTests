from cmath import log
from distutils.log import debug, info
import os
import logging
import logging.config
import json

class menu:

    #constructor, no recibe, no devuelve
    def __init__(self):
        #lambda limpia pantalla, no recibe, no devuelve nada
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
        self.confJsonLogger("Salida de usuario", "info")
        exit()

    #carga el diccionario y lo transforma en Json, no recibe, no devuelve
    def LoggerJsonLoader(self):
        ruta = "conf.json"

        with open(ruta,"r") as archivo_json:
            contenido= archivo_json.read()
            contenido= json.loads(contenido)
            logging.config.dictConfig(contenido)

    #utiliza la configuracion de Json para llamar el log requerido, recibe dos variables una con el mensaje otra con el log a afectar, no devuelve
    def confJsonLogger(self, message="nota de accion", tipo="debug"):
        self.LoggerJsonLoader()

        log_entry= logging.getLogger(tipo)
        if tipo =="debug":
            log_entry.debug(message)
        elif tipo=="error":
            log_entry.error(message)
        elif tipo=="info":
            log_entry.info(message)
        else:
            log_entry = logging.getLogger("debug")
            log_entry.debug("Error en menuOpciones.menu.confJsonLogger"+str(tipo))
    