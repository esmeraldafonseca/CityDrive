# Este ficheiro define o modelo Categoria, utilizado para representar uma
# categoria de viatura existente na CityDrive. Cada categoria possui os dados
# necessários para identificar e descrever um determinado tipo de viatura.
# O modelo serve para transportar estes dados entre as diferentes camadas da
# aplicação e não deve conter operações de acesso à base de dados.
class Categoria:
    def __init__(self, id=None, nome="", descricao=""):
        self.id = id
        self.nome = nome
        self.descricao = descricao

    @classmethod
    def from_dict(cls, data):
        return cls(id=data["id"], nome=data["nome"], descricao=data.get("descricao", ""))
