"""
Este ficheiro contém o Service responsável pelas principais regras de negócio
das reservas. Antes de uma reserva ser criada, este Service deve coordenar as
verificações necessárias sobre o período, o cliente, a viatura, a estação, o
horário de funcionamento e possíveis conflitos. Por esse motivo, este Service
utiliza vários Repositories e constitui uma das partes centrais do projeto.
"""


from datetime import datetime, time

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
        if inicio is None or fim is None:
            raise ValueError("As datas de início e fim são obrigatórias.")
        if inicio >= fim:
            raise ValueError("A data de início deve ser anterior à data de fim.")

        # - confirmar viatura ativa;
        viatura = self.viatura_repository.find_by_id(viatura_id)
        if viatura is None:
            raise ValueError("A viatura indicada não existe.")
        if not viatura.ativa:
            raise ValueError("A viatura indicada não está ativa.")

        # - confirmar estação ativa;
        estacao = self.estacao_repository.find_by_id(viatura.estacao_id)
        if estacao is None:
            raise ValueError("A estação da viatura não existe.")
        if not estacao.ativa:
            raise ValueError("A estação da viatura não está ativa.")

        # - confirmar horário da estação;
        hora_inicio = inicio.time()
        hora_fim = fim.time()
        if hora_inicio < estacao.hora_abertura or hora_inicio > estacao.hora_fecho:
            raise ValueError("O horário de início está fora do horário da estação.")
        if hora_fim < estacao.hora_abertura or hora_fim > estacao.hora_fecho:
            raise ValueError("O horário de fim está fora do horário da estação.")

        # - confirmar ausência de conflito;
        if self.repository.has_conflict(viatura_id, inicio, fim):
            raise ValueError("Já existe uma reserva para esta viatura nesse período.")

        # - criar a reserva.
        reserva = Reserva(cliente_id=cliente_id, viatura_id=viatura_id, inicio=inicio, fim=fim, estado="CONFIRMADA")
        return self.repository.create(reserva)

    def cancelar_reserva(self, reserva_id):
        # TODO 23: cancelar a reserva aplicando as regras do sistema.
        reserva = self.repository.find_by_id(reserva_id)
        if reserva is None:
            raise ValueError("A reserva indicada não existe.")

        if reserva.estado in ("CANCELADA", "CONCLUIDA"):
            raise ValueError("Esta reserva não pode ser cancelada.")

        self.repository.cancel(reserva_id)
        return True


    def obter_reserva(self, reserva_id):
        return self.repository.find_by_id(reserva_id)


    def listar_reservas_cliente(self, cliente_id):
        return self.repository.find_by_cliente(cliente_id)


    def listar_todas(self):
        return self.repository.find_all()
