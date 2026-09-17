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
        sql = """
                SELECT id, nome, morada, cidade, hora_abertura, hora_fecho, ativa
                FROM estacoes
                ORDER BY nome
            """
        rows = self.db.execute(sql, fetch=True)

        estacoes = []
        for row in rows:
            estacao = Estacao.from_dict(row)
            estacoes.append(estacao)

        return estacoes


    def create(self, estacao):
        # TODO 6: inserir uma estação.
        sql = """
                INSERT INTO estacoes (nome, morada, cidade, hora_abertura, hora_fecho, ativa)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
        params = (estacao.nome, estacao.morada, estacao.cidade, estacao.hora_abertura, estacao.hora_fecho, estacao.ativa)

        novo_id = self.db.execute(sql, params)

        estacao.id = novo_id
        return estacao
    
    def update(self, estacao):
        # TODO 7: atualizar uma estação.
        sql = """
                UPDATE estacoes
                SET nome = %s, morada = %s, cidade = %s, hora_abertura = %s, hora_fecho = %s, ativa = %s
                WHERE id = %s
            """
        params = (estacao.nome, estacao.morada, estacao.cidade, estacao.hora_abertura, estacao.hora_fecho, estacao.ativa, estacao.id)

        self.db.execute(sql, params)

        return estacao