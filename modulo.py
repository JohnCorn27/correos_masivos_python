from archivos import *
from correo import *
agregar = crearArchivo
correo_personalizado = correo

def ingresar_correo():
    empresa = input("Ingresa el nombre de la empresa")
    correo = input("Ingresar el correo de la empresa")
    obj = (empresa, correo)
    __grabar(obj)

def __grabar(obj):
    msg = str(obj[0]) + ";" + obj[1] + ";\n"
    agregar("correo.csv", msg, "a")

def getListar():
    lista = leerArchivo("correo.csv")
    print("*-*-* Vamos a enlistar todos los datos *-*-*\n")
    for i in range(len(lista)) :
        print("Correo Numero",i)
        print("-- Empresa: " + lista[i][0] + "\n-- Correo: " + lista[i][1]+"\n")

def personalizado_correo():
    correo = input("Ingresa el correo")
    asunto = input("Ingresa el asunto")
    contenido = input("Ingresa el contenido")
    correo_personalizado(contenido, correo, asunto)

def correo_global(contenido, asunto):
    lista = leerArchivo("correo.csv")
    for i in range(len(lista)):
        correo_personalizado(contenido, lista[i][1], asunto)

