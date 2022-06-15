from menu import *
from modulo import *

imprimir = inicio
correo_agregar = ingresar_correo
correo_listar = getListar
correo_personalidado = personalizado_correo
correo_masivo = correo_global

##Encabezado del programa
imprimir()
opc = int(input("| ---> Ingresa una opción: "))

### Opciones del programa
## Ingresar Opción 1
if opc == 1:
    correo_agregar()

## Ingresar Opcion 2
if opc == 2:
    correo_personalidado()

## Ingresar Opcion 3
if opc == 3:
    contenido = "Muy buenas. Me presento, me llamo John Cornejo, tengo 20 años y vivo en la zona norte de Guayaquil y quisiera pertenecer a su organización. Tengo experiencia en Retail, en tiendas Tuti como Cajero, Atención al Cliente, Limpieza y Perchas, desempeñándome como Auxiliar Polifuncional durante 1 año y 8 meses, dispongo de movilización propia. Le adjunto mi curriculum. Muchas gracias"
    asunto = "Curriculum Vital John Cornejo  "
    correo_masivo(contenido, asunto)

## Ingresar Opcion 4
if opc == 4:
    correo_listar()