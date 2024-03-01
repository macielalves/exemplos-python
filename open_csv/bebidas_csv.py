import csv


class OpenCsv:
    def __init__(self, filename):
        self.filename = filename
        self.dataset = self._load_csv()
        ...

    def _load_csv(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            return list(csv.DictReader(file))


class RelatorioBebidas(OpenCsv):
    def __init__(self, file_path):
        super().__init__(file_path)

    def paises_que_nao_bebem_vinho(self):
        paises = []
        for i in self.dataset:
            if i.get("wine_servings") and float(i["wine_servings"]) == 0.0:
                paises.append(i["country"])
        return paises

    def pais_que_mais_bebe_vinho(self):
        wine_max = None
        pais = None

        for i in self.dataset:
            if wine_max is None and pais is None:
                pais, wine_max = i["country"], i["wine_servings"]
            else:
                if wine_max < i["wine_servings"]:
                    pais, wine_max = i["country"], i["wine_servings"]
        return (
            pais,
            wine_max,
        )


# ['country', 'beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']

relatorio_bebidas = RelatorioBebidas("./drinks.csv")

print(relatorio_bebidas.paises_que_nao_bebem_vinho())
print(relatorio_bebidas.pais_que_mais_bebe_vinho())
