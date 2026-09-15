"""
Este ficheiro contém o Repository responsável pelo acesso aos dados das
categorias de viaturas. As operações implementadas aqui devem comunicar com
a tabela correspondente no MySQL e transformar os resultados em objetos
Categoria. Os TODO deste ficheiro permitem começar por consultas SQL simples
antes de avançar para operações que envolvem várias tabelas.
"""


from database import Database
from models.categoria import Categoria


class CategoriaRepository:
    def __init__(self): self.db = Database()

    def find_all(self):
        # TODO 1: obter todas as categorias ordenadas pelo nome.
        sql = "SELECT  id, nome, descricao FROM categorias_viatura ORDER BY nome"
        rows = self.db.execute(sql, fetch= True)

        categorias = []
        for row in rows:
            categoria = Categoria.from_dict(row)
            categorias.append(categoria)

        return categorias

     
    def find_by_id(self, categoria_id):
        # TODO 2: obter uma categoria pelo ID.
        sql = "SELECT  id, nome, descricao FROM categorias_viatura WHERE id = %s"
        rows = self.db.execute(sql,(categoria_id,), fetch=True)

        if not rows:
            return None


        return Categoria.from_dict(rows[0])

