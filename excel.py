import os
import pandas as pd
from openpyxl import load_workbook


def crear_diccionario_en_excel(instancia_diccionario, nombre_archivo):
    # Si el archivo no existe, guardar directamente el DataFrame en el archivo Excel

    df = pd.DataFrame.from_dict(instancia_diccionario)
    # Transponer el DataFrame para que cada diccionario sea una fila
    df = df.transpose()

    df = df.reindex(columns=list(instancia_diccionario["column_1"].keys()))
    # Guardar el DataFrame en un archivo Excel
    df.to_excel(nombre_archivo, index=False)

    print(f"Se creo el Excel, junto con una nueva fila")


def obtener_ultima_fila_con_informacion(nombre_archivo, nombre_columna):
    # Cargar el archivo de Excel
    df = pd.read_excel(nombre_archivo)

    value = df[nombre_columna].notna().sum()

    return value


def guardar_diccionario_en_excel(instancia_diccionario, nombre_archivo):
    # Si el archivo ya existe, cargar el contenido existente en un DataFrame

    id = obtener_ultima_fila_con_informacion(nombre_archivo, "PropertyID")

    nuevo_id = id + 1

    instancia_diccionario["column_1"]["PropertyID"] = "TOOLS_" + str(nuevo_id).zfill(5)

    df_existente = pd.read_excel(nombre_archivo)

    df_nuevo = pd.DataFrame.from_dict(instancia_diccionario)

    df_nuevo = df_nuevo.transpose()

    df_nuevo = df_nuevo.reindex(columns=list(instancia_diccionario["column_1"].keys()))

    df_final = pd.concat([df_existente, df_nuevo])

    # Guardar el DataFrame actualizado en el archivo Excel
    df_final.to_excel(nombre_archivo, index=False)

    print(f"Se creo una nueva fila del Excel")


def actualizar_fila_excel(fila, nueva_data, nombre_archivo):
    try:
        fila += 2

        # Cargar el archivo Excel existente
        book = load_workbook(nombre_archivo)

        # Seleccionar la hoja de trabajo
        hoja = book.active

        # Actualizar la fila con la nueva data
        for i, valor in enumerate(nueva_data.values(), start=1):
            if i != 1:
                if type(valor) == list:
                    valor = str(valor)
                hoja.cell(row=fila, column=i).value = valor

        # Guardar los cambios en el archivo Excel
        book.save(nombre_archivo)

        print(f"Se actualizo la fila {fila} del Excel")

    except FileNotFoundError:
        print("El archivo Excel no se encuentra.")
    except Exception as e:
        print("Error al procesar el archivo Excel:", e)


def verificar_nombre_existente(instancia_diccionario, nombre_archivo):
    try:
        df = pd.read_excel(nombre_archivo)

        nombre_existente = df.loc[df["Name"] == instancia_diccionario["Name"]]

        filas = nombre_existente.index.to_list()

        if len(filas) == 0:
            guardar_diccionario_en_excel(
                {"column_1": instancia_diccionario}, nombre_archivo
            )
        else:
            actualizar_fila_excel(filas[0], instancia_diccionario, nombre_archivo)

    except FileNotFoundError:
        print("El archivo Excel no se encuentra.")
    except Exception as e:
        print("Error al procesar el archivo Excel:", e)


def verificar_existencia_excel(nombre_archivo):
    return os.path.isfile(nombre_archivo)
