# Este ficheiro define o modelo Viatura, utilizado para representar uma viatura
# da frota CityDrive. Para além dos seus dados próprios, como matrícula, marca,
# modelo e ano, uma viatura está relacionada com uma categoria e uma estação.
# Alguns atributos permitem ainda guardar informação obtida através de consultas
# com JOIN, facilitando a apresentação dos dados nas restantes camadas.

class Viatura:
    def __init__(self, id=None, matricula="", marca="", modelo="", categoria_id=None, ano=None, estacao_id=None, ativa=True, categoria_nome="", estacao_nome="", cidade=""):
        self.id = id
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.categoria_id = categoria_id
        self.ano = ano
        self.estacao_id = estacao_id
        self.ativa = ativa
        self.categoria_nome = categoria_nome
        self.estacao_nome = estacao_nome
        self.cidade = cidade

    @classmethod
    def from_dict(cls, data):
        return cls(id=data["id"], matricula=data["matricula"], marca=data["marca"], modelo=data["modelo"], categoria_id=data["categoria_id"], ano=data["ano"], estacao_id=data["estacao_id"], ativa=data["ativa"], categoria_nome=data.get("categoria_nome", ""), estacao_nome=data.get("estacao_nome", ""), cidade=data.get("cidade", ""))
