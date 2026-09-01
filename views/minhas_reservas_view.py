# Este ficheiro define a View onde o cliente poderá consultar as suas reservas.
# A informação apresentada deverá permitir perceber qual a viatura reservada,
# a estação, o período e o estado atual de cada reserva. Quando permitido pelas
# regras do sistema, esta área poderá também disponibilizar ao utilizador a
# possibilidade de cancelar uma reserva existente.

import flet as ft

from services.reserva_service import ReservaService
from views.components import app_header, navigation_bar, section_card


class MinhasReservasView:
    def __init__(self, page, cliente_id):
        self.page = page
        self.cliente_id = cliente_id
        self.service = ReservaService()
        self.lista = ft.Column(spacing=10)
        self.mensagem = ft.Text()

    def show(self):
        self.page.clean()

        self.page.add(
            ft.Column(
                [
                    navigation_bar(self.page, self.cliente_id,
                                   current="reservas"),
                    app_header(
                        "As minhas reservas",
                        "Consulta e gestão das reservas associadas ao cliente.",
                    ),
                    ft.Row(
                        [ft.ElevatedButton("Atualizar", on_click=self.carregar)]),
                    self.mensagem,
                    section_card(self.lista),
                ],
                spacing=16,
            )
        )

        self.carregar(None)

    def carregar(self, e):
        # TODO 28:
        # - obter as reservas do cliente;
        # - apresentar viatura, estação, período e estado;
        # - disponibilizar cancelamento quando permitido.
        self.lista.controls.clear()
        self.lista.controls.append(
            ft.Text("TODO 28: apresentar as reservas do cliente."))
        self.page.update()
