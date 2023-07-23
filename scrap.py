import requests
from clase import Scrap
from excel import (
    verificar_nombre_existente,
    verificar_existencia_excel,
    crear_diccionario_en_excel,
)

from translate import Translator
from deep_translator import GoogleTranslator


def translate_text(text, dest_lang):
    translated = GoogleTranslator(source="auto", target=dest_lang).translate(text)
    return translated


def generar_categories(data):
    elem_keywords_eng = []
    elem_keywords_esp = []
    elem_keywords_port = []

    for elem in data:
        key = elem["categoryName"]
        elem_keywords_eng.append(key)
        key_esp = translate_text(key, "es")
        elem_keywords_esp.append(key_esp)
        key_port = translate_text(key, "pt")
        elem_keywords_port.append(key_port)

    return elem_keywords_eng, elem_keywords_esp, elem_keywords_port


def generar_keywords(data):
    elem_keywords_eng = []
    elem_keywords_esp = []
    elem_keywords_port = []

    for elem in data:
        elem_keywords_eng.append(elem)
        key_esp = translate_text(elem, "es")
        elem_keywords_esp.append(key_esp)
        key_port = translate_text(elem, "pt")
        elem_keywords_port.append(key_port)

    return elem_keywords_eng, elem_keywords_esp, elem_keywords_port


def generar_descripcion(data):
    desc_eng = data
    desc_esp = translate_text(data, "es")
    desc_port = translate_text(data, "pt")

    return desc_eng, desc_esp, desc_port


def hacer_pedido_get(url):
    try:
        # Realizar la solicitud GET
        response = requests.get(url)

        # Verificar el código de estado de la respuesta
        if response.status_code == 200:
            # La solicitud fue exitosa
            data = response.json()  # Convertir la respuesta a JSON
            return data
        else:
            # La solicitud no fue exitosa
            print(
                f"Error en la solicitud GET. Código de estado: {response.status_code}"
            )
            return None
    except requests.exceptions.RequestException as e:
        print("Error de conexión:", e)
        return None


def generar_link_imagen(element):
    base_link = "https://cdn.sanity.io/images/u0v1th4q/production/"

    img_link = element
    img_link = img_link.replace("image-", "")

    posicion_guion = img_link.rfind("-")
    if posicion_guion != -1:
        # Reemplazar el guión por un punto "."
        img_link = img_link[:posicion_guion] + "." + img_link[posicion_guion + 1 :]

    return "https://cdn.sanity.io/images/u0v1th4q/production/" + img_link


def generar_paths(categories):
    path = set()

    for cat in categories:
        if cat in [
            "3D",
            "AI",
            "AR",
            "authentication",
            "code",
            "crypto",
            "database",
            "extensions",
            "games",
            "hosting",
            "integrations",
            "NFT",
            "privacy",
            "QA",
            "security",
            "VR",
        ]:
            path.add("TECHNOLOGY")
        if cat in [
            "3D",
            "animation",
            "audio",
            "content",
            "editors",
            "games",
            "generators",
            "NFT",
            "video",
            "VR",
        ]:
            path.add("ARTS")
        if cat in [
            "3D",
            "colors",
            "editors",
            "fonts",
            "games",
            "generators",
            "icons",
            "image",
            "inspirations",
            "shadow",
            "UX - UI",
        ]:
            path.add("DESIGN")
        if cat in [
            "accounting",
            "crypto",
            "entrepreneur",
            "finance",
            "HR",
            "investing",
        ]:
            path.add("BUSINESS")
        if cat in ["analytics", "monitoring"]:
            path.add("DATA")
        if cat in [
            "branding",
            "content",
            "copywriting",
            "creators",
            "e-commerce",
            "editors",
            "generators",
            "media",
            "SEO",
            "social",
        ]:
            path.add("MARKETING")
        if cat in ["communication", "HR", "productivity"]:
            path.add("SOFT SKILLS")
        if cat in [
            "editors",
            "frameworks",
            "generators",
            "mockups",
            "no code",
            "productivity",
        ]:
            path.add("PRODUCT")

    path = list(path)

    return path


def scrap_website(url):
    respuesta = hacer_pedido_get(url)

    for element in respuesta:
        cat_eng, cat_esp, cat_port = generar_categories(element["toolCategories"])

        desc_eng, desc_esp, desc_port = generar_descripcion(
            element["toolShortDescription"]
        )

        key_eng, key_esp, key_port = generar_keywords(element["tagsIndex"])

        if "socialLinks" in element:
            media_links = element["socialLinks"]
        else:
            media_links = ""

        if "startingPrice" in element:
            prices = element["startingPrice"].split("/mo")
            prices_mod = prices[0]
        else:
            prices_mod = ""

        media_link = generar_link_imagen(element["mainImage"]["asset"]["_ref"])

        path = generar_paths(cat_eng)

        instancia = Scrap(
            path=path,
            categories_eng=cat_eng,
            categories_esp=cat_esp,
            categories_port=cat_port,
            name=element["toolName"],
            description_eng=desc_eng,
            description_esp=desc_esp,
            description_port=desc_port,
            prices=prices_mod,
            currency="usd",
            business_model=element["pricing"],
            keywords_eng=key_eng,
            keywords_esp=key_esp,
            keywords_port=key_port,
            link=element["websiteUrl"],
            media=media_link,
        )

        if verificar_existencia_excel("tools.xlsx"):
            verificar_nombre_existente(instancia.__dict__, "tools.xlsx")
        else:
            crear_diccionario_en_excel({"column_1": instancia.__dict__}, "tools.xlsx")


def scrap(vueltas):
    for x in range(1, vueltas):
        url = f"https://www.futurepedia.io/api/tools?page={x}&sort=verified"
        scrap_website(url)
