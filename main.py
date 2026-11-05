
import flet as ft


class ContadorApp:

    def __init__(self, page):
        self.page = page
        self.contador = 0

        self.page.title = "Contador Interactivo"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.bgcolor = ft.Colors.WHITE

        self.numero = ft.Text(
            value="0",
            size=55,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE
        )

        self.page.add(
            ft.Column(
                controls=[
                    ft.Text(
                        "CONTADOR INTERACTIVO",
                        size=25,
                        weight=ft.FontWeight.BOLD
                    ),
                    self.numero,
                    ft.Row(
                        controls=[
                            ft.Button(
                                content="Sumar +",
                                on_click=self.sumar
                            ),
                            ft.Button(
                                content="Restar -",
                                on_click=self.restar
                            ),
                            ft.Button(
                                content="Reiniciar",
                                on_click=self.reiniciar
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=25
            )
        )

    def sumar(self, e):
        self.contador += 1
        self.actualizar()

    def restar(self, e):
        self.contador -= 1
        self.actualizar()

    def reiniciar(self, e):
        self.contador = 0
        self.actualizar()

    def actualizar(self):
        self.numero.value = str(self.contador)
        self.page.update()


def main(page: ft.Page):
    ContadorApp(page)


ft.run(main)
