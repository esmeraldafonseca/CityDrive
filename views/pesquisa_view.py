# Este ficheiro define a View utilizada para pesquisar viaturas disponíveis.
# O utilizador indica a cidade e o período pretendido, sendo responsabilidade
# desta View recolher e converter esses valores, solicitar a pesquisa ao Service
# e apresentar os resultados recebidos. A lógica que determina efetivamente
# se uma viatura está disponível não deve ser implementada diretamente aqui.

import flet as ft
from datetime import datetime

from services.viatura_service import ViaturaService
from views.viatura_view import ViaturaView
from views.components import app_header, navigation_bar, section_card


class PesquisaView:
    def __init__(self, page, cliente_id):
        self.page = page
        self.cliente_id = cliente_id
        self.service = ViaturaService()

        self.cidade = ft.TextField(
            label="Cidade", value="Castelo Branco", width=280)
        self.inicio = ft.TextField(
            label="Início",
            hint_text="AAAA-MM-DD HH:MM",
            width=230,
        )
        self.fim = ft.TextField(
            label="Fim",
            hint_text="AAAA-MM-DD HH:MM",
            width=230,
        )

        self.resultados = ft.Column(spacing=10)
        self.mensagem = ft.Text()

    def show(self):
        self.page.clean()

        filtros = ft.Row(
            [
                self.cidade,
                self.inicio,
                self.fim,
                ft.ElevatedButton("Pesquisar", on_click=self.pesquisar),
            ],
            wrap=True,
            spacing=12,
        )

        exemplo = ft.Column(
            [
                ft.Text("Exemplo de pesquisa", weight=ft.FontWeight.BOLD),
                ft.Text("Cidade: Castelo Branco"),
                ft.Text("Início: 2026-09-10 06:30"),
                ft.Text("Fim: 2026-09-10 12:00"),
            ],
            spacing=4,
        )

        self.page.add(
            ft.Column(
                [
                    navigation_bar(self.page, self.cliente_id,
                                   current="pesquisa"),
                    app_header(
                        "Pesquisa de viaturas",
                        "O sistema deverá apresentar apenas viaturas disponíveis no período selecionado.",
                    ),
                    section_card(filtros),
                    section_card(exemplo),
                    self.mensagem,
                    ft.Text("Resultados", size=20, weight=ft.FontWeight.BOLD),
                    self.resultados,
                ],
                spacing=16,
            )
        )

    def pesquisar(self, e):
        # TODO 25:
        # - converter as datas;
        # - validar o período;
        # - procurar viaturas disponíveis;
        # - apresentar os resultados em cartões com opção "Ver viatura".
        self.resultados.controls.clear()
        self.mensagem.value = "TODO 25: concluir a pesquisa de disponibilidade."
        self.page.update()

    def abrir_viatura(self, viatura_id, inicio, fim):
        ViaturaView(
            self.page,
            self.cliente_id,
            viatura_id,
            inicio,
            fim,
        ).show()
