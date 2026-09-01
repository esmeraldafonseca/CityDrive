# Este ficheiro define o modelo Estacao, utilizado para representar uma estação
# da CityDrive. Uma estação possui uma localização, uma cidade, um horário de
# funcionamento e um estado que indica se está ativa. Estes dados são também
# importantes para as reservas, uma vez que uma viatura está associada a uma
# estação e o período reservado deve respeitar as regras definidas para ela.
class Estacao:
    def __init__(self, id=None, nome="", morada="", cidade="", hora_abertura=None, hora_fecho=None, ativa=True):
        self.id = id
        self.nome = nome
        self.morada = morada
        self.cidade = cidade
        self.hora_abertura = hora_abertura
        self.hora_fecho = hora_fecho
        self.ativa = ativa

    @classmethod
    def from_dict(cls, data):
        return cls(id=data["id"], nome=data["nome"], morada=data["morada"], cidade=data["cidade"], hora_abertura=data["hora_abertura"], hora_fecho=data["hora_fecho"], ativa=data["ativa"])
