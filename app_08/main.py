import flet as ft


def main(page: ft.Page):
#establecer tamaño de pantalla

    page.window_width=800
    page.window_height=800
    
    page.bgcolor="black"
    page.title="Mictlan"
    page.fgcolor"gray"
    
    intro=ft.Audio(src="Intro.mp3",volumen=1,balance=0)
    page.overlay.append(Intro) 
    
    PrimerNivel=ft.Audio(src="Primer_Nviel.mp3",volume=1,balance=0)
    page.overlay.append(PrimerNivel)
    
    SegundoNivel=ft.Audio(src="Segundo_Nviel.mp3",volume=1,balance=0)
    page.overlay.append(SegundoNivel)
    
    TercerNivel=ft.Audio(src="Tercer_Nviel.mp3",volume=1,balance=0)
    page.overlay.append(TercerNivel)
    
    CuartoNivel=ft.Audio(src="Cuarto_Nviel.mp3",volume=1,balance=0)
    page.overlay.append(CuartoNivel)
    
    QuintoNivel=ft.Audio(src="Quinto_Nviel.mp3",volume=1,balance=0)
    page.overlay.append(QuintoNivel)
    
    SextoNivel=ft.Audio(src="Sexto_Nviel.mp3",volume=1,balance=0)
    page.overlay.append(SextoNivel)
    
    SeptimoNivel=ft.Audio(src="Septimo_Nviel.mp3",volume=1,balance=0)
    page.overlay.append(SeptimoNivel)
    
    OctavoNivel=ft.Audio(src="Octavo_Nviel.mp3",volume=1,balance=0)
    page.overlay.append(OctavoNivel)
    
    NovenoNivel=ft.Audio(src="Noveno_Nviel.mp3",volume=1,balance=0)
    page.overlay.append(NovenoNivel)
    
#Se crea el interfaz
    btnIntro=ft.FilledButton(text="Escucha el Intro",disabled==False)
    
    btnNivel1=ft.ElevatedButton(text="Primer Nivel")
    img1=ft.Image(src="Primer-Nivel.jpeg",width=150,height=150)
    
    btnNivel2=ft.ElevatedButton(text="Segundo Nivel")
    img2=ft.Image(src="Segundo-Nivel.jpeg",width=150,height=150)
    
    btnNivel3=ft.ElevatedButton(text="Tercero Nivel")
    img3=ft.Image(src="Tercer-Nivel.png",width=150,height=150)
    
    btnNivel4=ft.ElevatedButton(text="Primer Nivel")
    img1=ft.Image(src="Primer-Nivel.jpeg",width=150,height=150)
    
    btnNivel5=ft.ElevatedButton(text="Primer Nivel")
    img1=ft :t.Image(src="Primer-Nivel.jpeg",width=150,height=150)
    
    btnNivel6=ft.ElevatedButton(text="Primer Nivel")
    img1=ft.Image(src="Primer-Nivel.jpeg",width=150,height=150)
    
    btnNivel7=ft.ElevatedButton(text="Primer Nivel")
    img1=ft.Image(src="Primer-Nivel.jpeg",width=150,height=150)
    
    btnNivel8=ft.ElevatedButton(text="Primer Nivel")
    img1=ft.Image(src="Primer-Nivel.jpeg",width=150,height=150)
    
    btnNivel9=ft.ElevatedButton(text="Primer Nivel")
    img1=ft.Image(src="Primer-Nivel.jpeg",width=150,height=150)
    
    page.add(
        ft.Row(
            alignment=="start",
            controls=[btnIntro]
        ),
        ft.Column(
            alignment="CENTER",
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Row(
                    alignment="CENTER",
                    controls=[btnNivel1,img1]
                ),
                ft.Column(
                    alignment="CENTER",
                    controls=[btnNivel2,img1]
                    
                )
                )
            )
        )
    )
ft.app(main)
