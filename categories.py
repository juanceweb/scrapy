import re

lista_categorias = [
    "3D",
    "accounting",
    "analytics",
    "animation",
    "AR",
    "audio",
    "authentication",
    "boards",
    "branding",
    "cinema",
    "code",
    "colors",
    "communication",
    "content",
    "copywriting",
    "creators",
    "crypto",
    "database",
    "documentary",
    "e-books",
    "e-commerce",
    "editors",
    "entrepreneur",
    "extensions",
    "finance",
    "fonts",
    "frameworks",
    "games",
    "generators",
    "hosting",
    "HR",
    "icons",
    "image",
    "inspirations",
    "integrations",
    "investing",
    "media",
    "mockups",
    "monitoring",
    "NFT",
    "no code",
    "podcast",
    "privacy",
    "productivity",
    "QA",
    "security",
    "SEO",
    "shadow",
    "social",
    "UX - UI",
    "video",
    "VR",
    "fashion",
]

lista_categorias_espanol = [
    "3D",
    "contabilidad",
    "analítica",
    "animación",
    "AR",  # Realidad Aumentada
    "audio",
    "autenticación",
    "tableros",
    "marca",
    "cine",
    "código",
    "colores",
    "comunicación",
    "contenido",
    "redacción",
    "creadores",
    "cripto",  # Criptomonedas
    "base de datos",
    "documental",
    "e-books",  # Libros electrónicos
    "e-commerce",  # Comercio electrónico
    "editores",
    "emprendedor",
    "extensiones",
    "finanzas",
    "fuentes",
    "frameworks",  # Marcos de trabajo
    "juegos",
    "generadores",
    "hosting",
    "RRHH",  # Recursos Humanos
    "iconos",
    "imagen",
    "inspiraciones",
    "integraciones",
    "inversiones",
    "medios",
    "mockups",
    "monitoreo",
    "NFT",  # Tokens no fungibles
    "no code",  # Sin programación
    "podcast",
    "privacidad",
    "productividad",
    "QA",  # Control de calidad
    "seguridad",
    "SEO",  # Optimización para motores de búsqueda
    "sombra",
    "social",
    "UX - UI",  # Experiencia de Usuario - Interfaz de Usuario
    "video",
    "VR",  # Realidad Virtual
    "moda",
]

lista_categorias_portugues = [
    "3D",
    "contabilidade",
    "análises",
    "animação",
    "AR",  # Realidade Aumentada
    "áudio",
    "autenticação",
    "quadros",
    "branding",
    "cinema",
    "código",
    "cores",
    "comunicação",
    "conteúdo",
    "copywriting",
    "criadores",
    "cripto",  # Criptomoedas
    "banco de dados",
    "documentário",
    "e-books",  # Livros eletrônicos
    "e-commerce",  # Comércio eletrônico
    "editores",
    "empreendedor",
    "extensões",
    "finanças",
    "fontes",
    "frameworks",  # Estruturas
    "jogos",
    "geradores",
    "hospedagem",
    "RH",  # Recursos Humanos
    "ícones",
    "imagem",
    "inspirações",
    "integrações",
    "investimentos",
    "mídia",
    "mockups",
    "monitoramento",
    "NFT",  # Tokens não fungíveis
    "no code",  # Sem programação
    "podcast",
    "privacidade",
    "produtividade",
    "QA",  # Controle de Qualidade
    "segurança",
    "SEO",  # Otimização para mecanismos de busca
    "sombra",
    "social",
    "UX - UI",  # Experiência do Usuário - Interface do Usuário
    "vídeo",
    "RV",  # Realidade Virtual
    "moda",
]

cat_faltan = set()


def encontrar_palabras_especificas(texto_largo, palabras_a_encontrar):
    # Usamos una expresión regular para buscar todas las ocurrencias de las palabras
    # que se encuentran en la lista "palabras_a_encontrar".
    # El flag re.IGNORECASE hace que la búsqueda sea insensible a mayúsculas y minúsculas.
    patron = re.compile("|".join(palabras_a_encontrar))

    # Utilizamos findall() para obtener todas las coincidencias encontradas en el texto largo.
    coincidencias = patron.findall(texto_largo)

    return coincidencias


