# Este ficheiro contém o Repository responsável pelo acesso aos dados das
# reservas. Aqui são realizadas as operações SQL necessárias para criar,
# consultar e cancelar reservas, assim como verificar a existência de reservas
# que entrem em conflito com determinado período. A correta interpretação da
# sobreposição entre intervalos de tempo é uma parte fundamental deste ficheiro.

from database import Database
from models.reserva import Reserva


class ReservaRepository:
    def __init__(self): self.db = Database()

    def has_conflict(self, viatura_id, inicio, fim):
        # TODO 14: verificar sobreposição com reservas ativas.
        pass

    def create(self, reserva):
        # TODO 15: inserir uma reserva.
        pass

    def find_by_id(self, reserva_id):
        # TODO 16: obter uma reserva pelo ID.
        pass

    def find_by_cliente(self, cliente_id):
        # TODO 17: obter as reservas de um cliente.
        pass

    def find_all(self):
        # TODO 18: obter todas as reservas para administração.
        pass

    def cancel(self, reserva_id):
        # TODO 19: alterar o estado da reserva para CANCELADA.
        pass
