# Este ficheiro define a View responsável pela confirmação de uma reserva.
# A página apresenta ao utilizador um resumo da operação e permite solicitar
# a criação da reserva. A View não deve decidir sozinha se a reserva é válida;
# essa responsabilidade pertence ao ReservaService, que deverá aplicar todas
# as regras de negócio antes de permitir que os dados sejam gravados.

import flet as ft

from services.reserva_service import ReservaService
from views.pesquisa_view import PesquisaView
from views.components import app_header, navigation_bar, section_card


class ReservaView:
    def __init__(self, page, cliente_id, viatura_id, inicio, fim):
        self.page = page
        self.cliente_id = cliente_id
        self.viatura_id = viatura_id
        self.inicio = inicio
        self.fim = fim

        self.service = ReservaService()
        self.mensagem = ft.Text()

    def show(self):
        self.page.clean()

        resumo = ft.Column(
            [
                ft.Text("Resumo", size=18, weight=ft.FontWeight.BOLD),
                ft.Text(f"Viatura ID: {self.viatura_id}"),
                ft.Text(f"Início: {self.inicio}"),
                ft.Text(f"Fim: {self.fim}"),
                ft.Text(
                    "Antes de gravar, o sistema deverá validar a viatura, "
                    "a estação, o horário e conflitos com outras reservas."
                ),
            ],
            spacing=8,
        )

        self.page.add(
            ft.Column(
                [
                    navigation_bar(self.page, self.cliente_id),
                    app_header("Confirmar reserva"),
                    section_card(resumo),
                    ft.Row(
                        [
                            ft.OutlinedButton("Voltar", on_click=self.voltar),
                            ft.ElevatedButton(
                                "Confirmar reserva", on_click=self.confirmar),
                        ]
                    ),
                    self.mensagem,
                ],
                spacing=16,
            )
        )

    def confirmar(self, e):
        # TODO 27: chamar ReservaService.criar_reserva e apresentar o resultado.
        self.mensagem.value = "TODO 27: concluir a confirmação da reserva."
        self.page.update()

    def voltar(self, e):
        PesquisaView(self.page, self.cliente_id).show()
