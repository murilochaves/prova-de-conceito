# -*- coding: utf-8 -*-

# Importa bibliotecas necessárias
from PIL import Image
import os

def main():
    '''
    Função principal que, realiza todo o escopo de código da conversão.
    '''

    # Abre a imagem e realiza a conversão
    imagem = Image.open('./data/doguinho.png').convert('LA')

    # Imprime a imagem
    imagem.show()

    # Criando repositório de saída
    if not os.path.exists('./saida'):
        os.mkdir('./saida')

    # Salva a imagem
    imagem.save('./saida/doguinho_cinza.png')

    pass


if __name__ == '__main__':
    main()
