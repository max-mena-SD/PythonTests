
import json
import logging
import logging.config

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#https://betterprogramming.pub/easily-add-custom-attributes-to-logrecord-objects-in-python-31dae85592b1
#carga el diccionario y lo transforma en Json, no recibe, no devuelve
def LoggerJsonLoader(opcion, cant):
    ruta = "conf.json"

    with open(ruta,"r") as archivo_json:
        contenido= archivo_json.read()
        contenido= json.loads(contenido)
        logging.config.dictConfig(contenido)

    log_entry= logging.getLogger("info")
    log_entry.info(opcion, cant)

# #utiliza la configuracion de Json para llamar el log requerido, recibe dos variables una con el mensaje otra con el log a afectar, no devuelve
# def confJsonLogger( opcion, cant, tipo="info"):
#     LoggerJsonLoader()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def agregarTexto(texto):
    with open("doc.txt", "a", encoding="utf") as doc:
        texto = " " + texto
        doc = doc.write(texto)
    LoggerJsonLoader ("1", "10")
        # print("**","**")

est = True
while est:
    try:
        texto = input("Ingrese el texto que desea ingresar: ")

        if texto != "":
            agregarTexto(texto)
            # print(texto+ "/")
            est = False
        else:
            print("No se ingreso ningun texto vuelva a intentarlo.")
        
    except BaseException as e:
        print(e.args)
        print ("error capturado")
        break
    
