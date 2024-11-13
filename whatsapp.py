import flet as ft
def main(page: ft.Page):
    def open_whatsapp(e):
        # Substitua pelo seu número de WhatsApp com o código do país (ex: +55)
        whatsapp_link = f"https://wa.me/5519992068471?text=Olá,%20gostaria%20de%20saber%20mais%20sobre..."
        page.launch_url(whatsapp_link)

    # Ícone do WhatsApp
    whatsapp_icon = ft.Container(
        ft.Image("IMC/app_imc/assets/logo_whatsapp.png"),
        on_click=open_whatsapp,
        tooltip="Fale conosco no WhatsApp",width=100,height=100,col=6,scale=1
        )
    
    # Container para o botão, com posicionamento fixo no canto inferior direito
    bot_whatsapp = ft.Container(
        whatsapp_icon,
        padding=10,
        width=120,
        height=120,
        col=6
    )

    return bot_whatsapp
#     page.add(bot_whatsapp)

# ft.app(target=main)
