# Este ficheiro define a área administrativa da aplicação CityDrive. A interface
# reúne funcionalidades destinadas à consulta e gestão de estações, viaturas e
# reservas. Mesmo nesta área, as operações devem continuar a respeitar a
# arquitetura do projeto, utilizando os Services apropriados em vez de executar
# SQL ou implementar diretamente a lógica de acesso aos dados.

import flet as ft

from services.estacao_service import EstacaoService
from services.viatura_service import ViaturaService
from services.reserva_service import ReservaService
from views.components import app_header, navigation_bar, section_card


class AdminView:
    def __init__(self, page, cliente_id=None):
        self.page = page
        self.cliente_id = cliente_id
        self.estacao_service = EstacaoService()
        self.viatura_service = ViaturaService()
        self.reserva_service = ReservaService()
        self.conteudo = ft.Column(spacing=10)

    def show(self):
        self.page.clean()

        dashboard = ft.Row(
            [
                section_card(
                    ft.Column(
                        [
                            ft.Text("Estações", size=18,
                                    weight=ft.FontWeight.BOLD),
                            ft.Text("Gestão de localizações e horários."),
                            ft.ElevatedButton(
                                "Listar", on_click=self.listar_estacoes),
                        ]
                    ),
                    width=300,
                ),
                section_card(
                    ft.Column(
                        [
                            ft.Text("Viaturas", size=18,
                                    weight=ft.FontWeight.BOLD),
                            ft.Text("Gestão de frota e respetivas estações."),
                            ft.ElevatedButton(
                                "Listar", on_click=self.listar_viaturas),
                        ]
                    ),
                    width=300,
                ),
                section_card(
                    ft.Column(
                        [
                            ft.Text("Reservas", size=18,
                                    weight=ft.FontWeight.BOLD),
                            ft.Text("Consulta global das reservas."),
                            ft.ElevatedButton(
                                "Consultar", on_click=self.listar_reservas),
                        ]
                    ),
                    width=300,
                ),
            ],
            wrap=True,
            spacing=14,
        )

        self.page.add(
            ft.Column(
                [
                    navigation_bar(self.page, self.cliente_id,
                                   current="admin"),
                    app_header("Área de Administração",
                               "Gestão interna da CityDrive."),
                    dashboard,
                    ft.Divider(),
                    self.conteudo,
                ],
                spacing=16,
            )
        )

    def listar_estacoes(self, e):
        # TODO 29: obter as estações e apresentar uma tabela/lista administrativa.
        self.conteudo.controls.clear()
        self.conteudo.controls.append(ft.Text("TODO 29: listar estações."))
        self.page.update()

    def listar_viaturas(self, e):
        # TODO 30: obter as viaturas e apresentar categoria, estação e estado.
        self.conteudo.controls.clear()
        self.conteudo.controls.append(ft.Text("TODO 30: listar viaturas."))
        self.page.update()

    def listar_reservas(self, e):
        # TODO 31: obter todas as reservas e apresentar cliente, viatura, período e estado.
        self.conteudo.controls.clear()
        self.conteudo.controls.append(ft.Text("TODO 31: listar reservas."))
        self.page.update()
