import flet as ft
import whatsapp as wp
import time


def contato(page: ft.Page):
    bot_whatsapp = wp.main(page)
    linha_contato = ft.ResponsiveRow(controls=[
        ft.Column(controls=[
            ft.Text("whatsapp: (19) 999206-8471",size=16,color=ft.colors.WHITE),
            ft.Text("Email: imc.viva.bem@gmail.com",size=16,color=ft.colors.WHITE),
        ],col=6),
        ft.Column(controls=[ft.ResponsiveRow(controls=[bot_whatsapp],)],col=6,)
        ])
    
    pagina_contato = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Meu nome é Carlos José Marcato, desenvolvedor e criador da Plataforma IMC VIVA BEM",size=18,color=ft.colors.WHITE,italic=True),
                ft.Image(src="IMC/app_imc/assets/google_maps.JPG",width=700),
                ft.Text("Nossa sede está localizada na Cidade de Ipeúna - SP",size=16,color=ft.colors.WHITE),
                linha_contato
            ]    
    ),bgcolor=ft.colors.GREEN,expand=1,alignment=ft.alignment.center)    

    ft.animation

    return pagina_contato