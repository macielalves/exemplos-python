class Arquivo:
    def __init__(self, nome, tipo, tamanho):
        self.__nome = nome
        self.__tipo = tipo
        self.__tamanho = tamanho

    @property
    def nome(self):
        return self.__nome

    @property
    def tipo(self):
        return self.__tipo

    @property
    def tamanho(self):
        return self.__tamanho

    def renomear(self, novo_nome):
        self.__nome = novo_nome

    def __str__(self):
        return f"{self.__nome} ( {self.__tamanho}Mb )"


class Pendrive:
    # _id = 0

    def __init__(self, id, capacidade):
        # PenDrive._id += 1
        self.__id = id
        # capacidade em megabites
        self.__espaco_livre = self.__capacidade = capacidade
        self._root_folder = {}

    @property
    def id(self):
        return self.__id

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def espaco_livre(self):
        return self.__espaco_livre

    def formatar(self):
        self._root_folder.clear()
        self.__espaco_livre = self.__capacidade
        print(
            "pendrive formatado com sucesso!",
            f"Espaço livre: {self.__espaco_livre} MB",
            sep="\n",
        )

    def listar_arquivos(self):
        return list(self._root_folder.keys())

    def adicionar_arquivo(self, __arquivo):
        if isinstance(__arquivo, Arquivo):
            if (espaco := __arquivo.tamanho) <= self.__espaco_livre:
                key = __arquivo.nome
                if not key.endswith("." + __arquivo.tipo) and __arquivo.tipo != "":
                    key = __arquivo.nome + "." + __arquivo.tipo
                self._root_folder[key] = __arquivo
                self.__espaco_livre -= espaco
                print(f"Arquivo adicionado com sucesso!")
                print(f"Espaço disponível no pendrive: {self.__espaco_livre} MB")
            else:
                print("Espaço insuficiente!")

    def apagar_arquivo(self, __arquivo):
        try:
            tamanho = self._root_folder.get(__arquivo).tamanho
            self._root_folder.pop(__arquivo)
            self.__espaco_livre += tamanho
        except AttributeError:
            print("*Arquivo inexistente")
        except KeyError:
            print("Arquivo inexistente!")
        else:
            print("Arquivo excluido com sucesso!")
            print(f"Espaço disponível no pendrive: {self.__espaco_livre} MB")

    def copiar_arquivo(self, arquivo, pendrive):
        if isinstance(pendrive, Pendrive):
            if arquivo in self._root_folder.keys():
                if arquivo not in pendrive.listar_arquivos():
                    _arquivo = self._root_folder.get(arquivo)
                    if _arquivo is not None:
                        _arquivo = Arquivo(*vars(_arquivo).values())
                        if _arquivo.tamanho <= pendrive.espaco_livre:
                            pendrive._root_folder.update({_arquivo.nome: _arquivo})
                            pendrive.__espaco_livre -= _arquivo.tamanho
                            print("Teste")
                            print("Arquivo copiado com sucesso!")
                            print(
                                f"Espaço disponível no pendrive de destino: {pendrive.__espaco_livre} MB"
                            )
                        else:
                            print("Não foi possível copiar para o pendrive de destino!")
                    else:
                        print("Nenhum arquivo para ser copiado!")
                else:
                    print("Erro! Já existe um arquivo com este nome!")
                    # opções para sobrescrever
            else:
                print("Arquivo inexistente!")
        else:
            print("Pendrive inválido!")

    def mover_arquivo(self, arquivo, pendrive):
        if isinstance(pendrive, Pendrive):
            if arquivo in self._root_folder.keys():
                if arquivo not in pendrive.listar_arquivos():
                    _arquivo = self._root_folder.get(arquivo)

                    pendrive._root_folder.update({_arquivo.nome: _arquivo})
                    del _arquivo
                else:
                    print("Erro! Já existe um arquivo com este nome!")
            else:
                print("Arquivo inexistente!")
        else:
            print("Pendrive inválido!")

    def __str__(self):
        return f"# ID: {self.id}\n# Capacidade: {self.capacidade}\n# Espaço livre: {self.__espaco_livre}"


# root = {
#     "css": {"tipo": "pasta"},
#     "img": {"tipo": "pasta"},
#     "js": {"tipo": "pasta"},
#     "index.html": {"tipo": "arquivo"},
#     "sobre.html": {"tipo": "arquivo"},
# }


pendrive1 = Pendrive(1, 1024)
pendrive2 = Pendrive(2, 512)
pendrive1.adicionar_arquivo(Arquivo("teste1.txt", "txt", 10))
# Arquivo adicionado com sucesso!
# Espaço disponivel no pendrive: 1014 MB
titanic = Arquivo("titanic.mp4", "video", 1048)
pendrive1.adicionar_arquivo(titanic)
# Espaço insuficiente!
forro_das_antigas = Arquivo("forro.mp3", "mp3", 300)
pendrive2.adicionar_arquivo(forro_das_antigas)
# Arquivo adicionado com sucesso!
# espaço disponivel no pendrive: 212 MB
pendrive2.copiar_arquivo("forro.mp3", pendrive1)
# Arquivo copiado com sucesso!
# Espaço disponível no pendrive destino: 714 MB
pendrive1.apagar_arquivo("teste1.docx")
# Arquivo inexistente!

pendrive1.apagar_arquivo("teste1.txt")
# Arquivo excluido com sucesso!
# Espaço disponivel no pendrive: 724 MB

pendrive2.mover_arquivo("forro.mp3", pendrive1)
# Erro! Já existe um arquivo com este nome!

pendrive1.formatar()
# pendrive formatado com sucesso!
# Espaço livre: 1024 MB
