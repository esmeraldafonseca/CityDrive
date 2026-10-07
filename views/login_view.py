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
                ft.ElevatedButton("Entrar na aplicação", on_click=self.login, width=220),
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
        self.mensagem.value = ""

        if self.email.value:
            email = self.email.value.strip()
        else:
            email = ""

        if not email:
            self.mensagem.value = "O email é obrigatório."
            self.page.update()
            return

        cliente = self.service.obter_por_email(email)

        if cliente is None:
            try:
                cliente = self.service.criar_cliente(
                    self.nome.value, self.email.value, self.telefone.value
                )
            except ValueError as erro:
                self.mensagem.value = str(erro)
                self.page.update()
                return

        from views.pesquisa_view import PesquisaView
        PesquisaView(self.page, cliente.id).show()