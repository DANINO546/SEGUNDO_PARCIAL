import flet as ft
import random

#Funcion principal
def main(page: ft.Page):
    #Variables globales
    global número_secreto,entrada_número,texto_resultado,boton_adivinar
    
    page.title= "Adivina el número"
    
    #Generar un número aleatorio
    número_secreto = random.randint(1,100)
    
    #crear los elementos de la interfaz(interfaz:lo que va a ver el usuario)
    titulo=ft.Text("Adivina el número secreto entre el 1 y el 100",size= 20, color="white")
    entrada_número=ft.TextField(label="Tu Adivinanza",width=150)
    boton_adivinar=ft.ElevatedButton("Adivinar")
    texto_resultado=ft.Text("",color="white")
    
    contenedor_principal=ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                entrada_número,
                boton_adivinar,
                texto_resultado,
                ft.Image(
                    src="https://i.ibb.co/Gxgryg9/laser.gif",
                    fit=ft.ImageFit.COVER,
                    width=350,
                    height=200
                )
            ],alignment="CENTER",
            horizontal_alignment="CENTER",
            spacing=20
        ),
        bgcolor="orange",
        width=page.window.width,
        height=page.window.height,
        padding=20
    
    
    )
    page.add(contenedor_principal)
    
    
    
ft.app(main)
    