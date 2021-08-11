# -*- coding: utf-8 -*-

import easyocr


def main():
    '''
    Função principal que, realiza todo o escopo de código da conversão.
    '''

    # Define Português como idioma padrão
    leitor = easyocr.Reader(['pt'])

    # Lê a imagem
    resultados = leitor.readtext(
        './data/guia-do-mochileiro.jpg', paragraph=False)

    # Itera sobre o resultado
    for resultado in resultados:
        print(
            f'Texto encontrado: \n',
            f'\tPosição: {resultado[0]}\n',
            f'\tTexto: {resultado[1]}\n',
        )


if __name__ == '__main__':
    main()