def generar_paths_y_categories(categories, description):
    categories_set = set()
    categories_set.add("AI")

    path = set()

    for categ in categories:
        cat = categ["categoryName"]

        match cat:
            case "image generator":
                finded = encontrar_palabras_especificas(description, lista_categorias)
                categories_set.update(cat.strip() for cat in finded)
                categories_set.update(["image", "generators"])
                path.update(["MARKETING", "ARTS", "DESIGN"])

            case "art":
                finded = encontrar_palabras_especificas(description, lista_categorias)
                categories_set.update(cat.strip() for cat in finded)
                categories_set.update(["generators", "inspirations"])
                path.add("ARTS")

            case "developer tools":
                finded = encontrar_palabras_especificas(description, lista_categorias)
                categories_set.update(cat.strip() for cat in finded)
                categories_set.add("code")
                path.add("TECH")

            case "gaming":
                finded = encontrar_palabras_especificas(description, lista_categorias)
                categories_set.update(cat.strip() for cat in finded)
                categories_set.update(["games"])
                path.update(["TECH", "MARKETING", "ARTS", "DESIGN"])

            case "avatars":
                finded = encontrar_palabras_especificas(description, lista_categorias)
                categories_set.update(cat.strip() for cat in finded)
                path.update(["TECH", "MARKETING", "ARTS", "DESIGN"])

            case "fun tools":
                finded = encontrar_palabras_especificas(description, lista_categorias)
                categories_set.update(cat.strip() for cat in finded)
                path.update(["TECH", "MARKETING", "ARTS"])

            case "video generator":
                finded = encontrar_palabras_especificas(description, lista_categorias)
                categories_set.update(cat.strip() for cat in finded)
                categories_set.update(["generators", "media", "content", "editors"])
                path.add("MARKETING")

            case "video generator":
                finded = encontrar_palabras_especificas(description, lista_categorias)
                categories_set.update(cat.strip() for cat in finded)
                categories_set.update(["generators", "media", "content", "editors"])
                path.add("MARKETING")

            case "image editing":
                finded = encontrar_palabras_especificas(description, lista_categorias)
                categories_set.update(cat.strip() for cat in finded)
                categories_set.update(
                    ["generators", "image", "content", "media", "social"]
                )
                path.update(["DESIGN", "MARKETING", "ARTS"])

            case "3D":
                finded = encontrar_palabras_especificas(description, lista_categorias)
                categories_set.update(cat.strip() for cat in finded)
                categories_set.update(["3D", "cinema"])
                path.update(["TECH", "DESIGN", "ARTS"])

            case "resources":
                finded = encontrar_palabras_especificas(description, lista_categorias)
                categories_set.update(cat.strip() for cat in finded)
                path.add("TECH")

            case "startup tools":
                categories_set.update(["entrepreneur", "investing"])
                path.update(["BUSINESS", "PRODUCT"])

            case "audio editing":
                categories_set.update(["audio", "media", "video"])
                path.update(["MARKETING", "ARTS"])

            case "customer support":
                categories_set.add("communication")
                path.add("SOFT SKILLS")

            case "personalized videos":
                categories_set.update(["media", "content", "video", "social"])
                path.update(["MARKETING", "ARTS"])

            case "education assistant":
                categories_set.add("communication")
                path.add("SOFT SKILLS")

            case "code assistant":
                categories_set.add("code")
                path.add("TECH")

            case "e-commerce":
                categories_set.add("e-commerce")
                path.add("MARKETING")

            case "email assistant":
                path.add("MARKETING")

            case "text to speech":
                categories_set.add("communication")
                path.add("MARKETING")

            case "prompts":
                categories_set.add("code")
                path.update(["TECH", "DATA"])

            case "finance":
                categories_set.add("finance")
                path.add("BUSINESS")

            case "presentations":
                categories_set.add("communication")
                path.add("SOFT SKILLS")

            case "video editing":
                categories_set.update(["media", "video"])
                path.update(["MARKETING", "ARTS"])

            case "human resources":
                categories_set.add("HR")
                path.add("SOFT SKILLS")

            case "fitness":
                path.update(["TECH", "SOFT SKILLS"])

            case "social media assistant":
                categories_set.add("social")
                path.add("MARKETING")

            case "general writing":
                categories_set.update(["copywriting", "cinema"])
                path.update(["MARKETING", "ARTS"])

            case "story teller":
                categories_set.update(["copywriting", "cinema"])
                path.update(["MARKETING", "ARTS"])

            case "design assistant":
                path.update(["DESIGN", "TECH"])

            case "search engine":
                path.add("TECH")

            case "music":
                categories_set.update(["video", "audio"])
                path.update(["ARTS", "MARKETING"])

            case "spreadsheets":
                path.add("DATA")

            case "low-code/no-code":
                categories_set.add("no code")
                path.add("PRODUCT")

            case "copywriting":
                categories_set.update(["copywriting", "cinema"])
                path.update(["MARKETING", "ARTS"])

            case "life assistant":
                path.add("TECH")

            case "transcriber":
                path.add("DATA")

            case "logo generator":
                categories_set.update(["generators", "image"])
                path.add("DESIGN")

            case "research":
                categories_set.update(["database", "analytics"])
                path.add("DATA")

            case "SEO":
                categories_set.add("SEO")
                path.add("MARKETING")

            case "SQL":
                categories_set.update(["code", "database"])
                path.add("TECH")

            case "sales":
                categories_set.add("accounting")
                path.add("BUSINESS")

            case "productivity":
                categories_set.add("productivity")
                path.update(["PRODUCT", "SOFT SKILLS"])

            case "healthcare":
                path.add("SOFT SKILLS")

            case "dating":
                categories_set.add("social")
                path.add("MARKETING")

            case "fashion":
                categories_set.add("fashion")
                path.add("DESIGN")

            case "summarizer", "religion", "experiments", "real estate", "paraphraser", "gift ideas", "travel", "memory", "legal assistant":
                pass

            case _:  # Caso por defecto si no coincide con ninguno de los casos anteriores
                cat_faltan.add(cat)

    categories_list = list(categories_set)
    categories_esp_list = ["IA"]
    categories_port_list = ["IA"]

    for category in categories_list:
        if category != "AI":
            indice = lista_categorias.index(category)
            categories_esp_list.append(lista_categorias_espanol[indice])
            categories_port_list.append(lista_categorias_portugues[indice])

    return list(path), categories_list, categories_esp_list, categories_port_list
