# -*- coding: utf-8 -*-

from tqdm import tqdm


def main():
    '''
    Função principal que, realiza todo o escopo de código da conversão.
    '''

    numeros = range(int(10e7))

    for i in tqdm(numeros, colour='gray', desc='Processando'):
        pass


if __name__ == '__main__':
    main()
