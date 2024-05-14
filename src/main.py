import flet as ft
from flet import UserControl, TextButton, Row, Page
import math


def navigation_btn_clicked(e):
    print(e.data + ' button was clicked')

def main(page: ft.Page):
    page.title = "Navigate"

    connection = ft.Container(
        alignment= ft.alignment.center,
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Text("Click to connect"),
                                margin=10,
                                padding=10,
                                alignment=ft.alignment.center,
                                bgcolor=ft.colors.GREEN_200,
                                width=150,
                                height=50,
                                border_radius=10,
                                on_click=lambda e: print("Click to connect clicked!"),
                            ),
                        ]
                    )
                )
            ]
        )
    )

    navigation = ft.Container(
        alignment= ft.alignment.center,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.IconButton(
                                data='Upper Left',
                                icon=ft.icons.KEYBOARD_ARROW_UP,
                                icon_color="gray",
                                icon_size=48,
                                rotate= - math.pi / 4,
                                on_click=lambda e: navigation_btn_clicked(e),
                            ),
                            ft.IconButton(
                                icon=ft.icons.KEYBOARD_ARROW_UP,
                                icon_color="gray",
                                icon_size=48,
                            ),
                            ft.IconButton(
                                icon=ft.icons.KEYBOARD_ARROW_UP,
                                icon_color="gray",
                                icon_size=48,
                                rotate= math.pi / 4
                            ),
                        ],
                    ),
                    padding=10,
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.KEYBOARD_ARROW_LEFT,
                                icon_color="gray",
                                icon_size=48,
                            ),
                            ft.IconButton(
                                icon=ft.icons.STOP_CIRCLE,
                                icon_color="gray",
                                icon_size=48,
                            ),
                            ft.IconButton(
                                icon=ft.icons.KEYBOARD_ARROW_RIGHT,
                                icon_color="gray",
                                icon_size=48,
                            ),
                        ],
                    ),
                    padding=10,
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.KEYBOARD_ARROW_DOWN,
                                icon_color="gray",
                                icon_size=48,
                                rotate= math.pi / 4
                            ),
                            ft.IconButton(
                                icon=ft.icons.KEYBOARD_ARROW_DOWN,
                                icon_color="gray",
                                icon_size=48,
                            ),
                            ft.IconButton(
                                icon=ft.icons.KEYBOARD_ARROW_DOWN,
                                icon_color="gray",
                                icon_size=48,
                                rotate= - math.pi / 4
                            ),
                        ],
                    ),
                    padding=10,
                ),
            ]
        )
    )

    page.add(
        ft.Row(
            [
                connection,
                navigation,
            ]
    )
    )

app = ft.app(target=main)
