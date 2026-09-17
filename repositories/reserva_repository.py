"""
Este ficheiro contém o Repository responsável pelo acesso aos dados das
reservas. Aqui são realizadas as operações SQL necessárias para criar,
consultar e cancelar reservas, assim como verificar a existência de reservas
que entrem em conflito com determinado período. A correta interpretação da
sobreposição entre intervalos de tempo é uma parte fundamental deste ficheiro.
"""

from database import Database
from models.reserva import Reserva


class ReservaRepository:
    def __init__(self): self.db = Database()

    def has_conflict(self, viatura_id, inicio, fim):
        # TODO 14: verificar sobreposição com reservas ativas.
        pass

    def create(self, reserva):
        # TODO 15: inserir uma reserva.
        sql = """
                INSERT INTO reservas (cliente_id, viatura_id, inicio, fim, estado)
                VALUES (%s, %s, %s, %s, %s)
            """
        params = (reserva.cliente_id, reserva.viatura_id, reserva.inicio, reserva.fim, reserva.estado)

        novo_id = self.db.execute(sql, params)

        reserva.id = novo_id
        return reserva

    def find_by_id(self, reserva_id):
        # TODO 16: obter uma reserva pelo ID.
        sql = """
                SELECT id, cliente_id, viatura_id, inicio, fim, estado, criada_em
                FROM reservas
                WHERE id = %s
            """
        rows = self.db.execute(sql, (reserva_id,), fetch=True)

        if not rows:
            return None

        return Reserva.from_dict(rows[0])


    def find_by_cliente(self, cliente_id):
        # TODO 17: obter as reservas de um cliente.
        pass

    def find_all(self):
        # TODO 18: obter todas as reservas para administração.
        sql = """
                SELECT r.id, r.cliente_id, r.viatura_id, r.inicio, r.fim, r.estado, r.criada_em,
                    CONCAT(v.marca, ' ', v.modelo, ' (', v.matricula, ')') AS viatura_descricao,
                    e.nome AS estacao_nome
                FROM reservas r
                JOIN viaturas v ON r.viatura_id = v.id
                JOIN estacoes e ON v.estacao_id = e.id
            """
        rows = self.db.execute(sql, fetch=True)

        reservas = []
        for row in rows:
            reserva = Reserva.from_dict(row)
            reservas.append(reserva)

        return reservas

    def cancel(self, reserva_id):
        # TODO 19: alterar o estado da reserva para CANCELADA.
        sql = """
                UPDATE reservas 
                SET estado = 'CANCELADA' 
                WHERE id = %s
            """
        self.db.execute(sql, (reserva_id,))