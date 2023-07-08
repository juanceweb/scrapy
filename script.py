import json


def leer_datos():
    with open("datos.json", "r") as archivo:
        datos = json.load(archivo)
    return datos


def escribir_datos(datos):
    with open("datos.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)


def crear_registro(registro):
    datos = leer_datos()
    datos.append(registro)
    escribir_datos(datos)


def leer_registros():
    datos = leer_datos()
    for registro in datos:
        print(registro)


def actualizar_registro(indice, nuevo_registro):
    datos = leer_datos()
    if indice >= 0 and indice < len(datos):
        datos[indice] = nuevo_registro
        escribir_datos(datos)
        print("Registro actualizado correctamente.")
    else:
        print("Índice de registro inválido.")


def eliminar_registro(indice):
    datos = leer_datos()
    if indice >= 0 and indice < len(datos):
        registro_eliminado = datos.pop(indice)
        escribir_datos(datos)
        print("Registro eliminado correctamente.")
        return registro_eliminado
    else:
        print("Índice de registro inválido.")


# Ejemplo de uso
crear_registro({"nombre": "Ejemplo 1", "edad": 25, "ciudad": "Ciudad 1"})
crear_registro({"nombre": "Ejemplo 2", "edad": 30, "ciudad": "Ciudad 2"})
leer_registros()

actualizar_registro(
    0, {"nombre": "Nuevo Ejemplo", "edad": 27, "ciudad": "Ciudad Nueva"}
)

registro_eliminado = eliminar_registro(1)
if registro_eliminado:
    print("Registro eliminado:", registro_eliminado)
