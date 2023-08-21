import requests
import datetime
import re
from excel import (
    verificar_existente_identico,
    verificar_existencia_excel,
    crear_diccionario_en_excel,
    actualizar_fila_excel,
    guardar_diccionario_en_excel,
)
from categories import generar_paths_y_categories, generar_categories_esp_port
from deep_translator import GoogleTranslator


tool_id = 0

translator_esp = GoogleTranslator(source="auto", target="es")

translator_port = GoogleTranslator(source="auto", target="pt")


def generar_keywords(data):
    elem_keywords_eng = []

    for elem in data:
        elem_keywords_eng.append(elem["categoryName"])

    return elem_keywords_eng


def generar_keywords_esp_port(key_eng):
    elem_keywords_esp = []
    elem_keywords_port = []

    for elem in key_eng:
        elem_keywords_esp.append(translator_esp.translate(elem))
        elem_keywords_port.append(translator_port.translate(elem))

    return elem_keywords_esp, elem_keywords_port


def generar_descripcion_esp_port(desc_eng):
    desc_esp = translator_esp.translate(desc_eng)
    desc_port = translator_port.translate(desc_eng)

    return desc_esp, desc_port


def generar_precio(data: str):
    data = data.lower()
    index_1 = data.find("/")
    if index_1 != -1:
        data = data[:index_1]

    index_2 = data.find("per")
    if index_2 != -1:
        data = data[:index_2]

    index_3 = data.find("one-time")
    if index_3 != -1:
        data = data[:index_3]

    index_start = re.search(r"\d", data).start()
    data = data[index_start:]

    index_4 = data.find("$")
    if index_4 != -1:
        data = data[:index_4]

    return "$" + data


def generar_link_imagen(element):
    img_link = element
    img_link = img_link.replace("image-", "")

    posicion_guion = img_link.rfind("-")
    if posicion_guion != -1:
        # Reemplazar el guión por un punto "."
        img_link = img_link[:posicion_guion] + "." + img_link[posicion_guion + 1 :]

    return "https://cdn.sanity.io/images/u0v1th4q/production/" + img_link


def hacer_pedido_get(url):
    try:
        response = requests.get(url, timeout=20)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(
                f"Error en la solicitud GET. Código de estado: {response.status_code}"
            )
            return None
    except requests.exceptions.RequestException as e:
        print("Error de conexión:", e)
        return None


def scrap_website(url):
    global tool_id
    respuesta = hacer_pedido_get(url)

    if respuesta == []:
        return False
    elif respuesta is None:
        return None

    for element in respuesta:
        # GENERAMOS DESCRIPCION INGLES
        if "toolShortDescription" in element:
            desc_eng = element["toolShortDescription"]
        else:
            desc_eng = ""

        # GENERAMOS KEYWORDS INGLES
        if "toolCategories" in element:
            key_eng = generar_keywords(element["toolCategories"])
        else:
            key_eng = generar_keywords("")

        # GENERAMOS PRECIOS
        if "startingPrice" in element:
            price = element["startingPrice"]

            if price.lower() != "" and price.lower() != "free":
                if price != 0 and price != "0":
                    prices_mod = generar_precio(price)
                else:
                    prices_mod = ""
            else:
                prices_mod = ""
        else:
            prices_mod = ""

        # GENERAMOS IMAGEN
        if "mainImage" in element:
            media_link = generar_link_imagen(element["mainImage"]["asset"]["_ref"])
        else:
            media_link = "no image"

        # GENERAMOS CATEGORIAS Y PATH INGLES
        if "toolCategories" in element:
            path, cat_eng = generar_paths_y_categories(
                element["toolCategories"], desc_eng
            )
        else:
            path, cat_eng = generar_paths_y_categories("", desc_eng)

        # GENERAMOS TOOL ID
        tool_id += 1

        # GENERAMOS PRICING
        if "pricing" in element:
            price = element["pricing"]
        else:
            price = ""

        # YA ESTA CREADO EL EXCEL O NO
        existe_excel = verificar_existencia_excel("tools.xlsx")

        # CHEQUEA SI LA TOOL EN CUESTION YA EXISTE EN EL EXCEL Y NO TUBO CAMBIOS
        if existe_excel:
            ya_existe_tool, indice = verificar_existente_identico(
                element["toolName"],
                path,
                cat_eng,
                desc_eng,
                prices_mod,
                price,
                key_eng,
                element["websiteUrl"],
                media_link,
                "tools.xlsx",
            )
        else:
            ya_existe_tool = "NO EXISTE"
            indice = False

        if ya_existe_tool == "NO EXISTE" or ya_existe_tool == "CAMBIOS":
            cat_esp, cat_port = generar_categories_esp_port(cat_eng)
            desc_esp, desc_port = generar_descripcion_esp_port(desc_eng)
            key_esp, key_port = generar_keywords_esp_port(key_eng)

            instancia = {
                "PropertyID": "TOOLS_" + str(tool_id).zfill(5),
                "Paths": path,
                "CategoriesENG": cat_eng,
                "CategoriesESP": cat_esp,
                "CategoriesPORT": cat_port,
                "Name": element["toolName"],
                "DescriptionEnglish": desc_eng,
                "DescriptionSpanish": desc_esp,
                "DescriptionPortuguese": desc_port,
                "Prices": prices_mod,
                "Currency": "usd",
                "BusinessModel": price,
                "KeywordsENG": key_eng,
                "KeywordsESP": key_esp,
                "KeywordsPORT": key_port,
                "Link": element["websiteUrl"],
                "Media": media_link,
            }

            if existe_excel:
                if indice:
                    actualizar_fila_excel(indice, instancia, "tools.xlsx")
                else:
                    guardar_diccionario_en_excel({"column_1": instancia}, "tools.xlsx")
            else:
                crear_diccionario_en_excel({"column_1": instancia}, "tools.xlsx")

    return True


def scrap():
    page = 1
    while True:
        url = f"https://www.futurepedia.io/api/tools?page={page}&sort=verified"
        res = scrap_website(url)

        ahora = datetime.datetime.now()
        print(f"page = {page} hora = {ahora.strftime('%H:%M:%S')}")

        if res is None:
            continue

        elif res is False:
            break

        page += 1
