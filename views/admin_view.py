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
                            ft.Text("Estações", size=18, weight=ft.FontWeight.BOLD),
                            ft.Text("Gestão de localizações e horários."),
                            ft.ElevatedButton("Listar", on_click=self.listar_estacoes),
                        ]
                    ),
                    width=300,
                ),
                section_card(
                    ft.Column(
                        [
                            ft.Text("Viaturas", size=18, weight=ft.FontWeight.BOLD),
                            ft.Text("Gestão de frota e respetivas estações."),
                            ft.ElevatedButton("Listar", on_click=self.listar_viaturas),
                        ]
                    ),
                    width=300,
                ),
                section_card(
                    ft.Column(
                        [
                            ft.Text("Reservas", size=18, weight=ft.FontWeight.BOLD),
                            ft.Text("Consulta global das reservas."),
                            ft.ElevatedButton("Consultar", on_click=self.listar_reservas),
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
                    navigation_bar(self.page, self.cliente_id, current="admin"),
                    app_header("Área de Administração", "Gestão interna da CityDrive."),
                    dashboard,
                    ft.Divider(),
                    self.conteudo,
                ],
                spacing=16,
            )
        )

    def listar_estacoes(self, e):
        # TODO 29: obter as estações e apresentar uma tabela/lista administrativa.
        estacoes = self.estacao_service.listar()

        self.conteudo.controls.clear()

        if not estacoes:
            self.conteudo.controls.append(ft.Text("Não existem estações registadas."))
            self.page.update()
            return

        linhas = []
        for estacao in estacoes:
            if estacao.ativa:
                texto_estado = "Ativa"
            else:
                texto_estado = "Inativa"

            linha = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(estacao.nome)),
                    ft.DataCell(ft.Text(estacao.cidade)),
                    ft.DataCell(ft.Text(estacao.morada)),
                    ft.DataCell(ft.Text(f"{estacao.hora_abertura} - {estacao.hora_fecho}")),
                    ft.DataCell(ft.Text(texto_estado)),
                ]
            )
            linhas.append(linha)

        tabela = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Nome")),
                ft.DataColumn(ft.Text("Cidade")),
                ft.DataColumn(ft.Text("Morada")),
                ft.DataColumn(ft.Text("Horário")),
                ft.DataColumn(ft.Text("Estado")),
            ],
            rows=linhas,
        )

        self.conteudo.controls.append(tabela)
        self.page.update()

    def listar_viaturas(self, e):
        # TODO 30: obter as viaturas e apresentar categoria, estação e estado.
        viaturas = self.viatura_service.listar()

        self.conteudo.controls.clear()

        if not viaturas:
            self.conteudo.controls.append(ft.Text("Não existem viaturas registadas."))
            self.page.update()
            return

        linhas = []
        for viatura in viaturas:
            if viatura.ativa:
                texto_estado = "Ativa"
            else:
                texto_estado = "Inativa"

            linha = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(f"{viatura.marca} {viatura.modelo}")),
                    ft.DataCell(ft.Text(viatura.matricula)),
                    ft.DataCell(ft.Text(viatura.categoria_nome)),
                    ft.DataCell(ft.Text(f"{viatura.estacao_nome} ({viatura.cidade})")),
                    ft.DataCell(ft.Text(texto_estado)),
                ]
            )
            linhas.append(linha)

        tabela = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Viatura")),
                ft.DataColumn(ft.Text("Matrícula")),
                ft.DataColumn(ft.Text("Categoria")),
                ft.DataColumn(ft.Text("Estação")),
                ft.DataColumn(ft.Text("Estado")),
            ],
            rows=linhas,
        )

        self.conteudo.controls.append(tabela)
        self.page.update()

    def listar_reservas(self, e):
        # TODO 31: obter todas as reservas e apresentar cliente, viatura, período e estado.
        reservas = self.reserva_service.listar_todas()

        self.conteudo.controls.clear()

        if not reservas:
            self.conteudo.controls.append(ft.Text("Não existem reservas registadas."))
            self.page.update()
            return

        linhas = []
        for reserva in reservas:
            linha = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(reserva.cliente_id))),
                    ft.DataCell(ft.Text(reserva.viatura_descricao)),
                    ft.DataCell(ft.Text(f"{reserva.inicio} → {reserva.fim}")),
                    ft.DataCell(ft.Text(reserva.estado)),
                ]
            )
            linhas.append(linha)

        tabela = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Cliente ID")),
                ft.DataColumn(ft.Text("Viatura")),
                ft.DataColumn(ft.Text("Período")),
                ft.DataColumn(ft.Text("Estado")),
            ],
            rows=linhas,
        )

        self.conteudo.controls.append(tabela)
        self.page.update()