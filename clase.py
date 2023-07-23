class Scrap:
    id = 0

    def __init__(
        self,
        path,
        categories_eng,
        categories_esp,
        categories_port,
        name,
        description_eng,
        description_esp,
        description_port,
        prices,
        currency,
        business_model,
        keywords_eng,
        keywords_esp,
        keywords_port,
        link,
        media,
    ):
        Scrap.id += 1
        self.PropertyID = "TOOLS_" + str(Scrap.id).zfill(5)
        self.Paths = path
        self.CategoriesENG = categories_eng
        self.CategoriesESP = categories_esp
        self.CategoriesPORT = categories_port
        self.Name = name
        self.DescriptionEnglish = description_eng
        self.DescriptionSpanish = description_esp
        self.DescriptionPortuguese = description_port
        self.Prices = prices
        self.Currency = currency
        self.BusinessModel = business_model
        self.KeywordsENG = keywords_eng
        self.KeywordsESP = keywords_esp
        self.KeywordsPORT = keywords_port
        self.Link = link
        self.Media = media
