import flet as ft

def main(page: ft.Page):
    # إعدادات الصفحة الأساسية
    page.title = "SKYNET WORLD AI"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # تحسين الأداء للويب
    page.window_visible = True

    # محتوى البوابة
    page.add(
        ft.Column(
            [
                ft.Icon(ft.icons.SHIELD_ROUNDS, color="blue", size=100),
                ft.Text("SKYNET WORLD AI", size=40, weight="bold", color="blue"),
                ft.Text("INTELLIGENCE SYSTEM ONLINE", size=18, italic=True, color="grey"),
                ft.Divider(height=20, color="transparent"),
                ft.Container(
                    content=ft.Text("Welcome, Agent. System is fully operational.", color="white"),
                    bgcolor="blue900",
                    padding=20,
                    border_radius=10,
                ),
                ft.ElevatedButton(
                    "Enter Portal", 
                    icon=ft.icons.LOGIN,
                    on_click=lambda _: print("Accessing...")
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
