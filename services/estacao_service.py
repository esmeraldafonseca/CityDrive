"""
Este ficheiro contém o Service responsável pelas operações e validações
relacionadas com as estações CityDrive. Antes de solicitar dados ao
Repository, o Service pode verificar se os valores recebidos são válidos.
Desta forma, as regras e validações não ficam espalhadas pelas Views nem
misturadas com as instruções SQL.
"""


from repositories.estacao_repository import EstacaoRepository


class EstacaoService:
    def __init__(self): self.repository = EstacaoRepository()

    def listar_por_cidade(self, cidade):
        # TODO 20: validar a cidade e obter as estações correspondentes.
        if not cidade or not cidade.strip():
            raise ValueError("A cidade é obrigatória.")

        return self.repository.find_active_by_city(cidade.strip())

    def obter_estacao(self, estacao_id):
        return self.repository.find_by_id(estacao_id)

    def listar(self):
        return self.repository.find_all()