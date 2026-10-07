"""
Este ficheiro contém o Service responsável pelas operações relacionadas com
as viaturas. Entre as suas responsabilidades encontra-se a validação dos
dados utilizados numa pesquisa de disponibilidade antes de comunicar com o
ViaturaRepository. A interface deverá pedir ao Service que execute a operação,
sem conhecer os detalhes das consultas utilizadas para encontrar as viaturas.
"""


from datetime import datetime
from repositories.viatura_repository import ViaturaRepository


class ViaturaService:
    def __init__(self): self.repository = ViaturaRepository()

    def procurar_disponiveis(self, cidade, inicio, fim):
        # TODO 21: validar os dados e procurar viaturas disponíveis.
        if not cidade or not cidade.strip():
            raise ValueError("A cidade é obrigatória.")

        if inicio is None or fim is None:
            raise ValueError("As datas de início e fim são obrigatórias.")

        if not isinstance(inicio, datetime) or not isinstance(fim, datetime):
            raise ValueError("As datas devem ser objetos datetime válidos.")

        if inicio >= fim:
            raise ValueError("A data de início deve ser anterior à data de fim.")

        return self.repository.find_available(cidade.strip(), inicio, fim)

    
    def obter_viatura(self, viatura_id): 
        return self.repository.find_by_id(viatura_id)

    
    def listar_por_estacao(self, estacao_id): 
        return self.repository.find_by_station(estacao_id)


    def listar(self): 
        return self.repository.find_all()
