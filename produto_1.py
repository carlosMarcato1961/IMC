import flet as ft


def produto_1(page: ft.Page):
    # page.title = "Produto"
    page.bgcolor= ft.colors.BLACK
    # page.window.width = 450
    # page.window.height = 300

    def saiba_mais(e):
        def limpa_alert(e):
            texto.open = False
            page.update()
        texto = ft.AlertDialog(content= ft.Column(controls=[
                    ft.ElevatedButton('Fechar', bgcolor='black', color='white',on_click=limpa_alert),
                    ft.Text('Cálculo realizado com dados fornecidos pela Organização Mundial da Saúde. O IMC não leva em consideração a taxa de massa muscular e a quantidade de gordura no corpo.\nSempre consulte um médico antes de iniciar qualquer ação para ganhar ou perder peso.\n\nFeche para ver o resultado.', size=20,color='black'),
                    ]),bgcolor='amber',)
        page.overlay.append(texto)
        texto.open = True
        page.update()


    def imagem_ativa_1(e):
        for elem in imagem_opcao.controls:
            #verifica se o botão clicado e o botão que vai ser ativo
            if elem == e.control:
                elem.opacity = 1
                imagem_princ.src = elem.image_src
            else:
                elem.opacity = 0.5
        imagem_princ.update()
        imagem_opcao.update()
    
    def link_mp(e):
        page.launch_url('https://mpago.la/1vp8j2G')


    imagem_prod_1 = ft.Container(
                    content=ft.Column(
                    #um componente vai pra cima e o outro para baixo
                    # alignment=ft.MainAxisAlignment.CENTER,
                    controls=[imagem_princ := ft.Image(src="IMC/app_imc/assets/imagem_1.png"),
                              imagem_opcao := ft.Row(alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Container(
                                        image_src="IMC/app_imc/assets/imagem_1.png",
                                        width= 60,
                                        height= 60,
                                        opacity=1,
                                        #função troca a imagem em destaque
                                        on_click=imagem_ativa_1
                                    ),
                                    ft.Container(
                                        image_src="IMC/app_imc/assets/imagem_2.png",
                                        width= 60,
                                        height= 60,
                                        opacity=0.5,
                                        #função troca a imagem em destaque
                                        on_click=imagem_ativa_1
                                    ),
                                    ft.Container(
                                        image_src="IMC/app_imc/assets/imagem_3.png",
                                        width= 60,
                                        height= 60,
                                        opacity=0.5,
                                        #função troca a imagem em destaque
                                        on_click=imagem_ativa_1
                                    ),
                                ]
                                ),
                                ft.Container(content=ft.ElevatedButton(
                                        text="Saiba Mais",bgcolor=ft.colors.AMBER,color=ft.colors.BLACK,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=10),
                                            ),
                                        on_click=saiba_mais,icon=ft.icons.VISIBILITY
                                ),alignment=ft.alignment.center)
                            ]
            ),bgcolor=ft.colors.WHITE,#aspect_ratio=9/16,
                               col={'xs':6,'md':6, 'lg':6, 'xl':6}
            )
    detalhes_prod = ft.Container(padding=0,
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                value="Nome do produto",
                                size=20,
                                color=ft.colors.AMBER,
                                weight=ft.FontWeight.BOLD,),
                            # ft.Text(
                            #     value='Nome do produto',
                            #     size=15,
                            #     color=ft.colors.WHITE),
                            ft.ResponsiveRow(
                                columns=12,
                                controls=[
                                    ft.Text(
                                        value='R$ 99,99',
                                        size=18,
                                        color=ft.colors.WHITE,
                                        col={'xs':5,'md':5, 'lg':5, 'xl':5}),
                                    ft.Row(
                                        controls=[
                                            ft.Icon(
                                                name=ft.icons.STAR,
                                                color=ft.colors.AMBER,
                                                size=10
                                            )for i in range(5) #gera 5 estrelas
                                    ],
                                        col={'xs':7,'md':7, 'lg':7, 'xl':7}
                                    )
                                ]
                            ),
                            ft.Tabs(
                                height=120,
                                #primeira aba fica selecionada
                                selected_index=0, 
                                #cor da aba selecionada            
                                indicator_color=ft.colors.AMBER,
                                #cor do texto da aba selecionada
                                label_color=ft.colors.AMBER,                   
                                    tabs=[
                                        ft.Tab(
                                            text="Descrição",
                                            content=ft.Text('Este produto é a sensação do verão, proteje sua pele e ao mesmo tempo deixa um bronzeado maravilhoso, sua amigas vão invejar e seu marido vai adorar!',size=10)
                                        ),
                                        ft.Tab(
                                            text="Detalhes",
                                            content=ft.Text('Detalhes do produto',size=10)
                                        )
                                ]),
                            ft.ResponsiveRow(
                                columns=12,
                                controls=[
                                    # ft.Dropdown(
                                    #     col=6,
                                    #     label="Cor",
                                    #     label_style=ft.TextStyle(color=ft.colors.WHITE,size=12),
                                    #     border_color=ft.colors.GREEN,
                                    #     border_width=0.5,
                                    #     options=[
                                    #         ft.dropdown.Option("Azul"),
                                    #         ft.dropdown.Option("Vermelho"),
                                    #         ft.dropdown.Option("Verde"),
                                    #     ]
                                    # ),
                                    ft.Dropdown(
                                        col=6,
                                        label="Quantidade",
                                        label_style=ft.TextStyle(color=ft.colors.WHITE,size=12),
                                        border_color=ft.colors.GREEN,
                                        border_width=0.5,
                                        height=40,width=120,
                                        text_size=12,
                                        options=[
                                            ft.dropdown.Option(f'{num} Unid')for num in range(1,11)
                                        ]
                                    ),
                                    ft.ElevatedButton('Adicionar ao carrinho',col=12),
                                    ft.ElevatedButton('Comprar',col=12,on_click=link_mp,bgcolor=ft.colors.GREEN,color=ft.colors.WHITE)
                                    
                                ])
                        ]
                    ,run_spacing=0,spacing=0),bgcolor=ft.colors.GREY_800,#aspect_ratio=9/16,
                               col={'xs':6,'md':6, 'lg':6, 'xl':6},
                )
    
    produto_1 = ft.ResponsiveRow(controls=[imagem_prod_1,detalhes_prod],spacing=0)

    return produto_1