"""
Este ficheiro contém o Repository responsável pelo acesso aos dados das
estações CityDrive. Aqui devem ser implementadas as instruções SQL necessárias
para consultar, criar e atualizar estações. Esta camada deve preocupar-se com
a obtenção e persistência dos dados, deixando as decisões e validações das
regras de negócio para os Services.
"""

from database import Database
from models.estacao import Estacao


class EstacaoRepository:
    def __init__(self): self.db = Database()

    def find_active_by_city(self, cidade):
        # TODO 3: obter as estações ativas da cidade indicada.
        sql = """
                SELECT id, nome, morada, cidade, hora_abertura, hora_fecho, ativa
                FROM estacoes
                WHERE cidade = %s AND ativa = TRUE
                ORDER BY nome
            """
        rows = self.db.execute(sql, (cidade,), fetch=True)

        estacoes = []
        for row in rows:
            estacao = Estacao.from_dict(row)
            estacoes.append(estacao)

        return estacoes


    def find_by_id(self, estacao_id):
        # TODO 4: obter uma estação pelo ID.
        sql = """
                SELECT id, nome, morada, cidade, hora_abertura, hora_fecho, ativa
                FROM estacoes
                WHERE id = %s
            """
        rows = self.db.execute(sql, (estacao_id,), fetch=True)

        if not rows:
            return None

        return Estacao.from_dict(rows[0])

    def find_all(self):
        # TODO 5: obter todas as estações.
        pass

    def create(self, estacao):
        # TODO 6: inserir uma estação.
        pass

    def update(self, estacao):
        # TODO 7: atualizar uma estação.
        pass
