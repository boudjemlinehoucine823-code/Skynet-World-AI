import flet as ft
import requests

def main(page: ft.Page):
    page.title = "SKYNET - Intelligence Hub"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.GREY_900
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.padding = 20

    def fetch_market_data(e):
        status_text.value = "⏳ جاري سحب بيانات السوق..."
        fetch_btn.disabled = True
        page.update()
        try:
            response = requests.get(
                "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT",
                timeout=10
            )
            data = response.json()
            price = float(data['price'])
            market_text.value = f"💰 BTC/USDT: ${price:,.2f}"
            status_text.value = "✅ تم سحب البيانات بنجاح."
            status_text.color = ft.colors.GREEN_400
        except Exception as ex:
            status_text.value = f"❌ خطأ: {str(ex)}"
            status_text.color = ft.colors.RED_400
        fetch_btn.disabled = False
        page.update()

    status_text = ft.Text(
        "🔵 النظام في وضع الاستعداد",
        color=ft.colors.BLUE_200,
        size=14
    )

    market_text = ft.Text(
        "اضغط على الزر للبدء...",
        size=18,
        color=ft.colors.GREEN_300,
        weight=ft.FontWeight.BOLD
    )

    fetch_btn = ft.ElevatedButton(
        "📡 سحب بيانات السوق",
        icon=ft.icons.DOWNLOAD,
        on_click=fetch_market_data,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.BLUE_800,
            color=ft.colors.WHITE
        )
    )

    result_card = ft.Container(
        content=ft.Column([
            ft.Text(
                "📊 بيانات السوق الحية",
                size=18,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.WHITE
            ),
            market_text,
        ]),
        padding=20,
        bgcolor=ft.colors.GREY_800,
        border_radius=12,
        border=ft.border.all(1, ft.colors.BLUE_700)
    )

    page.add(
        ft.AppBar(
            title=ft.Text(
                "⚡ SKYNET INTELLIGENCE PORTAL",
                color=ft.colors.WHITE
            ),
            bgcolor=ft.colors.BLUE_900,
            center_title=True
        ),
        ft.Column(
            controls=[
                ft.Icon(ft.icons.ANALYTICS, size=60, color=ft.colors.BLUE_300),
                ft.Text(
                    "مركز تحليل البيانات",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.WHITE
                ),
                status_text,
                fetch_btn,
                result_card,
                ft.TextField(
                    label="اسأل عن البيانات...",
                    multiline=True,
                    min_lines=2,
                    border_color=ft.colors.BLUE_700,
                    color=ft.colors.WHITE,
                    label_style=ft.TextStyle(color=ft.colors.BLUE_200)
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.app(target=main)
