# Este ficheiro contém o Repository responsável pelo acesso aos dados das
# estações CityDrive. Aqui devem ser implementadas as instruções SQL necessárias
# para consultar, criar e atualizar estações. Esta camada deve preocupar-se com
# a obtenção e persistência dos dados, deixando as decisões e validações das
# regras de negócio para os Services.

from database import Database
from models.estacao import Estacao


class EstacaoRepository:
    def __init__(self): self.db = Database()

    def find_active_by_city(self, cidade):
        # TODO 3: obter as estações ativas da cidade indicada.
        pass

    def find_by_id(self, estacao_id):
        # TODO 4: obter uma estação pelo ID.
        pass

    def find_all(self):
        # TODO 5: obter todas as estações.
        pass

    def create(self, estacao):
        # TODO 6: inserir uma estação.
        pass

    def update(self, estacao):
        # TODO 7: atualizar uma estação.
        pass
