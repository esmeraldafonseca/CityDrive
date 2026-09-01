# Este ficheiro contém componentes visuais reutilizáveis pelas diferentes Views
# da aplicação. A sua existência evita repetir a mesma construção de interface
# em vários ficheiros e ajuda a manter uma apresentação consistente. Elementos
# comuns, como cabeçalhos, cartões, indicadores de estado e navegação, podem
# assim ser definidos uma vez e reutilizados onde forem necessários.

import flet as ft


def app_header(title, subtitle=None):
    controls = [ft.Text(title, size=28, weight=ft.FontWeight.BOLD)]
    if subtitle:
        controls.append(ft.Text(subtitle, size=13))
    return ft.Column(controls, spacing=2)


def section_card(content, width=None):
    return ft.Container(
        content=content,
        width=width,
        padding=18,
        border=ft.Border.all(1),
        border_radius=12,
    )


def status_chip(text):
    return ft.Container(
        content=ft.Text(text, size=12, weight=ft.FontWeight.BOLD),
        padding=ft.Padding.symmetric(horizontal=10, vertical=5),
        border=ft.Border.all(1),
        border_radius=20,
    )


def navigation_bar(page, cliente_id=None, current="pesquisa"):
    from views.pesquisa_view import PesquisaView
    from views.minhas_reservas_view import MinhasReservasView
    from views.admin_view import AdminView

    def go_search(e):
        PesquisaView(page, cliente_id).show()

    def go_bookings(e):
        MinhasReservasView(page, cliente_id).show()

    def go_admin(e):
        AdminView(page, cliente_id).show()

    return ft.Row(
        [
            ft.TextButton("Pesquisar", on_click=go_search,
                          disabled=current == "pesquisa"),
            ft.TextButton("As minhas reservas", on_click=go_bookings,
                          disabled=current == "reservas"),
            ft.TextButton("Administração", on_click=go_admin,
                          disabled=current == "admin"),
        ],
        alignment=ft.MainAxisAlignment.END,
    )
