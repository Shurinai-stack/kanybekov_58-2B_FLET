import flet as ft 


def main(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Hello world")
    greeting_text1 = ft.Text("Hello world")
    name_input = ft.TextField(label="Введите имя:")
    age_input = ft.TextField(label="Введите возраст:")

    def on_button_click(_):
        name = name_input.value.strip()
        age = age_input.value.strip()
        print(name)
        print(age)

        if name and age:
            greeting_text.value = f"Hello {name}"
            greeting_text1.value = f"Привет {name}, тебе {age} лет"
            name_input.value = ""
            age_input.value = ""
        else:
            print("User ничего не ввел")
            greeting_text.value = 'Пожалуйста, введите имя!'
            greeting_text1.value = 'Пожалуйста, введите возраст!'

        page.update()
        
    
    def change_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()
            



    name_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click=on_button_click)
    change_theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=change_theme)
    
    # name_button_text = ft.TextButton("SEND")
    # name_button_icon = ft.IconButton(icon=ft.Icons.SEND)

    page.add(greeting_text, name_input, greeting_text1,age_input , name_button, change_theme_button)


ft.app(target=main, view=ft.WEB_BROWSER)

