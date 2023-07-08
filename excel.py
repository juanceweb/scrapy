import os
import pandas as pd


def guardar_diccionario_en_excel(diccionario, nombre_archivo):
    if os.path.isfile(nombre_archivo):
        # Si el archivo ya existe, cargar el contenido existente en un DataFrame
        df_existente = pd.read_excel(nombre_archivo)

        df_nuevo = pd.DataFrame.from_dict(diccionario)

        df_nuevo = df_nuevo.transpose()

        df_nuevo = df_nuevo.reindex(columns=list(diccionario["column_1"].keys()))

        df_final = pd.concat([df_existente, df_nuevo])

        # Guardar el DataFrame actualizado en el archivo Excel
        df_final.to_excel(nombre_archivo, index=False)
    else:
        # Si el archivo no existe, guardar directamente el DataFrame en el archivo Excel
        df = pd.DataFrame.from_dict(diccionario)
        # Transponer el DataFrame para que cada diccionario sea una fila
        df = df.transpose()

        df = df.reindex(columns=list(diccionario["column_1"].keys()))
        # Guardar el DataFrame en un archivo Excel
        df.to_excel(nombre_archivo, index=False)
