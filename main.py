import flet as ft 
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Hello world")

    greeting_history = []
    history_text = ft.Text("История приветствий:")


    def on_button_click(_):
        name = name_input.value.strip()
        print(name)

        if name:
            greeting_text.value = f"Hello {name}"
            name_input.value = ""

            timestamp = datetime.now().strftime("%H:%M:%S")
            greeting_history.append(f"{timestamp} {name}")
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history) 
        else:
            print("User ничего не ввел")
            greeting_text.value = 'Пожалуйста, введите имя!'

        page.update()

    def clear_history(_):
        greeting_history.clear()
        history_text.value = 'История приветствий'
        page.update()
    
    def sorted_history(_):
        greeting_history.sort(key=lambda x: x.split(" ", 1)[1])
        history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        page.update()

    def last_delete(_):
        if greeting_history:
            greeting_history.pop()
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            print("Ваш список пустой")

        page.update()


    name_input = ft.TextField(label="Введите имя:", on_submit=on_button_click, expand=True)
    name_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click=on_button_click)
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    sort_button = ft.IconButton(icon=ft.Icons.SORT, on_click=sorted_history)
    delete_last_button = ft.IconButton(icon=ft.Icons.DELETE_FOREVER_SHARP, on_click=last_delete)
    # name_button_text = ft.TextButton("SEND")
    # name_button_icon = ft.IconButton(icon=ft.Icons.SEND)

    # page.add(greeting_text, name_input, name_button, clear_button, history_text)
    page.add(greeting_text, 
             ft.Row([name_input, name_button, clear_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
             history_text,
             ft.Row([sort_button, delete_last_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
             )
    

ft.app(target=main, view=ft.WEB_BROWSER)