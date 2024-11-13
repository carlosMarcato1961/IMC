import flet as ft
import numpy as np
from grade_venda_emagrec import card_venda_emagrec
from grade_venda_beleza import card_venda_beleza
from grade_venda_cuidPessoais import card_venda_cuidPessoais
from grade_venda_pele import card_venda_pele
from contato import contato
from cadastro import cadastro
from carrinho import carrinho

#FUNÇÃO FLET PARA PRODUZIR UM FRONTEND EM PYTHON
def main(page: ft.Page):
    page.title = 'IMC VIVA BEM'
    page.bgcolor= ft.colors.BLACK
    page.padding= 0 
    page.scroll=ft.ScrollMode.AUTO
    # page.window_width = 'auto'    

    def main_cri(e):
        idade = int(cri_idade.value)
        peso = round(float(cri_peso.value),2)
        altura = round(float(cri_altura.value),2)
        imc = round(peso/altura**2, 1)

        tx_cri_normal_5_12 = f'O valor do IMC é {imc}, portanto o peso do seu filho(a) está em uma faixa adequada em relação a altura. Uma alimentação balanceada, com baixos níveis de açucar e gordura, fará de seu filho uma criança saudável e no futuro um adulto com menos propensão a obesidade.\nLembre-se, qualquer dúvida consulte um pediatra.'
        tx_cri_magro_5_12 = f'O valor do IMC é {imc}, este valor é considerado abaixo do recomendado. Srs. pais se atentem que quanto mais a seta se afasta da área verde mais preocupante é a situação. seria adequado uma consulta ao pediatra para avaliar melhor o resultado do IMC.'
        tx_cri_gordo_5_12 = f'O valor do IMC é {imc}, este valor é considerado acima do peso adequado. Srs. pais se atentem que quanto mais a seta se afasta da área verde mais preocupante é a situação. Consulte um pediatra para melhor avaliação do resultado. Lembre-se que a obesidade pode trazer sérios risco a saúde.'

        adolec_normal = f'O valor do seu IMC é {imc}, esse valor se enquadra em uma faixa de peso considerada adequada para sua altura. Se a seta aponta para as extremidades, da área verde, fique atento para não ficar abaixo nem acima do peso mais saudável para você. Sempre consulte um médico se tiver alguma dúvida.'
        adolec_magro = f'O valor do seu IMC é {imc}, esse valor está abaixo do adequado para sua altura, quanto mais a seta se afasta da área verde mais preocupante é sua relação peso/altura. Consulte um médico para avaliar melhor o resultado obtido.'
        adolec_gordo = f'O valor do seu IMC é {imc}, este valor está acima do adequado para sua altura, quanto mais a seta se afasta da área verde mais preocupante é sua relação peso/altura. A obesidade gera graves problemas de saúde, consulte um médico para avaliar melhor seu peso.'
        
        #CRIANÇAS DE 5 A 12 ANOS
        #5 ANOS
        if cri_idade.value == '5': 
            #peso nornal
            if imc > 14.9 and imc < 15.7:
                normal_2.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            elif imc > 13.9 and imc < 15:
                normal_1.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            elif imc > 15.6 and imc < 16.8:
                normal_3.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            #peso abaixo
            elif imc > 13.5 and imc < 14:
                magro_3.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            elif imc > 13.1 and imc < 13.6:
                magro_2.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            elif imc < 13.2:
                magro_1.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            #peso acima
            elif imc > 16.7 and imc < 18.1:
                gordo_1.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
            elif imc > 18 and imc < 19.1:
                gordo_2.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
            elif imc > 19:
                gordo_3.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
            # page.update()
        #6 ANOS
        elif cri_idade.value == '6': 
            #peso nornal
            if imc > 14.9 and imc < 15.7:
                normal_2.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            elif imc > 13.9 and imc < 15:
                normal_1.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            elif imc > 15.6 and imc < 16.8:
                normal_3.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            #peso abaixo
            elif imc > 13.5 and imc < 14:
                magro_3.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            elif imc > 13.1 and imc < 13.6:
                magro_2.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            elif imc < 13.2:
                magro_1.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            #peso acima
            elif imc > 16.7 and imc < 18.6:
                gordo_1.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
            elif imc > 18.5 and imc < 19.5:
                gordo_2.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
            elif imc > 19.4:
                gordo_3.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
        #7 ANOS
        elif cri_idade.value == '7': 
            #peso nornal
            #normal_2 é central
            if imc > 15.1 and imc < 15.9:
                normal_2.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            elif imc > 14.1 and imc < 15.2:
                normal_1.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            elif imc > 15.8 and imc < 17.3:
                normal_3.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            #peso abaixo
            #magro_3 é mais perto do noraml
            elif imc > 13.8 and imc < 14.2:
                magro_3.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            elif imc > 13.4 and imc < 13.9:
                magro_2.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            elif imc < 13.5:
                magro_1.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            #peso acima
            #gordo_1 é mais perto do normal
            elif imc > 17.1 and imc < 18.8:
                gordo_1.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
            elif imc > 18.7 and imc < 19.7:
                gordo_2.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
            elif imc > 19.6:
                gordo_3.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
        #8 ANOS
        elif cri_idade.value == '8': 
            #peso nornal
            #normal_2 é central
            if imc > 15.3 and imc < 16.1:
                normal_2.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            elif imc > 14.2 and imc < 15.4:
                normal_1.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            elif imc > 16 and imc < 17.6:
                normal_3.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            #peso abaixo
            #magro_3 é mais perto do noraml
            elif imc > 13.8 and imc < 14.3:
                magro_3.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            elif imc > 13.3 and imc < 13.9:
                magro_2.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            elif imc < 13.4:
                magro_1.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            #peso acima
            #gordo_1 é mais perto do normal/SOBRE PESO
            elif imc > 17.4 and imc < 19.4:
                gordo_1.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
            elif imc > 19.3 and imc < 20.4:
                gordo_2.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
            elif imc > 20.3:
                gordo_3.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
        #9 ANOS
        elif cri_idade.value == '9': 
            #peso nornal
            #normal_2 é central
            if imc > 15.6 and imc < 16.4:
                normal_2.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            elif imc > 14.5 and imc < 15.7:
                normal_1.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            elif imc > 16.3 and imc < 18.1:
                normal_3.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            #peso abaixo
            #magro_3 é mais perto do noraml
            elif imc > 14.1 and imc < 14.7:
                magro_3.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            elif imc > 13.5 and imc < 14.2:
                magro_2.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            elif imc < 13.6:
                magro_1.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            #peso acima
            #gordo_1 é mais perto do normal/SOBRE PESO
            elif imc > 17.9 and imc < 20.3:
                gordo_1.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
            elif imc > 20.2 and imc < 21.3:
                gordo_2.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
            elif imc > 21.2:
                gordo_3.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
        #10 ANOS
        elif cri_idade.value == '10': 
            #peso nornal
            #normal_2 é central
            if imc > 15.9 and imc < 16.9:
                normal_2.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            elif imc > 14.7 and imc < 16:
                normal_1.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            elif imc > 16.8 and imc < 18.7:
                normal_3.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            #peso abaixo
            #magro_3 é mais perto do noraml
            elif imc > 14.2 and imc < 14.9:
                magro_3.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            elif imc > 13.6 and imc < 14.3:
                magro_2.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            elif imc < 13.7:
                magro_1.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            #peso acima
            #gordo_1 é mais perto do normal/SOBRE PESO
            elif imc > 18.6 and imc < 21.1:
                gordo_1.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
            elif imc > 21 and imc < 21.9:
                gordo_2.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
            elif imc > 21.8:
                gordo_3.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
        #11 ANOS
        elif cri_idade.value == '11': 
            #peso nornal
            #normal_2 é central
            if imc > 16.4 and imc < 17.4:
                normal_2.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            elif imc > 15.2 and imc < 16.5:
                normal_1.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            elif imc > 17.3 and imc < 19.4:
                normal_3.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            #peso abaixo
            #magro_3 é mais perto do noraml
            elif imc > 14.7 and imc < 15.3:
                magro_3.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            elif imc > 14.1 and imc < 14.8:
                magro_2.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            elif imc < 14.2:
                magro_1.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            #peso acima
            #gordo_1 é mais perto do normal/SOBRE PESO
            elif imc > 19.3 and imc < 22.1:
                gordo_1.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
            elif imc > 22 and imc < 23.1:
                gordo_2.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
            elif imc > 23:
                gordo_3.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
        #12 ANOS
        elif cri_idade.value == '12': 
            #peso nornal
            #normal_2 é central
            if imc > 16.9 and imc < 18.1:
                normal_2.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            elif imc > 15.6 and imc < 17:
                normal_1.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            elif imc > 18 and imc < 20.1:
                normal_3.opacity = 1
                texto_imc_cri.value = tx_cri_normal_5_12
            #peso abaixo
            #magro_3 é mais perto do noraml
            elif imc > 15 and imc < 15.7:
                magro_3.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            elif imc > 14.6 and imc < 15.1:
                magro_2.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            elif imc < 14.7:
                magro_1.opacity = 1
                texto_imc_cri.value = tx_cri_magro_5_12
            #peso acima
            #gordo_1 é mais perto do normal/SOBRE PESO
            elif imc > 20 and imc < 23.1:
                gordo_1.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
            elif imc > 23 and imc < 24.1:
                gordo_2.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12
            elif imc > 24:
                gordo_3.opacity = 1
                texto_imc_cri.value = tx_cri_gordo_5_12

        #ADOLESCENTES DE 12 A 19 ANOS

        #13 ANOS
        elif cri_idade.value == '13': 
            #peso nornal
            #normal_2 é central
            if imc > 17.5 and imc < 18.9:
                normal_2.opacity = 1
                texto_imc_cri.value = adolec_normal
            elif imc > 16.2 and imc < 17.6:
                normal_1.opacity = 1
                texto_imc_cri.value = adolec_normal
            elif imc > 18.8 and imc < 21.1:
                normal_3.opacity = 1
                texto_imc_cri.value = adolec_normal
            #peso abaixo
            #magro_3 é mais perto do noraml
            elif imc > 15.6 and imc < 16.3:
                magro_3.opacity = 1
                texto_imc_cri.value = adolec_magro
            elif imc > 15.1 and imc < 15.7:
                magro_2.opacity = 1
                texto_imc_cri.value = adolec_magro
            elif imc < 15.2:
                magro_1.opacity = 1
                texto_imc_cri.value = adolec_magro
            #peso acima
            #gordo_1 é mais perto do normal/SOBRE PESO
            elif imc > 21 and imc < 24.3:
                gordo_1.opacity = 1
                texto_imc_cri.value = adolec_gordo
            elif imc > 24.2 and imc < 25.3:
                gordo_2.opacity = 1
                texto_imc_cri.value = adolec_gordo
            elif imc > 25.2:
                gordo_3.opacity = 1
                texto_imc_cri.value = adolec_gordo
        # 14 ANOS
        elif cri_idade.value == '14': 
            #peso nornal
            #normal_2 é central
            if imc > 18.4 and imc < 19.6:
                normal_2.opacity = 1
                texto_imc_cri.value = adolec_normal
            elif imc > 16.8 and imc < 18.5:
                normal_1.opacity = 1
                texto_imc_cri.value = adolec_normal
            elif imc > 19.5 and imc < 21.9:
                normal_3.opacity = 1
                texto_imc_cri.value = adolec_normal
            #peso abaixo
            #magro_3 é mais perto do noraml
            elif imc > 16.1 and imc < 16.9:
                magro_3.opacity = 1
                texto_imc_cri.value = adolec_magro
            elif imc > 15.6 and imc < 16.2:
                magro_2.opacity = 1
                texto_imc_cri.value = adolec_magro
            elif imc < 15.7:
                magro_1.opacity = 1
                texto_imc_cri.value = adolec_magro
            #peso acima
            #gordo_1 é mais perto do normal/SOBRE PESO
            elif imc > 21.8 and imc < 25.4:
                gordo_1.opacity = 1
                texto_imc_cri.value = adolec_gordo
            elif imc > 25.3 and imc < 26.5:
                gordo_2.opacity = 1
                texto_imc_cri.value = adolec_gordo
            elif imc > 26.4:
                gordo_3.opacity = 1
                texto_imc_cri.value = adolec_gordo
        #15 ANOS
        elif cri_idade.value == '15': 
            #peso nornal
            #normal_2 é central
            if imc > 18.9 and imc < 20.5:
                normal_2.opacity = 1
                texto_imc_cri.value = adolec_normal
            elif imc > 17.5 and imc < 19:
                normal_1.opacity = 1
                texto_imc_cri.value = adolec_normal
            elif imc > 20.4 and imc < 22.7:
                normal_3.opacity = 1
                texto_imc_cri.value = adolec_normal
            #peso abaixo
            #magro_3 é mais perto do noraml
            elif imc > 16.8 and imc < 17.6:
                magro_3.opacity = 1
                texto_imc_cri.value = adolec_magro
            elif imc > 16.1 and imc < 16.9:
                magro_2.opacity = 1
                texto_imc_cri.value = adolec_magro
            elif imc < 16.2:
                magro_1.opacity = 1
                texto_imc_cri.value = adolec_magro
            #peso acima
            #gordo_1 é mais perto do normal/SOBRE PESO
            elif imc > 22.7 and imc < 26.4:
                gordo_1.opacity = 1
                texto_imc_cri.value = adolec_gordo
            elif imc > 26.3 and imc < 28.5:
                gordo_2.opacity = 1
                texto_imc_cri.value = adolec_gordo
            elif imc > 28.4:
                gordo_3.opacity = 1
                texto_imc_cri.value = adolec_gordo
        #16 ANOS
        elif cri_idade.value == '16': 
            #peso nornal
            #normal_2 é central
            if imc > 19.4 and imc < 21.9:
                normal_2.opacity = 1
                texto_imc_cri.value = adolec_normal
            elif imc > 18.1 and imc < 19.5:
                normal_1.opacity = 1
                texto_imc_cri.value = adolec_normal
            elif imc > 21.8 and imc < 23.8:
                normal_3.opacity = 1
                texto_imc_cri.value = adolec_normal
            #peso abaixo
            #magro_3 é mais perto do noraml
            elif imc > 17.3 and imc < 18.2:
                magro_3.opacity = 1
                texto_imc_cri.value = adolec_magro
            elif imc > 16.6 and imc < 17.4:
                magro_2.opacity = 1
                texto_imc_cri.value = adolec_magro
            elif imc < 16.7:
                magro_1.opacity = 1
                texto_imc_cri.value = adolec_magro
            #peso acima
            #gordo_1 é mais perto do normal/SOBRE PESO
            elif imc > 23.7 and imc < 27.3:
                gordo_1.opacity = 1
                texto_imc_cri.value = adolec_gordo
            elif imc > 27.2 and imc < 30.3:
                gordo_2.opacity = 1
                texto_imc_cri.value = adolec_gordo
            elif imc > 30.2:
                gordo_3.opacity = 1
                texto_imc_cri.value = adolec_gordo
        #17 ANOS
        elif cri_idade.value == '17': 
            #peso nornal
            #normal_2 é central
            if imc > 20.5 and imc < 22.5:
                normal_2.opacity = 1
                texto_imc_cri.value = adolec_normal
            elif imc > 18.6 and imc < 20.6:
                normal_1.opacity = 1
                texto_imc_cri.value = adolec_normal
            elif imc > 22.4 and imc < 24.5:
                normal_3.opacity = 1
                texto_imc_cri.value = adolec_normal
            #peso abaixo
            #magro_3 é mais perto do noraml
            elif imc > 17.8 and imc < 18.7:
                magro_3.opacity = 1
                texto_imc_cri.value = adolec_magro
            elif imc > 17.1 and imc < 17.9:
                magro_2.opacity = 1
                texto_imc_cri.value = adolec_magro
            elif imc < 17.2:
                magro_1.opacity = 1
                texto_imc_cri.value = adolec_magro
            #peso acima
            #gordo_1 é mais perto do normal/SOBRE PESO
            elif imc > 24.4 and imc < 28.1:
                gordo_1.opacity = 1
                texto_imc_cri.value = adolec_gordo
            elif imc > 28 and imc < 30.3:
                gordo_2.opacity = 1
                texto_imc_cri.value = adolec_gordo
            elif imc > 30.2:
                gordo_3.opacity = 1
                texto_imc_cri.value = adolec_gordo
        #18 ANOS
        elif cri_idade.value == '18': 
            #peso nornal
            #normal_2 é central
            if imc > 20.7 and imc < 23.3:
                normal_2.opacity = 1
                texto_imc_cri.value = adolec_normal
            elif imc > 19.1 and imc < 20.8:
                normal_1.opacity = 1
                texto_imc_cri.value = adolec_normal
            elif imc > 23.2 and imc < 25.1:
                normal_3.opacity = 1
                texto_imc_cri.value = adolec_normal
            #peso abaixo
            #magro_3 é mais perto do noraml
            elif imc > 18.2 and imc < 19.2:
                magro_3.opacity = 1
                texto_imc_cri.value = adolec_magro
            elif imc > 17.4 and imc < 18.3:
                magro_2.opacity = 1
                texto_imc_cri.value = adolec_magro
            elif imc < 17.5:
                magro_1.opacity = 1
                texto_imc_cri.value = adolec_magro
            #peso acima
            #gordo_1 é mais perto do normal/SOBRE PESO
            elif imc > 25 and imc < 28.8:
                gordo_1.opacity = 1
                texto_imc_cri.value = adolec_gordo
            elif imc > 28.7 and imc < 31.3:
                gordo_2.opacity = 1
                texto_imc_cri.value = adolec_gordo
            elif imc > 31.2:
                gordo_3.opacity = 1
                texto_imc_cri.value = adolec_gordo
        #DIALOGO DE ALERTA
        def limpa_alert(e):
            texto.open = False
            page.update()

        texto = ft.AlertDialog(content= ft.Column(controls=[
                    ft.Text('Cálculo realizado com dados fornecidos pela Organização Mundial da Saúde. As crianças e adolescentes estão crescendo todo o tempo, então a análise é mais conplexa que o IMC dos adultos, por isso o resultado vem de uma curva média de crescimento para cada idade.\nQualquer dúvida sempre consulte um médico.\n\nFeche para ver o resultado.', size=20),
                    ft.ElevatedButton('Fechar', bgcolor='#008000', on_click=limpa_alert)],width=500,height=300),bgcolor='green',shadow_color='#008000')
        page.overlay.append(texto)
        texto.open = True
        page.update()

    
    def main_adulto(e):
        peso = round(float(adulto_peso.value),2)
        altura = round(float(adulto_altura.value),2)
        imc_ad = round(peso/altura**2, 1)
        #peso ideal
        if imc_ad > 18.5 and imc_ad < 25.1:
           ideal.opacity = 1
           texto_imc_ad.value = f'Seu IMC é {imc_ad}, esse valor está dentro de uma faixa de resultado considerado ideal para a relação peso/altura.\nLembre-se, sua saúde depende de outros fatores, consulte seu médico regularmente para avaliações e exames de rotina.'
        #magreza leve
        elif imc_ad > 16.9 and imc_ad < 18.6:
           magro_leve.opacity = 1
           texto_imc_ad.value = f'Seu IMC é {imc_ad}, esse valor corresponde a uma magreza leve. Se atente para que essa perda de massa não seja uma tendência, se estiver estabilizada não há grandes problemas.\nLembre-se, um médico é sempre o profissional mais adequado para avaliar o resultado do IMC.'
        #magreza moderada
        elif imc_ad > 15.9 and imc_ad < 17:
           magro_moderado.opacity = 1
           texto_imc_ad.value = f'Seu IMC é {imc_ad}, esse valor corresponde a uma magreza moderada. Fique atento, já que quanto mais a seta se afasta da área verde mais preocupante é o resultado do IMC. Consulte seu médico para melhor avaliar a situação.'
        #magreza grave
        elif imc_ad < 16:
           magro_grave.opacity = 1
           texto_imc_ad.value = f'Seu IMC é {imc_ad}, esse valor corresponde a uma magreza grave. Neste caso, provavelmente, o corpo não tem as substâncias necessárias para mantê-lo saudável, haverá deficiência de vitaminas e nutrientes fundamentais para o bom funcionamento do corpo. Consulte seu médico para avaliação e exames. '
        #sobrepeso
        elif imc_ad > 25 and  imc_ad < 30:
           sobre_peso.opacity = 1
           texto_imc_ad.value = f'seu IMC é {imc_ad}, esse valor corresponde a um sobrepeso. Você ainda não é considerado obeso, mas com certeza é mais fácil ganhar peso que perder, por isso fique atento. Evite açucar, gordura em excesso e consulte seu médico para uma melhor avaliação.'
        #obesidade grau I
        elif imc_ad > 29.9 and  imc_ad < 35:
           obesidade_1.opacity = 1
           texto_imc_ad.value = f'seu IMC é {imc_ad}, esse valor corresponde a obesidade grau I. Você está ultrapassando uma barreira perigosa, um médico poderá lhe orientar em como traçar um plano para perda de peso de maneira saúdavel.\nNunca faça isso por conta própria, fórmulas mágicas podem causar sérios danos a sua saúde. '
        #obesidade grau II
        elif imc_ad > 34.9 and  imc_ad < 40:
           obesidade_severa.opacity = 1
           texto_imc_ad.value = f'seu IMC é {imc_ad}, esse valor corresponde a obesidade severa. Procure imediatamente um médico para tomar providências quanto a diminuição do seu peso. Não espere!!! Esta situação atual pode causar danos severos a seu corpo.'
        #obesidade grau III
        elif imc_ad > 39.9:
           obesidade_morbida.opacity = 1
           texto_imc_ad.value = f'seu IMC é {imc_ad}, esse valor corresponde a obesidade morbida. Procure imediatamente um médico para tomar providências quanto a diminuição do seu peso. Não espere!!! Esta situação atual pode causar danos severos a seu corpo.'


        def limpa_alert(e):
            texto.open = False
            page.update()

        texto = ft.ResponsiveRow(controls=[ft.AlertDialog(content= ft.Column(controls=[
                    ft.ElevatedButton('Fechar', bgcolor='#008000', on_click=limpa_alert),
                    ft.Text('Cálculo realizado com dados fornecidos pela Organização Mundial da Saúde. O IMC não leva em consideração a taxa de massa muscular e a quantidade de gordura no corpo.\nSempre consulte um médico antes de iniciar qualquer ação para ganhar ou perder peso.\n\nFeche para ver o resultado.', size=20),
                    ],width=500, height=300),bgcolor='green',)])
        page.overlay.append(texto)
        texto.open = True
        page.update()
        
    def main_idoso(e):
        peso = round(float(idoso_peso.value),2)
        altura = round(float(idoso_altura.value),2)
        imc_ad = round(peso/altura**2, 1)
        #peso ideal
        if imc_ad > 21.9 and imc_ad < 27.1:
           id_ideal.opacity = 1
           texto_imc_id.value = f'seu IMC é {imc_ad}, esse valor está dentro de uma faixa de resultado considerado ideal para a relação peso/altura.\nLembre-se, sua saúde depende de outros fatores, consulte seu médico regularmente para avaliações e exames de rotina.'
        #magreza leve
        elif imc_ad > 16.9 and imc_ad < 22:
           id_magro_leve.opacity = 1
           texto_imc_id.value = f'seu IMC é {imc_ad}, esse valor corresponde a uma magreza leve. Se atente para que essa perda de massa não seja uma tendência, se estiver estabilizada não há grandes problemas.\nLembre-se, um médico é sempre o profissional mais adequado para avaliar o resultado do IMC.'
        #magreza moderada
        elif imc_ad > 15.9 and imc_ad < 17:
           id_magro_moderado.opacity = 1
           texto_imc_id.value = f'seu IMC é {imc_ad}, esse valor corresponde a uma magreza moderada. Fique atento, já que quanto mais a seta se afasta da área verde mais preocupante é o resultado do IMC. Consulte seu médico para melhor avaliar a situação.'
        #magreza grave
        elif imc_ad < 16:
           id_magro_grave.opacity = 1
           texto_imc_id.value = f'seu IMC é {imc_ad}, esse valor corresponde a uma magreza grave. Neste caso, provavelmente, o corpo não tem as substâncias necessárias para mantê-lo saudável, haverá deficiência de vitaminas e nutrientes fundamentais para o bom funcionamento do corpo. Consulte seu médico para avaliação e exames. '
        #sobrepeso
        elif imc_ad > 27 and  imc_ad < 30:
           id_sobre_peso.opacity = 1
           texto_imc_id.value = f'seu IMC é {imc_ad}, esse valor corresponde a um sobrepeso. Você ainda não é considerado obeso, mas com certeza é mais fácil ganhar peso que perder, por isso fique atento. Evite açucar, gordura em excesso e consulte seu médico para uma melhor avaliação.'
        #obesidade grau I
        elif imc_ad > 29.9 and  imc_ad < 35:
           id_obesidade_1.opacity = 1
           texto_imc_id.value = f'seu IMC é {imc_ad}, esse valor corresponde a obesidade grau I. Você está ultrapassando uma barreira perigosa, um médico poderá lhe orientar em como traçar um plano para perda de peso de maneira saúdavel.\nNunca faça isso por conta própria, fórmulas mágicas podem causar sérios danos a sua saúde. '
        #obesidade grau II
        elif imc_ad > 34.9 and  imc_ad < 40:
           id_obesidade_severa.opacity = 1
           texto_imc_id.value = f'seu IMC é {imc_ad}, esse valor corresponde a obesidade severa. Procure imediatamente um médico para tomar providências quanto a diminuição do seu peso. Não espere!!! Esta situação atual pode causar danos severos a seu corpo.'
        #obesidade grau III
        elif imc_ad > 39.9:
           id_obesidade_morbida.opacity = 1
           texto_imc_id.value = f'seu IMC é {imc_ad}, esse valor corresponde a obesidade morbida. Procure imediatamente um médico para tomar providências quanto a diminuição do seu peso. Não espere!!! Esta situação atual pode causar danos severos a seu corpo.'

        def limpa_alert(e):
            texto.open = False
            page.update()

        texto = ft.AlertDialog(content= ft.Column(controls=[
                    ft.Text('Cálculo realizado com dados fornecidos pela Organização Mundial da Saúde. Acima dos 60 anos o cálculo do IMC é um pouco diferente, a Organização Mundial da Saúde muda os parâmetros de peso considerados adequados para esta faixa etária. De qualquer forma qualquer ação para aumentar ou diminuir peso deve ser acompanhado pelo seu médico.\n\nFeche para ver o resultado.', size=20),
                    ft.ElevatedButton('Fechar', bgcolor='#008000', on_click=limpa_alert)],width=500,height=300),bgcolor='green',)
        page.overlay.append(texto)
        texto.open = True
        page.update()
    #limpar criança
    def limpar(e):
        cri_idade.value = None
        cri_altura.value = None
        cri_peso.value = None
        normal_1.opacity = 0
        normal_2.opacity = 0
        normal_3.opacity = 0
        magro_1.opacity = 0
        magro_2.opacity = 0
        magro_3.opacity = 0
        gordo_1.opacity = 0
        gordo_2.opacity = 0
        gordo_3.opacity = 0
        texto_imc_cri.value = '  Resultado do Índice de Massa Muscular'
        page.update()

    def limpar_adulto(e):
        ideal.opacity = 0
        magro_leve.opacity = 0
        magro_moderado.opacity = 0
        magro_grave.opacity = 0
        sobre_peso.opacity = 0
        obesidade_1.opacity = 0
        obesidade_severa.opacity = 0
        obesidade_morbida.opacity = 0
        adulto_altura.value = None
        adulto_peso.value = None
        texto_imc_ad.value = '  Resultado do Índice de Massa Muscular'
        page.update()

    def limpar_idoso(e):
        id_ideal.opacity = 0
        id_magro_leve.opacity = 0
        id_magro_moderado.opacity = 0
        id_magro_grave.opacity = 0
        id_sobre_peso.opacity = 0
        id_obesidade_1.opacity = 0
        id_obesidade_severa.opacity = 0
        id_obesidade_morbida.opacity = 0
        idoso_altura.value = None
        idoso_peso.value = None
        texto_imc_id.value = '  Resultado do Índice de Massa Muscular'
        page.update()
 
    #criando 3 faixas etarias
    abas_etarias = ft.Tabs(
        indicator_color='white',
        label_color='white',
        unselected_label_color='#008000',
        expand=1,
        tabs=[
            ft.Tab(
                text='De 5 a 18 anos',
                content=ft.Container(
                    padding=10,
                    content=ft.Column(controls=[
                                    ft.ResponsiveRow(controls=[
                                            cri_idade := ft.Dropdown(
                                                width=150,height=50,label='Idade / Anos',label_style=ft.TextStyle(color='white'),
                                                border_color='white',text_size=16,border_radius=20,col='4',
                                                options=[
                                                    ft.dropdown.Option(text=f'{num}')for num in range(5,19)
                                                ],color='white',bgcolor='#008000'
                                            ),
                                            cri_altura := ft.Dropdown(
                                                width=150,height=50,label='Altura / Metro',label_style=ft.TextStyle(color='white'),
                                                border_color='white',text_size=16,border_radius=20,col='4',
                                                options=[
                                                    ft.dropdown.Option(text=f'{alt}')for alt in np.round(np.arange(0.80,2.00,0.01),3)
                                                ],color='white', bgcolor='#008000'
                                            ),  
                                            cri_peso := ft.Dropdown(
                                                width=150,height=50,label='Peso / Kilos',label_style=ft.TextStyle(color='white'),
                                                border_color='white',text_size=16,border_radius=20,col='4',
                                                options=[
                                                    ft.dropdown.Option(text=f'{peso}')for peso in np.round(np.arange(7,100,0.2),3)
                                                ],color='white', bgcolor='#008000'
                                            ),  
                                    ]),
                                    ft.ResponsiveRow(controls=[ft.ElevatedButton(text='Calcular',bgcolor='#98FB98',color='#008000',on_click=main_cri,col='4'),
                                    ft.ElevatedButton(text='Limpar',bgcolor='#98FB98',color='#008000',on_click=limpar,col='4'),
                                    ft.Text('Limpe antes de nova pesquisa',col='4',color='red')]),
                                    
                                    ft.Row(controls=[
                                        ft.Container(ft.Text(value='Está Magro'),bgcolor='#0000CD',height=40, expand=1),
                                        ft.Container(ft.Text(value='Peso Normal'),bgcolor='#008000',height=40, expand=1),
                                        ft.Container(ft.Text(value='Obsidade Cuidado'),height=40, expand=1, gradient=ft.LinearGradient(
                                                                                    begin=ft.alignment.center_left,
                                                                                    end=ft.alignment.center_right,
                                                                                    colors=['#FFA500', '#FF0000'],

                                        )),
                                    ], spacing=0),
                                    #CLIP_BEHAVIOR= permite que a imagem sai do conteiner e invada outros componentes
                                    #EXPAND= dá uma parte do espaço para cada imagem
                                    #SCALE= aumenta o tamanho da imagem
                                    ft.Container(clip_behavior=ft.ClipBehavior.NONE,gradient=ft.LinearGradient(
                                                    begin=ft.alignment.bottom_center,
                                                    end=ft.alignment.top_center,
                                                    colors=['#DCDCDC', '#B8860B']),height=20,content=ft.Row(controls=[
                                        magro_1 := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                scale=ft.Scale(scale=4),expand=1,opacity=0),
                                        magro_2 := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                scale=ft.Scale(scale=4),expand=1,opacity=0),
                                        magro_3 := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                scale=ft.Scale(scale=4),expand=1,opacity=0),
                                        normal_1 := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                scale=ft.Scale(scale=4),expand=1,opacity=0),
                                        normal_2 := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                scale=ft.Scale(scale=4),expand=1,opacity=0),
                                        normal_3 := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                scale=ft.Scale(scale=4),expand=1,opacity=0),
                                        gordo_1 := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                scale=ft.Scale(scale=4),expand=1,opacity=0),
                                        gordo_2 := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                scale=ft.Scale(scale=4),expand=1,opacity=0),
                                        gordo_3 := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                scale=ft.Scale(scale=4),expand=1,opacity=0),
                                    ])),
                                    texto_imc_cri := ft.Text(value='  Resultado do Índice de Massa Corporal', size=16, color='#0000CD',height=300),

                        ]
                        )
                )
            ),
            ft.Tab(
                text='Adulto',
                content=ft.Container(
                    # height=,
                    padding=10,
                    content=ft.Column(controls=[
                                        
                                        ft.Row([
                                            adulto_altura := ft.Dropdown(
                                                width=150,height=50,label='Altura',label_style=ft.TextStyle(color='white'),
                                                border_color='white',text_size=16,border_radius=20,
                                                options=[
                                                ft.dropdown.Option(text=f'{alt}')for alt in np.round(np.arange(1.20,2.20,0.01),3)
                                                ],color='white', bgcolor='#008000'
                                            ),  
                                            adulto_peso := ft.Dropdown(
                                                width=150,height=50,label='peso',label_style=ft.TextStyle(color='white'),
                                                border_color='white',text_size=16,border_radius=20,
                                                options=[
                                                ft.dropdown.Option(text=f'{peso}')for peso in np.round(np.arange(30,180,0.2),3)
                                                ],color='white', bgcolor='#008000'
                                            ),  
                                        ]),
                                            ft.ResponsiveRow(controls=[ft.ElevatedButton(text='Calcular',bgcolor='#98FB98',color='#008000',on_click=main_adulto,col='4'),
                                            ft.ElevatedButton(text='Limpar',bgcolor='#98FB98',color='#008000',on_click=limpar_adulto,col='4'),
                                            ft.Text('Limpe antes de nova pesquisa',col='4',color='red')]),
                                    
                                            ft.ResponsiveRow(controls=[
                                                ft.Container(ft.Text(value='Está Magro'),bgcolor='#0000CD',height=40, col='4'),
                                                ft.Container(ft.Text(value='Peso Normal'),bgcolor='#008000',height=40, col='2'),
                                                ft.Container(ft.Text(value='Obsidade Cuidado'),height=40, col='6', gradient=ft.LinearGradient(
                                                                                            begin=ft.alignment.center_left,
                                                                                            end=ft.alignment.center_right,
                                                                                            colors=['#FFA500', '#FF0000'],

                                                )),
                                            ], spacing=0),
                                            #CLIP_BEHAVIOR= permite que a imagem sai do conteiner e invada outros componentes
                                            #EXPAND= dá uma parte do espaço para cada imagem
                                            #SCALE= aumenta o tamanho da imagem
                                            ft.Container(clip_behavior=ft.ClipBehavior.NONE,gradient=ft.LinearGradient(
                                                        begin=ft.alignment.bottom_center,
                                                        end=ft.alignment.top_center,
                                                        colors=['#DCDCDC', '#B8860B']),height=20,content=ft.Row(controls=[
                                                magro_grave := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                        scale=ft.Scale(scale=4),expand=1,opacity=0),
                                                magro_moderado := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                        scale=ft.Scale(scale=4),expand=1,opacity=0),
                                                magro_leve := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                        scale=ft.Scale(scale=4),expand=1,opacity=0),
                                                ideal := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                        scale=ft.Scale(scale=4),expand=1,opacity=0),
                                                sobre_peso := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                        scale=ft.Scale(scale=4),expand=1,opacity=0),
                                                obesidade_1 := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                        scale=ft.Scale(scale=4),expand=1,opacity=0),
                                                obesidade_severa := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                        scale=ft.Scale(scale=4),expand=1,opacity=0),
                                                obesidade_morbida := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                        scale=ft.Scale(scale=4),expand=1,opacity=0),
                                            ])),
                                            texto_imc_ad := ft.Text(value='  Resultado do Índice de Massa Corporal', size=16, color='#0000CD',height=300),

                                    ]
                                )
                ) 
            ),
            ft.Tab(
                text='Acima de 60 anos',
                content=ft.Container(
                    # height=,
                    padding=10,
                    content=ft.Column(controls=[
                                        
                                        ft.Row([
                                            idoso_altura := ft.Dropdown(
                                                width=150,height=50,label='Altura',label_style=ft.TextStyle(color='white'),
                                                border_color='white',text_size=16,border_radius=20,
                                                options=[
                                                ft.dropdown.Option(text=f'{alt}')for alt in np.round(np.arange(1.20,2.20,0.01),3)
                                                ],color='white', bgcolor='#008000'
                                            ),  
                                            idoso_peso := ft.Dropdown(
                                                width=150,height=50,label='peso',label_style=ft.TextStyle(color='white'),
                                                border_color='white',text_size=16,border_radius=20,
                                                options=[
                                                ft.dropdown.Option(text=f'{peso}')for peso in np.round(np.arange(30,180,0.2),3)
                                                ],color='white', bgcolor='#008000'
                                            ),  
                                        ]),
                                            ft.ResponsiveRow(controls=[ft.ElevatedButton(text='Calcular',bgcolor='#98FB98',color='#008000',on_click=main_idoso,col='4'),
                                            ft.ElevatedButton(text='Limpar',bgcolor='#98FB98',color='#008000',on_click=limpar_idoso,col='4'),
                                            ft.Text('Limpe antes de nova pesquisa',col='4',color='red')]),
                                    
                                            ft.ResponsiveRow(controls=[
                                                ft.Container(ft.Text(value='Está Magro'),bgcolor='#0000CD',height=40, col='4'),
                                                ft.Container(ft.Text(value='Peso Normal'),bgcolor='#008000',height=40, col='2'),
                                                ft.Container(ft.Text(value='Obsidade Cuidado'),height=40, col='6', gradient=ft.LinearGradient(
                                                                                            begin=ft.alignment.center_left,
                                                                                            end=ft.alignment.center_right,
                                                                                            colors=['#FFA500', '#FF0000'],

                                                )),
                                            ], spacing=0),
                                            #CLIP_BEHAVIOR= permite que a imagem sai do conteiner e invada outros componentes
                                            #EXPAND= dá uma parte do espaço para cada imagem
                                            #SCALE= aumenta o tamanho da imagem
                                            ft.Container(clip_behavior=ft.ClipBehavior.NONE,gradient=ft.LinearGradient(
                                                        begin=ft.alignment.bottom_center,
                                                        end=ft.alignment.top_center,
                                                        colors=['#DCDCDC', '#B8860B']),height=20,content=ft.Row(controls=[
                                                id_magro_grave := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                        scale=ft.Scale(scale=4),expand=1,opacity=0),
                                                id_magro_moderado := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                        scale=ft.Scale(scale=4),expand=1,opacity=0),
                                                id_magro_leve := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                        scale=ft.Scale(scale=4),expand=1,opacity=0),
                                                id_ideal := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                        scale=ft.Scale(scale=4),expand=1,opacity=0),
                                                id_sobre_peso := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                        scale=ft.Scale(scale=4),expand=1,opacity=0),
                                                id_obesidade_1 := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                        scale=ft.Scale(scale=4),expand=1,opacity=0),
                                                id_obesidade_severa := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                        scale=ft.Scale(scale=4),expand=1,opacity=0),
                                                id_obesidade_morbida := ft.Image(src='IMC/app_imc/assets/seta 6.png',
                                                        scale=ft.Scale(scale=4),expand=1,opacity=0),
                                            ])),
                                            texto_imc_id := ft.Text(value='  Resultado do Índice de Massa Corporal', size=16, color='#0000CD',height=300),

                                    ]
                                )
                ) 
            ),


            
        ]
    )
    
    def pag_contato(e):
        pagina.controls = texto_contato,contatos
        page.update()

    def pag_cadastro(e):
        pagina.controls = texto_cadastro,cadastros
        page.update()

    def pag_carrinho(e):
        pagina.controls = texto_carrinho,carrinhos
        page.update()
    
    def pag_home(e):
        pagina.controls = texto_fantasma,abas_produtos
        page.update()
    texto_fantasma = ft.Text('')
        #TEXTOS INICIO DAS PAGINAS
    texto_contato = ft.Text('Contato',size=25,color='white',italic=True,text_align=ft.TextAlign.CENTER)
    texto_carrinho = ft.Text('Carrinho',size=25,color='white',italic=True,text_align=ft.TextAlign.CENTER)
    texto_cadastro = ft.Text('Login',size=25,color='white',italic=True,text_align=ft.TextAlign.CENTER)
    titulo_coluna_2 = ft.Text('SHOPPING IMC VIVA BEM',size=25,color='amber',italic=True,col=6)
    barra_opcao = ft.Container(
            col='12',bgcolor='black',padding=20,
            content=ft.ResponsiveRow(controls=[
            ft.ElevatedButton(text='Home',col='2.5',on_click=pag_home),
            ft.ElevatedButton(text='Contato',col='3.5',on_click=pag_contato),
            ft.ElevatedButton(text='Carrinho',col='3.5',on_click=pag_carrinho),
            ft.ElevatedButton(text='Login',col='2.5',on_click=pag_cadastro),
            ],spacing=5)
            )

    #PAGINAS
    grade_prod_pele = card_venda_pele(page)
    grade_produto_pele = ft.Container(content=grade_prod_pele,padding=10)
    grade_prod_cuidPessoais = card_venda_cuidPessoais(page)
    grade_produto_cuidPessoais = ft.Container(content=grade_prod_cuidPessoais,padding=10)
    grade_prod_beleza = card_venda_beleza(page)
    grade_produto_beleza = ft.Container(content=grade_prod_beleza,padding=10)
    grade_prod_emagrec = card_venda_emagrec(page)
    grade_produto_emagrec = ft.Container(content=grade_prod_emagrec,padding=10)
    contat = contato(page)
    contatos = ft.Container(content=contat)
    cadast = cadastro(page)
    cadastros = ft.Container(content=cadast)
    carrinh = carrinho(page)
    carrinhos = ft.Container(content=carrinh)

    texto_coluna_2 = ft.Text('Explore nossa seleção de saúde e beleza, pensada para oferecer o melhor em cuidados pessoais.\nCuidar de você é simples – comece agora!',size=20,color='white',italic=True)#weight='BOLD' texto em negrito
    pagina_inicial_emagrec = ft.Column(controls=[texto_coluna_2,grade_produto_emagrec])
    pagina_inicial_beleza = ft.Column(controls=[texto_coluna_2,grade_produto_beleza])
    pagina_inicial_cuidPessoais = ft.Column(controls=[texto_coluna_2,grade_produto_cuidPessoais])
    pagina_inicial_pele = ft.Column(controls=[texto_coluna_2,grade_produto_pele])


    #ABAS DOS TIPOS DE PRODUTO
    abas_produtos = ft.Tabs(
        #deixa selecionado o primeiro da esquerda
        selected_index=0,
        #cor da barra selecionada
        indicator_color=ft.colors.AMBER,
        #cor do texto da aba selecionada
        label_color=ft.colors.AMBER,
        tabs=[
            ft.Tab(text='Emagrecedor', content=pagina_inicial_emagrec),
            ft.Tab(text='Beleza', content=pagina_inicial_beleza),
            ft.Tab(text='Cuidados Pessoais', content=pagina_inicial_cuidPessoais),
            ft.Tab(text='Pele', content=pagina_inicial_pele),
        ],col='12'
    )
    pagina = ft.Column(controls=[abas_produtos],col='12')

    #COLUNAS DO APLICATIVO
    coluna_1 = ft.Container(
        padding=10,
        border_radius=20,
        content= ft.Column(controls=
                [ft.Row([ft.Image(src='IMC/app_imc/assets/logo_imc_semF.png',
                        width=80,height=80,fit=ft.ImageFit.CONTAIN),
                ft.Text('IMC VIVA BEM',bgcolor='#A9A9A9',size=30,color='#008000',weight='BOLD', italic=True)]),
                ft.Text('Vamos ver como está sua saúde? Preencha os dados abaixo para descobrir como está seu peso em relação a sua altura.\nIMC - Índice de Massa Corporal',
                        size=16,color='#008000',weight='BOLD'),
                ft.Text('ESCOLHA SUA FAIXA DE IDADE', color='#0000CD'),
                abas_etarias, 
                #ft.Container(expand=True),
                ft.Text('Dados OMS - Organização Mundial da Saúde',size=14, color='#008000')
                ]),bgcolor='#A9A9A9',col={'sm':12,'md':3.5,'lg':3.5},aspect_ratio=9/16
    )

    frete_gratis=ft.Image(src='IMC/app_imc/assets/frete_gratis.png',scale=ft.Scale(scale=3),col=6)
    titulo_2 = ft.Container(content=(ft.ResponsiveRow(controls=[titulo_coluna_2,frete_gratis],col=12)),height=100,clip_behavior=ft.ClipBehavior.NONE)


    coluna_2 = ft.Container(
        padding=10,
        content= ft.Column(controls=
                [
                    titulo_2,
                    barra_opcao,
                    pagina
                ],), bgcolor=ft.colors.BLACK,col={'sm':12,'md':8.5,'lg':8.5}#,aspect_ratio=9/16
    )
    
    #ADICIONANDO OBJETOS A PAGINA
    layout = ft.Container(
        content= ft.ResponsiveRow(
            #espaço entre as colunas
            spacing=0,
            columns=12,
            controls=[
                coluna_1,
                coluna_2
            ]
        )
    )
    page.add(layout)

#commando roda o app e abre no  navegador
if __name__ == '__main__':
    ft.app(target=main)#, view=ft.WEB_BROWSER)
