# -*- coding: utf-8 -*-

class Fibonacci():
    def __init__(self, maximo=1000000):
        # Inicializa os dois primeiros números
        self.atual, self.proximo = 0, 1
        self.maximo = maximo

    def __iter__(self):
        # Retorna o objeto iterável (ele próprio: self)
        return self

    def __next__(self):
        # Fim da iteração, raise StopIteraction
        if self.atual > self.maximo:
            raise StopIteration

        # Salva o valor a ser retornado
        retorno = self.atual

        # Atualiza o próximo elemento da sequência
        self.atual, self.proximo = self.proximo, self.atual + self.proximo

        return retorno


def fibonacci(maximo):
    # Inicialização dos elementos
    atual, proximo = 0, 1

    # Define a condição de parada
    while atual < maximo:
        # Retorna o valor do elemento atual
        yield atual

        atual, proximo = proximo, atual + proximo


def main_iterador():
    '''
    Função principal que, realiza todo o escopo de código da conversão.
    '''

    # Cria nosso objeto iterável
    objeto_fibonacci = Fibonacci(maximo=1000000)

    # Itera nossa sequência
    for fibonacci in objeto_fibonacci:
        print('Sequência: {0}'.format(fibonacci))


def main_gerador():
    '''
    Função principal que, realiza todo o escopo de código da conversão.
    '''

    # Cria nosso objeto iterável
    fibonacci_generator = Fibonacci(1000000)

    # Mostra na tela toda a sequência
    for numero_fibonacci in fibonacci_generator:
        print(numero_fibonacci)


if __name__ == '__main__':
    main_gerador()
