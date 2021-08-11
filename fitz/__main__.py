# -*- coding: utf-8 -*-

import fitz


def main():
    '''
    Função principal que, realiza todo o escopo de código da conversão.
    '''

    # Abra o arquivo PDF
    with fitz.open('./data/guia-do-mochileiro.pdf') as pdf:
        texto = ''

        for pagina in pdf:
            texto += pagina.getText()

    print(texto)


if __name__ == '__main__':
    main()
