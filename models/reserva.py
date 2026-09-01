# Este ficheiro define o modelo Reserva, utilizado para representar a reserva
# de uma viatura por um cliente durante um determinado período. A reserva
# relaciona um cliente com uma viatura e contém a data e hora de início, a data
# e hora de fim e o respetivo estado. Este modelo será utilizado por várias
# operações relacionadas com disponibilidade, criação e consulta de reservas.

class Reserva:
    def __init__(self, id=None, cliente_id=None, viatura_id=None, inicio=None, fim=None, estado="CONFIRMADA", criada_em=None, viatura_descricao="", estacao_nome=""):
        self.id = id
        self.cliente_id = cliente_id
        self.viatura_id = viatura_id
        self.inicio = inicio
        self.fim = fim
        self.estado = estado
        self.criada_em = criada_em
        self.viatura_descricao = viatura_descricao
        self.estacao_nome = estacao_nome

    @classmethod
    def from_dict(cls, data):
        return cls(id=data["id"], cliente_id=data["cliente_id"], viatura_id=data["viatura_id"], inicio=data["inicio"], fim=data["fim"], estado=data["estado"], criada_em=data.get("criada_em"), viatura_descricao=data.get("viatura_descricao", ""), estacao_nome=data.get("estacao_nome", ""))
