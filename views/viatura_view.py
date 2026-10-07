import flet as ft

from services.estacao_service import EstacaoService
from services.viatura_service import ViaturaService
from views.reserva_view import ReservaView
from views.components import app_header, navigation_bar, section_card, status_chip


class ViaturaView:
    def __init__(self, page, cliente_id, viatura_id, inicio, fim):
        self.page = page
        self.cliente_id = cliente_id
        self.viatura_id = viatura_id
        self.inicio = inicio
        self.fim = fim

        self.viatura_service = ViaturaService()
        self.estacao_service = EstacaoService()
        self.conteudo = ft.Column(spacing=12)

    def show(self):
        self.page.clean()

        self.page.add(
            ft.Column(
                [
                    navigation_bar(self.page, self.cliente_id),
                    app_header("Detalhe da viatura"),
                    section_card(self.conteudo),
                    ft.Row(
                        [
                            ft.OutlinedButton("Voltar à pesquisa", on_click=self.voltar),
                            ft.ElevatedButton("Reservar esta viatura", on_click=self.abrir_reserva),
                        ]
                    ),
                ],
                spacing=16,
            )
        )

        # TODO 26:
        # - obter a viatura e a estação;
        viatura = self.viatura_service.obter_viatura(self.viatura_id)
        estacao = self.estacao_service.obter_estacao(viatura.estacao_id)

        # - preencher este painel com os dados reais;
        # - indicar marca, modelo, categoria, matrícula, ano, estação e horário.
        titulo = ft.Text(f"{viatura.marca} {viatura.modelo}", size=20, weight=ft.FontWeight.BOLD)
        matricula = ft.Text(f"Matrícula: {viatura.matricula}")
        categoria = ft.Text(f"Categoria: {viatura.categoria_nome}")
        ano = ft.Text(f"Ano: {viatura.ano}")

        nome_estacao = ft.Text(f"Estação: {estacao.nome}")
        morada_estacao = ft.Text(f"Morada: {estacao.morada}, {estacao.cidade}")
        horario_estacao = ft.Text(f"Horário: {estacao.hora_abertura} - {estacao.hora_fecho}")

        estado = status_chip("DISPONÍVEL PARA O PERÍODO PESQUISADO")
        periodo = ft.Text(f"Período pretendido: {self.inicio} → {self.fim}")

        self.conteudo.controls.append(titulo)
        self.conteudo.controls.append(matricula)
        self.conteudo.controls.append(categoria)
        self.conteudo.controls.append(ano)
        self.conteudo.controls.append(ft.Divider())
        self.conteudo.controls.append(nome_estacao)
        self.conteudo.controls.append(morada_estacao)
        self.conteudo.controls.append(horario_estacao)
        self.conteudo.controls.append(estado)
        self.conteudo.controls.append(periodo)

        self.page.update()

    def abrir_reserva(self, e):
        ReservaView(self.page, self.cliente_id, self.viatura_id, self.inicio, self.fim).show()

    def voltar(self, e):
        # Import local para evitar a importação circular com pesquisa_view.
        from views.pesquisa_view import PesquisaView
        PesquisaView(self.page, self.cliente_id).show()