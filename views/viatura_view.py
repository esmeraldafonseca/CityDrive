# Este ficheiro define a View responsável por apresentar os detalhes de uma
# viatura selecionada na pesquisa. Devem ser apresentados os dados relevantes
# da viatura e da estação onde esta se encontra, incluindo o respetivo horário.
# A partir desta View, o utilizador poderá avançar para a confirmação da reserva
# correspondente ao período anteriormente selecionado.

import flet as ft

from services.estacao_service import EstacaoService
from services.viatura_service import ViaturaService
from views.reserva_view import ReservaView
from views.pesquisa_view import PesquisaView
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
                            ft.OutlinedButton(
                                "Voltar à pesquisa", on_click=self.voltar),
                            ft.ElevatedButton(
                                "Reservar esta viatura", on_click=self.abrir_reserva),
                        ]
                    ),
                ],
                spacing=16,
            )
        )

        # TODO 26:
        # - obter a viatura e a estação;
        # - preencher este painel com os dados reais;
        # - indicar marca, modelo, categoria, matrícula, ano, estação e horário.
        self.conteudo.controls.extend(
            [
                ft.Text("TODO 26: carregar os dados reais da viatura."),
                status_chip("DISPONIBILIDADE A CONFIRMAR"),
                ft.Text(f"Período pretendido: {self.inicio} → {self.fim}"),
            ]
        )
        self.page.update()

    def abrir_reserva(self, e):
        ReservaView(
            self.page,
            self.cliente_id,
            self.viatura_id,
            self.inicio,
            self.fim,
        ).show()

    def voltar(self, e):
        PesquisaView(self.page, self.cliente_id).show()
