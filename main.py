import flet as ft

def main(page: ft.Page):
    # إعدادات لكسر السواد
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Icon(ft.icons.TERMINAL, color="green", size=50),
                ft.Text("HOUCINE SKYNET: SYSTEM ONLINE", color="green", size=25, weight="bold"),
                ft.Text("If you see this, the path error is fixed!", color="white")
            ], horizontal_alignment="center"),
            padding=20,
            border=ft.border.all(2, "green"),
            border_radius=10
        )
    )
    page.update()

ft.app(target=main)
