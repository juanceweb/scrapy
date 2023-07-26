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


def encontrar_palabras_especificas(texto_largo, palabras_a_encontrar):
    # Usamos una expresión regular para buscar todas las ocurrencias de las palabras
    # que se encuentran en la lista "palabras_a_encontrar".
    # El flag re.IGNORECASE hace que la búsqueda sea insensible a mayúsculas y minúsculas.
    patron = re.compile("|".join(palabras_a_encontrar))

    # Utilizamos findall() para obtener todas las coincidencias encontradas en el texto largo.
    coincidencias = patron.findall(texto_largo)

    return coincidencias


faltan = set()


def generar_paths_y_categories(categories, description):
    path = set()

    categories_set = set()

    categories_set.add("AI")

    for categ in categories:
        cat = categ["categoryName"]

        if cat == "image generator":
            finded = encontrar_palabras_especificas(
                description,
                lista_categorias,
            )
            for cat in finded:
                categories_set.add(cat.strip())
            categories_set.add("image")
            categories_set.add("generators")
            path.add("MARKETING")
            path.add("ARTS")
            path.add("DESIGN")

        elif cat == "art":
            finded = encontrar_palabras_especificas(
                description,
                lista_categorias,
            )
            for cat in finded:
                categories_set.add(cat.strip())
            categories_set.add("generators")
            categories_set.add("inspirations")
            path.add("ARTS")

        elif cat == "developer tools":
            finded = encontrar_palabras_especificas(
                description,
                lista_categorias,
            )
            for cat in finded:
                categories_set.add(cat.strip())
            categories_set.add("code")
            path.add("TECH")

        elif cat == "gaming":
            finded = encontrar_palabras_especificas(
                description,
                lista_categorias,
            )
            for cat in finded:
                categories_set.add(cat.strip())
            categories_set.add("games")
            path.add("TECH")
            path.add("MARKETING")
            path.add("ARTS")
            path.add("DESIGN")

        elif cat == "avatars":
            finded = encontrar_palabras_especificas(
                description,
                lista_categorias,
            )
            for cat in finded:
                categories_set.add(cat.strip())
            path.add("TECH")
            path.add("MARKETING")
            path.add("ARTS")
            path.add("DESIGN")

        elif cat == "fun tools":
            finded = encontrar_palabras_especificas(
                description,
                lista_categorias,
            )
            for cat in finded:
                categories_set.add(cat.strip())
            path.add("TECH")
            path.add("MARKETING")
            path.add("ARTS")

        elif cat == "video generator":
            finded = encontrar_palabras_especificas(
                description,
                lista_categorias,
            )
            for cat in finded:
                categories_set.add(cat.strip())
            categories_set.add("generators")
            categories_set.add("media")
            categories_set.add("content")
            categories_set.add("editors")
            path.add("MARKETING")

        elif cat == "image editing":
            finded = encontrar_palabras_especificas(
                description,
                lista_categorias,
            )
            for cat in finded:
                categories_set.add(cat.strip())
            categories_set.add("generators")
            categories_set.add("image")
            categories_set.add("content")
            categories_set.add("media")
            categories_set.add("social")
            path.add("MARKETING")
            path.add("ARTS")
            path.add("DESIGN")

        elif cat == "3D":
            finded = encontrar_palabras_especificas(
                description,
                lista_categorias,
            )
            for cat in finded:
                categories_set.add(cat.strip())
            categories_set.add("3D")
            categories_set.add("cinema")
            path.add("TECH")
            path.add("ARTS")
            path.add("DESIGN")

        elif cat == "resources":
            finded = encontrar_palabras_especificas(
                description,
                lista_categorias,
            )
            for cat in finded:
                categories_set.add(cat.strip())
            path.add("TECH")

        elif cat == "startup tools":
            categories_set.add("entrepreneur")
            categories_set.add("investing")
            path.add("BUSINESS")
            path.add("PRODUCT")

        elif cat == "audio editing":
            categories_set.add("audio")
            categories_set.add("media")
            categories_set.add("video")
            path.add("MARKETING")
            path.add("ARTS")

        elif cat == "customer support":
            categories_set.add("communication")
            path.add("SOFT SKILLS")

        elif cat == "personalized videos":
            categories_set.add("media")
            categories_set.add("content")
            categories_set.add("video")
            categories_set.add("social")
            path.add("MARKETING")
            path.add("ARTS")

        elif cat == "education assistant":
            categories_set.add("communication")
            path.add("SOFT SKILLS")

        elif cat == "code assistant":
            categories_set.add("code")
            path.add("TECH")

        elif cat == "e-commerce":
            categories_set.add("e-commerce")
            path.add("MARKETING")

        elif cat == "email assistant":
            path.add("MARKETING")

        elif cat == "text to speech":
            categories_set.add("communication")
            path.add("MARKETING")

        elif cat == "prompts":
            categories_set.add("code")
            path.add("TECH")
            path.add("DATA")

        elif cat == "finance":
            categories_set.add("finance")
            path.add("BUSINESS")

        elif cat == "presentations":
            categories_set.add("communication")
            path.add("SOFT SKILLS")

        elif cat == "video editing":
            categories_set.add("media")
            categories_set.add("video")
            path.add("MARKETING")
            path.add("ARTS")

        elif cat == "human resources":
            categories_set.add("HR")
            path.add("SOFT SKILLS")

        elif cat == "fitness":
            path.add("TECH")
            path.add("SOFT SKILLS")

        elif cat == "social media assistant":
            categories_set.add("social")
            path.add("MARKETING")

        elif cat == "general writing":
            categories_set.add("copywriting")
            categories_set.add("cinema")
            path.add("MARKETING")
            path.add("ARTS")

        elif cat == "storytelling":
            categories_set.add("copywriting")
            categories_set.add("cinema")
            path.add("MARKETING")
            path.add("ARTS")

        elif cat == "design assistant":
            path.add("DESIGN")
            path.add("TECH")

        elif cat == "search engine":
            path.add("TECH")

        elif cat == "music":
            categories_set.add("video")
            categories_set.add("audio")
            path.add("ARTS")
            path.add("MARKETING")

        elif cat == "spreadsheets":
            path.add("DATA")

        elif cat == "low-code/no-code":
            categories_set.add("no code")
            path.add("PRODUCT")

        elif cat == "copywriting":
            categories_set.add("copywriting")
            categories_set.add("cinema")
            path.add("MARKETING")
            path.add("ARTS")

        elif cat == "life assistant":
            path.add("TECH")

        elif cat == "transcriber":
            path.add("DATA")

        elif cat == "logo generator":
            categories_set.add("generators")
            categories_set.add("image")
            path.add("DESIGN")

        elif cat == "research":
            categories_set.add("database")
            categories_set.add("analytics")
            path.add("DATA")

        elif cat == "SEO":
            categories_set.add("SEO")
            path.add("MARKETING")

        elif cat == "SQL":
            categories_set.add("code")
            categories_set.add("database")
            path.add("TECH")

        elif cat == "sales":
            categories_set.add("accounting")
            path.add("BUSINESS")

        elif cat == "productivity":
            categories_set.add("productivity")
            path.add("PRODUCT")
            path.add("SOFT SKILLS")

        elif cat == "healthcare":
            path.add("SOFT SKILLS")

        elif cat == "dating":
            categories_set.add("social")
            path.add("MARKETING")

        elif cat == "fashion":
            categories_set.add("fashion")
            path.add("DESIGN")

        elif (
            cat == "summarizer"
            or cat == "religion"
            or cat == "experiments"
            or cat == "real estate"
            or cat == "paraphraser"
            or cat == "gift ideas"
            or cat == "travel"
            or cat == "memory"
            or cat == "legal assistant"
        ):
            pass

        # else:
        #     faltan.add(cat)

    path = list(path)

    categories_list = list(categories_set)

    categories_esp_list = ["IA"]

    categories_port_list = ["IA"]

    for category in categories_list:
        if category != "AI":
            indice = lista_categorias.index(category)
            categories_esp_list.append(lista_categorias_espanol[indice])
            categories_port_list.append(lista_categorias_portugues[indice])

    return path, categories_list, categories_esp_list, categories_port_list
