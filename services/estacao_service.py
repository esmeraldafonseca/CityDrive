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

        cidade = cidade.strip()

        if len(cidade) < 2:
            raise ValueError("A cidade deve ter pelo menos 2 caracteres.")

        if any(caractere.isdigit() for caractere in cidade):
            raise ValueError("A cidade não deve conter números.")

        return self.repository.find_active_by_city(cidade)

    def obter_estacao(self, estacao_id):
        return self.repository.find_by_id(estacao_id)

    def listar(self):
        return self.repository.find_all()