# Este ficheiro contém o Repository responsável pelo acesso aos dados dos
# clientes. É nesta camada que são executadas as instruções SQL necessárias
# para procurar e criar clientes. Este Repository encontra-se parcialmente
# implementado para servir como referência sobre a forma como os restantes
# Repositories devem utilizar a classe Database e devolver objetos do modelo.

from database import Database
from models.cliente import Cliente


class ClienteRepository:
    def __init__(self): self.db = Database()

    def find_by_email(self, email):
        rows = self.db.execute(
            "SELECT id, nome, email, telefone FROM clientes WHERE email = %s", (email,), fetch=True)
        return Cliente.from_dict(rows[0]) if rows else None

    def find_by_id(self, cliente_id):
        rows = self.db.execute(
            "SELECT id, nome, email, telefone FROM clientes WHERE id = %s", (cliente_id,), fetch=True)
        return Cliente.from_dict(rows[0]) if rows else None

    def create(self, cliente):
        return self.db.execute("INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)", (cliente.nome, cliente.email, cliente.telefone))
