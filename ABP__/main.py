import flet as ft
import random

# Lista de palabras para el juego
palabras = ['python', 'programacion', 'desarrollo', 'computadora', 'algoritmo']

# Función para obtener una palabra aleatoria
def obtener_palabra():
    return random.choice(palabras)

# Clase para el juego de ahorcados
class Ahorcado:
    def __init__(self):
        self.palabra = obtener_palabra()
        self.letras_adivinadas = []
        self.intentos_restantes = 6

    def adivinar(self, letra):
        if letra not in self.letras_adivinadas:
            self.letras_adivinadas.append(letra)
            if letra not in self.palabra:
                self.intentos_restantes -= 1

    def palabra_oculta(self):
        return ' '.join(letra if letra in self.letras_adivinadas else '_' for letra in self.palabra)

    def juego_terminado(self):
        return self.intentos_restantes <= 0 or all(letra in self.letras_adivinadas for letra in self.palabra)

def main(page: ft.Page):
    page.title = "Juego del Ahorcado"
    page.bgcolor="pink"
    page.window_width = 400
    page.window_height = 300

    ahorcado = Ahorcado()

    def actualizar_vista():
        page.controls.clear()
        
        page.add(
            ft.Text("Adivina la palabra:"),
            ft.Text(ahorcado.palabra_oculta(), size=30),
            ft.Text(f"Intentos restantes: {ahorcado.intentos_restantes}"),
        )

        if ahorcado.juego_terminado():
            if all(letra in ahorcado.letras_adivinadas for letra in ahorcado.palabra):
                page.add(ft.Text("¡Felicidades! Has adivinado la palabra.", color=ft.colors.GREEN))
            else:
                page.add(ft.Text(f"¡Perdiste! La palabra era: {ahorcado.palabra}", color=ft.colors.RED))
            page.add(ft.ElevatedButton("Reiniciar", on_click=reiniciar))
        else:
            page.add(ft.TextField(label="Adivina una letra", on_submit=lambda e: adivinar_letra(e.control.value)))

        page.update()

    def adivinar_letra(letra):
        ahorcado.adivinar(letra.lower())
        actualizar_vista()

    def reiniciar(e):
        ahorcado.__init__()
        actualizar_vista()

    actualizar_vista()

if __name__ == "__main__":
    ft.app(target=main)
