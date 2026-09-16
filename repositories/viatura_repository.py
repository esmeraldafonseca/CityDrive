"""
Este ficheiro contém o Repository responsável pelo acesso aos dados das
viaturas. Algumas operações exigem relacionar viaturas, categorias, estações
e reservas, pelo que neste ficheiro será necessário interpretar e construir
consultas SQL com JOIN e outras condições. É também aqui que deverá ser feita
a consulta necessária para determinar quais as viaturas disponíveis num
determinado período.
"""

from database import Database
from models.viatura import Viatura


class ViaturaRepository:
    def __init__(self): self.db = Database()

    def find_by_id(self, viatura_id):
        # TODO 8: obter uma viatura, incluindo categoria e estação.
        sql = """
                SELECT v.id, v.matricula, v.marca, v.modelo, v.categoria_id, v.ano, v.estacao_id, v.ativa,
                    c.nome AS categoria_nome, e.nome AS estacao_nome, e.cidade AS cidade
                FROM viaturas v
                JOIN categorias_viatura c ON v.categoria_id = c.id
                JOIN estacoes e ON v.estacao_id = e.id
                WHERE v.id = %s
            """
        rows = self.db.execute(sql, (viatura_id,), fetch=True)

        if not rows:
            return None

        return Viatura.from_dict(rows[0])

            
    def find_available(self, cidade, inicio, fim):
        # TODO 9: obter viaturas ativas disponíveis no período indicado.
        sql = """
                SELECT v.id, v.matricula, v.marca, v.modelo, v.categoria_id, v.ano, v.estacao_id, v.ativa,
                    c.nome AS categoria_nome, e.nome AS estacao_nome, e.cidade AS cidade
                FROM viaturas v
                JOIN categorias_viatura c ON v.categoria_id = c.id
                JOIN estacoes e ON v.estacao_id = e.id
                WHERE e.cidade = %s
                AND v.ativa = TRUE
                AND e.ativa = TRUE
                AND NOT EXISTS (
                    SELECT 1 FROM reservas r
                    WHERE r.viatura_id = v.id
                        AND r.estado NOT IN ('CANCELADA', 'CONCLUIDA')
                        AND r.inicio < %s
                        AND r.fim > %s
                )
                ORDER BY v.marca, v.modelo
            """
        params = (cidade, fim, inicio)
        rows = self.db.execute(sql, params, fetch=True)

        viaturas = []
        for row in rows:
            viatura = Viatura.from_dict(row)
            viaturas.append(viatura)

        return viaturas


    def find_by_station(self, estacao_id):
        # TODO 10: obter as viaturas de uma estação.
        pass


    def find_all(self):
        # TODO 11: obter todas as viaturas com categoria e estação.
        pass


    def create(self, viatura):
        # TODO 12: inserir uma viatura.
        pass


    def update(self, viatura):
        # TODO 13: atualizar uma viatura.
        pass
