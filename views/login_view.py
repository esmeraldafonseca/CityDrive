# Este ficheiro define a View inicial da aplicação CityDrive. É responsável por
# apresentar os campos necessários para identificar o cliente e responder à
# ação do botão de entrada. A View deve recolher os valores introduzidos e
# utilizar o Service apropriado, não devendo executar diretamente instruções
# SQL nem implementar regras que pertencem às outras camadas.

import flet as ft

from services.cliente_service import ClienteService
from views.components import app_header, section_card


class LoginView:
    def __init__(self, page):
        self.page = page
        self.service = ClienteService()

        self.email = ft.TextField(label="Email", width=360)
        self.nome = ft.TextField(label="Nome", width=360)
        self.telefone = ft.TextField(label="Telefone", width=360)
        self.mensagem = ft.Text()

    def show(self):
        self.page.clean()

        formulario = ft.Column(
            [
                app_header(
                    "CityDrive",
                    "Reserve uma viatura disponível na cidade e no horário pretendido.",
                ),
                ft.Divider(),
                self.email,
                self.nome,
                self.telefone,
                ft.ElevatedButton("Entrar na aplicação",
                                  on_click=self.login, width=220),
                self.mensagem,
            ],
            spacing=14,
        )

        info = ft.Column(
            [
                ft.Text("Como funciona", size=20, weight=ft.FontWeight.BOLD),
                ft.Text("1. Indique os seus dados."),
                ft.Text("2. Pesquise por cidade e período."),
                ft.Text("3. Consulte a estação e o horário."),
                ft.Text("4. Confirme a reserva da viatura."),
                ft.Divider(),
                ft.Text(
                    "A aplicação está parcialmente implementada. "
                    "Os TODO fazem parte do Trabalho Prático 4(Depois elimina isso no trabalho final)."
                ),
            ],
            spacing=10,
        )

        self.page.add(
            ft.Row(
                [
                    section_card(formulario, width=470),
                    section_card(info, width=420),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.START,
                spacing=28,
                wrap=True,
            )
        )

    def login(self, e):
        # TODO 24: procurar o cliente pelo email; se não existir, criar.
        # Depois abrir a área de pesquisa com o ID do cliente.
        self.mensagem.value = "TODO 24: concluir a entrada do cliente 😂 By: Prof Sebilson."
        self.page.update()
