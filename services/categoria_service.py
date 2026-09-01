# Este ficheiro contém o Service responsável pelas operações relacionadas com
# categorias de viaturas. A sua função é disponibilizar estas operações às
# restantes partes da aplicação sem expor diretamente o Repository. Esta
# separação permite manter a interface independente da forma como os dados
# são armazenados e consultados.

from repositories.categoria_repository import CategoriaRepository


class CategoriaService:
    def __init__(self): self.repository = CategoriaRepository()
    def listar(self): return self.repository.find_all()
