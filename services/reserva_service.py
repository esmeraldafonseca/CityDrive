# Este ficheiro contém o Service responsável pelas principais regras de negócio
# das reservas. Antes de uma reserva ser criada, este Service deve coordenar as
# verificações necessárias sobre o período, o cliente, a viatura, a estação, o
# horário de funcionamento e possíveis conflitos. Por esse motivo, este Service
# utiliza vários Repositories e constitui uma das partes centrais do projeto.

from models.reserva import Reserva
from repositories.reserva_repository import ReservaRepository
from repositories.viatura_repository import ViaturaRepository
from repositories.estacao_repository import EstacaoRepository


class ReservaService:
    def __init__(self):
        self.repository = ReservaRepository()
        self.viatura_repository = ViaturaRepository()
        self.estacao_repository = EstacaoRepository()

    def criar_reserva(self, cliente_id, viatura_id, inicio, fim):
        # TODO 22:
        # - validar inicio < fim;
        # - confirmar viatura ativa;
        # - confirmar estação ativa;
        # - confirmar horário da estação;
        # - confirmar ausência de conflito;
        # - criar a reserva.
        pass

    def cancelar_reserva(self, reserva_id):
        # TODO 23: cancelar a reserva aplicando as regras do sistema.
        pass

    def obter_reserva(
        self, reserva_id): return self.repository.find_by_id(reserva_id)
    def listar_reservas_cliente(
        self, cliente_id): return self.repository.find_by_cliente(cliente_id)

    def listar_todas(self): return self.repository.find_all()
