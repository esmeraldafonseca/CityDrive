# Este ficheiro é o ponto de entrada da aplicação CityDrive. É responsável por
# iniciar o Flet, configurar as principais propriedades da janela e apresentar
# a primeira View da aplicação. Aqui não devem ser implementadas regras de
# negócio nem instruções SQL, pois a sua função é apenas iniciar e preparar
# a aplicação.
import flet as ft

from views.login_view import LoginView


def main(page: ft.Page):
    page.title = "CityDrive - Reserva de Viaturas"
    page.padding = 24
    page.window.width = 1180
    page.window.height = 780
    page.scroll = ft.ScrollMode.AUTO

    LoginView(page).show()


if __name__ == "__main__":
    ft.run(main)
