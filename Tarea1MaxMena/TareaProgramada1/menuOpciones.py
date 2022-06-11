##
from email.mime.base import MIMEBase
from DatosCorreo import datoscorreo as dc
##
from cmath import log
from distutils.log import debug, info
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
import logging
import logging.config
import json
import re

class menu:

    ruta= "./doc.txt"
    rutaJson = "./conf.json"
    limpiaConsola = None
    pattern = "^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$"
    ListaArchivos = ["doc.txt", "../logs/info.log", "conf.json"]

    #constructor, no recibe, no devuelve
    def __init__(self):
        #lambda limpia pantalla, no recibe, no devuelve nada
        self.limpiaConsola = lambda: os.system('cls' if os.name in ('nt','dos') else 'clear')

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

    #carga el diccionario y lo transforma en Json, no recibe, no devuelve
    #que hace, que recibe, que devuelve
    def LoggerJsonLoader(self, opcion, texto):
        with open(self.rutaJson,"r") as archivo_json:
            contenido= archivo_json.read()
            contenido= json.loads(contenido)
            logging.config.dictConfig(contenido)#igual hasta aqui

        log_entry= logging.getLogger("info")
        log_entry.info(opcion, extra={ "cantchar": texto})

    #que hace, que recibe, que devuelve
    def coneccion_correo (self, correo_preparado):
        try:
            #establezco parametros de la conexion    
            print("estableciendo conección")
            coneccion = smtplib.SMTP(
                host=dc.servidor,
                port= dc.puerto
                )

            #inicio conexion segura 
            coneccion.starttls()
            coneccion.login(dc.usuario, dc.clave)
            coneccion.send_message(correo_preparado)
            coneccion.quit()
            print("envío exitoso")
        except BaseException as e:
            print("coneccion_correo:", e.args[1])
        
    #verifica que el correo tenga un formato aceptable, recibe un string (email), devuelve boolean
    def verifica_correo(self, email: str):
        verify = re.search(self.pattern, email)
        return True if verify else False

    #Opcion 1
    #que hace, que recibe, que devuelve
    def agregarTexto(self, texto: str):
        
        try:
            with open(self.ruta, "a", encoding="utf") as doc:
                texto = " " + texto
                doc = doc.write(texto)
                
            self.LoggerJsonLoader ("opcion1", len(texto))

        except :
            print ("Error: abrir archivo en agregarTexto()")

    #Opcion 2
    #que hace, que recibe, que devuelve
    def mostrarTexto(self):
        texto = ""

        try:

            with open ("doc.txt", "r") as doc:
                texto = doc.read()

            self.LoggerJsonLoader ("opcion2", None)
            return texto
        
        except BaseException as e:
            print("error", e.args)

    #Opcion 3
    #que hace, que recibe, que devuelve
    def prepara_correo(self, email: str):
        texto = None
        try:
            with open ("doc.txt", "r") as doc:
                texto = doc.read()

            correo_electronico = MIMEMultipart()

            correo_electronico["To"] = email
            correo_electronico["From"] = f"<Opcion 3> {dc.usuario}"
            correo_electronico["Subject"] = "Información de texto guardado"

            cuerpo_correo = MIMEText(texto, "plain")
            correo_electronico.attach(cuerpo_correo)

            self.coneccion_correo(correo_electronico)
        except BaseException as e:
            print("prepara_correo:",e.args)

    #Opcion 4
    #que hace, que recibe, que devuelve
    def correo_info_logs(self, email):

        try:
            correo_electronico = MIMEMultipart()
            correo_electronico["To"] = email
            correo_electronico["From"] = "<Opcion 4> max.utecnica@gmail.com"
            correo_electronico["Subject"] = "Archivos del programa"
            cuerpo_correo = MIMEText("Archivos generados por la tarea programada #1", "plain")
            correo_electronico.attach(cuerpo_correo)

            for docs in self.ListaArchivos:
                
                archivo_adjunto= MIMEBase("application", "file")
                
                with open(docs,'r') as archivo:
                    archivo_adjunto.set_payload(archivo.read())
                    # encoders.encode_base64(archivo_adjunto)
                    archivo_adjunto.add_header(
                        'Content-Disposition',
                        'attachment', 
                        filename= docs
                    )
                correo_electronico.attach(archivo_adjunto)

            self.coneccion_correo(correo_electronico)

        except BaseException as e:
            print("correo_info_logs", e.args)