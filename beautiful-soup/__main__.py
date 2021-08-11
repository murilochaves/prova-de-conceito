# -*- coding: utf-8 -*-

# importando bibliotecas responsáveis para o scrapping básico
import requests
from bs4 import BeautifulSoup


def main_python_academy():
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


def main_fundamentus():
    '''
    Função principal que, realiza todo o escopo de código da conversão.
    '''

    headers = {'User-Agent': 'Mozilla/5.0'}

    # Busca o código HTML da página que quer analisar
    pagina = requests.get('https://fundamentus.com.br/fii_resultado.php', headers=headers)

    # Instancia o BeautifulSoup, passando o HTML no construtor e o parser
    soup = BeautifulSoup(pagina.text, 'html.parser')

    # Ache o dado que quer na página (passo 2)
    dados = soup.find('table', {'id': 'tabelaResultado'}).find('tbody').findAll('tr')

    # Agora e com você! ;)
    for fundo in dados:
        dados_fundo = fundo.find_all('td')
        print(
            f'[{dados_fundo[0].text}]\n'
            f'\tCotação: {dados_fundo[2].text}\n'
            f'\tSetor: {dados_fundo[1].text}\n'
            f'\tDY %: {dados_fundo[4].text}\n'
            f'\tP/VPA: {dados_fundo[5].text}\n'
        )
    

if __name__ == '__main__':
    main_fundamentus()
