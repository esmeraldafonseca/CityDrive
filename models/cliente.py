# Este ficheiro define o modelo Cliente, utilizado para representar um cliente
# da CityDrive dentro da aplicação. O objeto guarda os principais dados de um
# cliente e permite transformar os resultados obtidos da base de dados em
# objetos Python. Este modelo representa os dados e não é responsável por
# executar SQL, validar regras de negócio ou construir a interface.

class Cliente:
    def __init__(self, id=None, nome="", email="", telefone=""):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone

    @classmethod
    def from_dict(cls, data):
        return cls(id=data["id"], nome=data["nome"], email=data["email"], telefone=data["telefone"])
