# Este ficheiro contém o Service responsável pelas operações relacionadas com
# clientes. O Service funciona como intermediário entre a interface e o
# Repository, podendo validar os dados antes de solicitar uma operação à base
# de dados. As Views devem utilizar este Service em vez de comunicar diretamente
# com o ClienteRepository.

from models.cliente import Cliente
from repositories.cliente_repository import ClienteRepository


class ClienteService:
    def __init__(self): self.repository = ClienteRepository()

    def obter_cliente(
        self, cliente_id): return self.repository.find_by_id(cliente_id)

    def obter_por_email(
        self, email): return self.repository.find_by_email(email)

    def criar_cliente(self, nome, email, telefone):
        if not nome.strip() or not email.strip() or not telefone.strip():
            raise ValueError("Todos os campos são obrigatórios.")
        cliente = Cliente(nome=nome.strip(), email=email.strip(
        ).lower(), telefone=telefone.strip())
        return self.repository.create(cliente)
