import flet as ft
from produto_1 import produto_1
from produto_2 import produto_2
from produto_3 import produto_3
from produto_4 import produto_4
def card_venda_beleza(page: ft.Page):
    # page.title = "Produto"
    page.bgcolor= ft.colors.BLACK
    # page.window.width = 450
    # page.window.height = 300

    produto_a = produto_1(page)
    produto_b = produto_2(page)
    produto_c = produto_3(page)
    produto_d = produto_4(page)
    
    grade_produtos = ft.Container(
        content=ft.Column(
            controls=[
                ft.GridView(
                    controls=[produto_a,produto_b,produto_c,produto_d],
                    expand=1, #runs_count=2,
                    spacing=20,
                    run_spacing=10,
                    # padding=10,
                    max_extent=500,
                    child_aspect_ratio=1,
                    
                )
            ]
        )
    )

    return grade_produtos

    # page.add(layout)


# if __name__ == '__main__':
#     ft.app(target=main)#, view=ft.WEB_BROWSER)