# Este ficheiro contém o Repository responsável pelo acesso aos dados das
# categorias de viaturas. As operações implementadas aqui devem comunicar com
# a tabela correspondente no MySQL e transformar os resultados em objetos
# Categoria. Os TODO deste ficheiro permitem começar por consultas SQL simples
# antes de avançar para operações que envolvem várias tabelas.

from database import Database
from models.categoria import Categoria


class CategoriaRepository:
    def __init__(self): self.db = Database()

    def find_all(self):
        # TODO 1: obter todas as categorias ordenadas pelo nome.
        pass

    def find_by_id(self, categoria_id):
        # TODO 2: obter uma categoria pelo ID.
        pass
