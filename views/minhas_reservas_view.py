import flet as ft

from services.reserva_service import ReservaService
from views.components import app_header, navigation_bar, section_card, status_chip


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
                    navigation_bar(self.page, self.cliente_id, current="reservas"),
                    app_header(
                        "As minhas reservas",
                        "Consulta e gestão das reservas associadas ao cliente.",
                    ),
                    ft.Row([ft.ElevatedButton("Atualizar", on_click=self.carregar)]),
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
        reservas = self.service.listar_reservas_cliente(self.cliente_id)

        # - apresentar viatura, estação, período e estado;
        # - disponibilizar cancelamento quando permitido.
        self.lista.controls.clear()

        if not reservas:
            self.lista.controls.append(ft.Text("Ainda não tem reservas."))
            self.page.update()
            return

        for reserva in reservas:
            pode_cancelar = reserva.estado not in ("CANCELADA", "CONCLUIDA")

            texto_viatura = ft.Text(reserva.viatura_descricao, weight=ft.FontWeight.BOLD)
            texto_estacao = ft.Text(f"Estação: {reserva.estacao_nome}")
            texto_periodo = ft.Text(f"Período: {reserva.inicio} → {reserva.fim}")
            chip_estado = status_chip(reserva.estado)

            elementos_linha = [texto_viatura, texto_estacao, texto_periodo, chip_estado]

            if pode_cancelar:
                botao_cancelar = ft.OutlinedButton(
                    "Cancelar",
                    on_click=lambda e, r=reserva.id: self.cancelar(r),
                )
                elementos_linha.append(botao_cancelar)

            coluna = ft.Column(elementos_linha, spacing=4)
            self.lista.controls.append(section_card(coluna))

        self.page.update()

    def cancelar(self, reserva_id):
        try:
            self.service.cancelar_reserva(reserva_id)
        except ValueError as erro:
            self.mensagem.value = str(erro)
            self.page.update()
            return

        self.mensagem.value = "Reserva cancelada com sucesso."
        self.carregar(None)