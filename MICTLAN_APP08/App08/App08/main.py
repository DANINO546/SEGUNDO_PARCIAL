import flet as ft


def main(page: ft.Page):
#establecer tamaño de pantalla
    
    page.window_width=800
    page.window_height=800
    
    page.bgcolor="black"
    page.title="mictlan"
    page.fgcolor="gray"
    
    def detener():
        Intro.pause()
        Nivel1.pause()
        Nivel2.pause()
        Nivel3.pause()
        Nivel4.pause()
        Nivel5.pause()
        Nivel6.pause()
        Nivel7.pause()
        Nivel8.pause()
        Nivel9.pause()


    def playIntro(e):
        detener()
        Intro.play()

    def playNivel1(e):
        detener()
        Nivel1.play()
    
    def playNivel2(e):
        detener()
        Nivel2.play()
    
    def playNivel3(e):
        detener()
        Nivel3.play()
    
    def playNivel4(e):
        detener()
        Nivel4.play()
    
    def playNivel5(e):
        detener()
        Nivel5.play()
    
    def playNivel6(e):
        detener()
        Nivel6.play()

    def playNivel7(e):
        detener()
        Nivel7.play()

    def playNivel8(e):
        detener()
        Nivel8.play()

    def playNivel9(e):
        detener()
        Nivel9.play()
        

    Intro=ft.Audio(src="Intro.mp3",volume=1,balance=0)
    page.overlay.append(Intro)
    
    Nivel1=ft.Audio(src="Primer_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel1)
    
    Nivel2=ft.Audio(src="Segundo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel2)
    
    Nivel3=ft.Audio(src="Tercer_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel3)
    
    Nivel4=ft.Audio(src="Cuarto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel4)
    
    Nivel5=ft.Audio(src="Quinto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel5)
    
    Nivel6=ft.Audio(src="Sexto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel6)
    
    Nivel7=ft.Audio(src="Septimo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel7)

    Nivel8=ft.Audio(src="Octavo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel8)

    Nivel9=ft.Audio(src="Noveno_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel9)
    
#creacion de la interfaz

    btnIntro=ft.FilledButton(text="escucha el intro",disabled=False,on_click=playIntro)

    btnNivel1=ft.ElevatedButton(text="primer nivel",on_click=playNivel1)
    img1=ft.Image(src="Primer-Nivel.jpeg",width=150,height=150)

    btnNivel2=ft.ElevatedButton(text="segundo nivel",on_click=playNivel2)
    img2=ft.Image(src="Segundo-Nivel.jpeg",width=150,height=150)

    btnNivel3=ft.ElevatedButton(text="tercer nivel",on_click=playNivel3)
    img3=ft.Image(src="Tercer-Nivel.png",width=150,height=150)

    btnNivel4=ft.ElevatedButton(text="cuarto nivel",on_click=playNivel4)
    img4=ft.Image(src="Cuarto-Nivel.jpeg",width=150,height=150)

    btnNivel5=ft.ElevatedButton(text="quinto nivel",on_click=playNivel5)
    img5=ft.Image(src="Quinto-Nivel.jpeg",width=150,height=150)

    btnNivel6=ft.ElevatedButton(text="sexto nivel",on_click=playNivel6)
    img6=ft.Image(src="Sexto-Nivel.jpeg",width=150,height=150)

    btnNivel7=ft.ElevatedButton(text="septimo nivel",on_click=playNivel7)
    img7=ft.Image(src="Septimo-Nivel.jpeg",width=150,height=150)

    btnNivel8=ft.ElevatedButton(text="octavo nivel",on_click=playNivel8)
    img8=ft.Image(src="Octavo-Nivel.png",width=150,height=150)

    btnNivel9=ft.ElevatedButton(text="noveno nivel",on_click=playNivel9)
    img9=ft.Image(src="Noveno-Nivel.jpeg",width=150,height=150)
    

    page.add(
        ft.Row(
            alignment="start",
            controls=[btnIntro]
        ),
        ft.Column(
            alignment="CENTER",
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Row(
                    alignment="CENTER",
                    controls=[
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnNivel1,img1]
                        ),
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnNivel2,img2]
                        ),
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnNivel3,img3]
                        )
                    ]
                ),
                ft.Row(
                    alignment="CENTER",
                    controls=[
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnNivel4,img4]
                        ),
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnNivel5,img5]
                        ),
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnNivel6,img6]
                        )
                    ]
                ),
                ft.Row(
                    alignment="CENTER",
                    controls=[
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnNivel7,img7]
                        ),
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnNivel8,img8]
                        ),
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnNivel9,img9]
                        )
                    ]
                )
            ]
        )
    )
            
        

ft.app(main)