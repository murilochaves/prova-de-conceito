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


def main():
    # Cria nosso objeto iterável
    objeto_fibonacci = Fibonacci(maximo=1000000)

    # Itera nossa sequência
    for fibonacci in objeto_fibonacci:
        print('Sequência: {0}'.format(fibonacci))


if __name__ == '__main__':
    main()
