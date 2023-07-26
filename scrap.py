import requests
import datetime
from excel import (
    verificar_nombre_existente,
    verificar_existencia_excel,
    crear_diccionario_en_excel,
)
from categories import generar_paths_y_categories
from deep_translator import GoogleTranslator


tool_id = 0

translator_esp = GoogleTranslator(source="auto", target="es")

translator_port = GoogleTranslator(source="auto", target="pt")


def generar_keywords(data):
    elem_keywords_eng = []
    elem_keywords_esp = []
    elem_keywords_port = []

    for elem in data:
        elem_keywords_eng.append(elem)
        elem_keywords_esp.append(translator_esp.translate(elem))
        elem_keywords_port.append(translator_port.translate(elem))

    return elem_keywords_eng, elem_keywords_esp, elem_keywords_port


def generar_descripcion(data):
    desc_eng = data
    desc_esp = translator_esp.translate(data)
    desc_port = translator_port.translate(data)

    return desc_eng, desc_esp, desc_port


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
    elif respuesta == None:
        return None

    for element in respuesta:
        desc_eng, desc_esp, desc_port = generar_descripcion(
            element["toolShortDescription"]
        )

        key_eng, key_esp, key_port = generar_keywords(element["tagsIndex"])

        if "startingPrice" in element:
            prices = element["startingPrice"].split("/mo")
            prices_mod = prices[0]
        else:
            prices_mod = ""

        media_link = generar_link_imagen(element["mainImage"]["asset"]["_ref"])

        path, cat_eng, cat_esp, cat_port = generar_paths_y_categories(
            element["toolCategories"], element["toolShortDescription"]
        )

        tool_id += 1

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
            "BusinessModel": element["pricing"],
            "KeywordsENG": key_eng,
            "KeywordsESP": key_esp,
            "KeywordsPORT": key_port,
            "Link": element["websiteUrl"],
            "Media": media_link,
        }

        if verificar_existencia_excel("tools.xlsx"):
            verificar_nombre_existente(instancia, "tools.xlsx")
        else:
            crear_diccionario_en_excel({"column_1": instancia}, "tools.xlsx")

    return True


def scrap():
    page = 1
    while True:
        url = f"https://www.futurepedia.io/api/tools?page={page}&sort=verified"
        res = scrap_website(url)

        print(page)
        ahora = datetime.datetime.now()

        print(ahora.strftime("%H:%M:%S"))

        if res == None:
            continue

        elif res == False:
            break

        page += 1
