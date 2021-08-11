# -*- coding: utf-8 -*-

# importando biblioteca responsável pela conversão
import speech_recognition as sr


def main():
    '''
    Função principal que, realiza todo o escopo de código da conversão.
    '''

    # Instancia a classe Recognizer
    r = sr.Recognizer()

    # Lê o arquivo de áudio
    with sr.AudioFile('./data/ola-mundo.wav') as arquivo:
        audio = r.record(arquivo)

    # Utiliza o Google Speech Recognition para fazer a conversão
    try:
        # Utiliza a chave de API padrão do próprio Speech Recognition
        # Para utilizar uma chave própria (recomendada), acesse a documentação
        texto = r.recognize_google(audio, language='pt-br')
        print(f'Google Speech Recognition acha que você disse: \n"{texto}"')

    except sr.UnknownValueError:
        print('Google Speech Recognition não entendeu seu áudio')

    except sr.RequestError as e:
        print(f'Não foi possível se conectar à API do Google. Erro: {str(e)}')


if __name__ == '__main__':
    main()
