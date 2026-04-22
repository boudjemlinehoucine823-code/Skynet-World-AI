import flet as ft

def main(page: ft.Page):
    # إعدادات إجبارية لمنع الشاشة السوداء
    page.window_visible = True
    page.theme_mode = ft.ThemeMode.DARK
    
    # واجهة Skynet المحدثة
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Icon(ft.icons.SHIELD_ROUNDS, color="blue", size=50),
                ft.Text("SKYNET SYSTEM ONLINE", size=20, weight="bold"),
                ft.ProgressBar(width=200, color="blue"),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            alignment=ft.alignment.center,
            expand=True
        )
    )
    page.update()

# السطر الأهم: يجب تحديد assets_dir بدقة
ft.app(target=main, assets_dir="assets")
