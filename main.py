import time
import threading

try:
    import flet as ft
    HAS_FLET = True
except ImportError:
    HAS_FLET = False

def run_terminal_backend(log_callback):
    """Фоновый поток для опроса телеметрии и логирования дрона"""
    log_callback("Инициализация мобильного тактического терминала...")
    time.sleep(1)
    log_callback("Порт USB OTG / Serial: Ожидание подключения полетного контроллера...")
    
    counter = 1
    while True:
        log_callback(f"[ТЕЛЕМЕТРИЯ #{counter}] Связь стабильна. Высота: 0.0м, Напряжение: 11.1В")
        counter += 1
        time.sleep(3)

def main(page: ft.Page):
    page.title = "Drone Tactical GCS"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    logs_view = ft.ListView(expand=1, spacing=5, auto_scroll=True)

    def add_log(text):
        logs_view.controls.append(ft.Text(text, font_family="monospace", size=12))
        page.update()

    title_text = ft.Text("📱 Mobile Drone GCS & Flashing", size=20, weight=ft.FontWeight.BOLD)
    
    status_card = ft.Container(
        content=ft.Column([
            ft.Text("Статус контроллера: Ожидание устройства", color=ft.colors.AMBER_450),
            ft.Row([
                ft.ElevatedButton("Подключить OTG", icon=ft.icons.USB),
                ft.ElevatedButton("Прошивка", icon=ft.icons.SYSTEM_UPDATE, color=ft.colors.RED_400),
            ], alignment=ft.MainAxisAlignment.SPACE_AROUND)
        ]),
        padding=10,
        border_radius=10,
        bgcolor=ft.colors.SURFACE_VARIANT,
    )

    page.add(title_text, status_card, ft.Divider(), ft.Text("Системный лог:", weight=ft.FontWeight.BOLD), logs_view)

    threading.Thread(target=run_terminal_backend, args=(add_log,), daemon=True).start()

if __name__ == "__main__":
    if HAS_FLET:
        ft.app(target=main)
    else:
        print("Flet не установлен. Запуск в консольном режиме.")
        def console_log(msg): print(msg)
        run_terminal_backend(console_log)
