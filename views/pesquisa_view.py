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

        self.cidade = ft.TextField(label="Cidade", value="Castelo Branco", width=280)
        self.inicio = ft.TextField(label="Início", hint_text="AAAA-MM-DD HH:MM", width=230)
        self.fim = ft.TextField(label="Fim", hint_text="AAAA-MM-DD HH:MM", width=230)

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
                    navigation_bar(self.page, self.cliente_id, current="pesquisa"),
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
        self.resultados.controls.clear()
        self.mensagem.value = ""

        try:
            inicio = datetime.strptime(self.inicio.value, "%Y-%m-%d %H:%M")
            fim = datetime.strptime(self.fim.value, "%Y-%m-%d %H:%M")
        except (ValueError, TypeError):
            self.mensagem.value = "Datas inválidas. Use o formato AAAA-MM-DD HH:MM."
            self.page.update()
            return

        # - validar o período;
        # - procurar viaturas disponíveis;
        try:
            viaturas = self.service.procurar_disponiveis(self.cidade.value, inicio, fim)
        except ValueError as erro:
            self.mensagem.value = str(erro)
            self.page.update()
            return

        if not viaturas:
            self.mensagem.value = "Não foram encontradas viaturas disponíveis para este período."
            self.page.update()
            return

        # - apresentar os resultados em cartões com opção "Ver viatura".
        for viatura in viaturas:
            informacao = ft.Column(
                [
                    ft.Text(f"{viatura.marca} {viatura.modelo}", weight=ft.FontWeight.BOLD),
                    ft.Text(f"Matrícula: {viatura.matricula}"),
                    ft.Text(f"Categoria: {viatura.categoria_nome}"),
                    ft.Text(f"Estação: {viatura.estacao_nome} ({viatura.cidade})"),
                ],
                spacing=2,
            )

            botao = ft.ElevatedButton(
                "Ver viatura",
                on_click=lambda e, v=viatura.id: self.abrir_viatura(v, inicio, fim),
            )

            linha = ft.Row(
                [informacao, botao],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )

            self.resultados.controls.append(section_card(linha))

        self.mensagem.value = f"{len(viaturas)} viatura(s) encontrada(s)."
        self.page.update()

    def abrir_viatura(self, viatura_id, inicio, fim):
        ViaturaView(self.page, self.cliente_id, viatura_id, inicio, fim).show()