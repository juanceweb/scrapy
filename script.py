import os
import json
from clase import Scrap
from excel import guardar_diccionario_en_excel


def leer_datos_json():
    with open("datos.json", "r") as archivo:
        datos = json.load(archivo)
        print
    return datos


def escribir_datos_json(datos):
    with open("datos.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)


def crear_registro_json(registro):
    datos = leer_datos_json()
    datos.append(registro)
    escribir_datos_json(datos)


def actualizar_registro_json(indice, nuevo_registro):
    datos = leer_datos_json()
    if indice >= 0 and indice < len(datos):
        datos[indice] = nuevo_registro
        escribir_datos_json(datos)
        print("Registro actualizado correctamente.")
    else:
        print("Índice de registro inválido.")


def eliminar_registro_json(indice):
    datos = leer_datos_json()
    if indice >= 0 and indice < len(datos):
        registro_eliminado = datos.pop(indice)
        escribir_datos_json(datos)
        print("Registro eliminado correctamente.")
        return registro_eliminado
    else:
        print("Índice de registro inválido.")


# VERIFICA SI EL JSON EXISTE, SINO LO CREA CON UNA LISTA [] VACIA
def verificar_y_crear_json(nombre_archivo):
    if not os.path.isfile(nombre_archivo):
        lista_vacia = []

        with open(nombre_archivo, "w") as archivo:
            json.dump(lista_vacia, archivo)

        print("Archivo JSON creado exitosamente.")

    else:
        print("El archivo JSON ya existe.")


nombre_archivo = "datos.json"
verificar_y_crear_json(nombre_archivo)


instancia = Scrap(
    "TOOLS_000004",
    ["DESIGN"],
    ["css", "generator"],
    ["css", "generador"],
    ["css", "generador"],
    "Menu Cool",
    "Rich HTML mega menu, or unl",
    "Un mega menú HTML, menús desplega",
    "Um mega menu HTML, menus ",
    100,
    "usd",
    ["Free"],
    ["effects", "generators", "full responsive", "buttons"],
    ["effects", "generators", "full responsive", "buttons"],
    ["effects", "generators", "full responsive", "buttons"],
    "http://www.menucool.com/css-menu",
    "tiene",
)

crear_registro_json(instancia.__dict__)
guardar_diccionario_en_excel({"column_1": instancia.__dict__}, "test.xlsx")
