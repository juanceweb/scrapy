import pandas as pd
import numpy as np
import ast
import json


def parse_array(string):
    try:
        # Intentamos analizar el string como una expresión de Python
        parsed = ast.literal_eval(string)

        # Verificamos si el resultado es una lista
        if isinstance(parsed, list):
            return parsed
        else:
            return None
    except (ValueError, SyntaxError):
        # Si ocurre un error al analizar el string, o no es una lista, retornamos None
        return None


def limpiar_datos(dato):
    nuevo = {}
    for x, y in dato.items():
        z = parse_array(y)
        if z is not None:
            nuevo[x] = z
        else:
            nuevo[x] = y

    return nuevo


def excel_a_json(archivo_excel, archivo_json):
    try:
        # Leer el archivo Excel en un DataFrame
        df = pd.read_excel(archivo_excel)

        df = df.replace({np.nan: ""})

        # Convertir el DataFrame a un diccionario
        datos = df.to_dict(orient="records")

        datos_new = []

        for dato in datos:
            datos_new.append(limpiar_datos(dato))

        # Escribir el diccionario en un archivo JSON
        with open(archivo_json, "w", encoding="utf-8") as archivo:
            # archivo.write(pd.Series(datos_new).to_json(orient="records", indent=4))
            json.dump(datos_new, archivo, indent=4, ensure_ascii=False)

        print("El archivo JSON se ha creado correctamente.")
    except FileNotFoundError:
        print("El archivo Excel no se encuentra.")
    except Exception as e:
        print("Error al procesar el archivo Excel:", e)


# Ejemplo de uso


# def leer_datos_json():
#     with open("datos.json", "r") as archivo:
#         datos = json.load(archivo)
#         print
#     return datos


# def escribir_datos_json(datos):
#     with open("datos.json", "w") as archivo:
#         json.dump(datos, archivo, indent=4)


# def crear_registro_json(registro):
#     datos = leer_datos_json()
#     datos.append(registro)
#     escribir_datos_json(datos)


# def actualizar_registro_json(indice, nuevo_registro):
#     datos = leer_datos_json()
#     if indice >= 0 and indice < len(datos):
#         datos[indice] = nuevo_registro
#         escribir_datos_json(datos)
#         print("Registro actualizado correctamente.")
#     else:
#         print("Índice de registro inválido.")


# def eliminar_registro_json(indice):
#     datos = leer_datos_json()
#     if indice >= 0 and indice < len(datos):
#         registro_eliminado = datos.pop(indice)
#         escribir_datos_json(datos)
#         print("Registro eliminado correctamente.")
#         return registro_eliminado
#     else:
#         print("Índice de registro inválido.")


# # VERIFICA SI EL JSON EXISTE, SINO LO CREA CON UNA LISTA [] VACIA
# def verificar_y_crear_json(nombre_archivo):
#     if not os.path.isfile(nombre_archivo):
#         lista_vacia = []

#         with open(nombre_archivo, "w") as archivo:
#             json.dump(lista_vacia, archivo)

#         print("Archivo JSON creado exitosamente.")

#     else:
#         print("El archivo JSON ya existe.")


# nombre_archivo = "datos.json"
# verificar_y_crear_json(nombre_archivo)
