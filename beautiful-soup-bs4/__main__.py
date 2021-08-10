# -*- coding: utf-8 -*-

# importando bibliotecas responsáveis para o scrapping básico
import requests
from bs4 import BeautifulSoup


def main():
    '''
    Função principal que, realiza todo o escopo de código da conversão.
    '''

    # Realiza uma requisição em um HTML desejado
    page = requests.get('https://pythonacademy.com.br')

    # Instancia a classe BEautifulSoup criando uma estrutura hierárquica do HTML
    sopa = BeautifulSoup(page.text, 'html.parser')

    # Scrapando todos os elementos que contenham como classe 'card-title'
    titulos_artigos = sopa.findAll(class_='card-title')

    # Iterando os títulos dos cards
    for titulo in titulos_artigos:
        print(titulo.get_text().strip())


if __name__ == '__main__':
    main()
