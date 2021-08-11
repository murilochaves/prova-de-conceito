# -*- coding: utf-8 -*-

from pytube import YouTube
import os


def main_video():
    '''
    Função principal que, realiza todo o escopo de código da conversão.
    '''

    # Cria objeto com URL do vídeo a ser baixado
    video = YouTube('https://www.youtube.com/watch?v=r337rEAvtPQ')

    # Configura a melhor qualidade de vídeo
    stream = video.streams.get_highest_resolution()

    # Faz o download do vídeo e salva na pasta 'saída'
    stream.download(output_path='./saida')


def main_audio():
    '''
    Função principal que, realiza todo o escopo de código da conversão.
    '''

    # Cria objeto com URL do vídeo a ser baixado
    video = YouTube('https://www.youtube.com/watch?v=r337rEAvtPQ')

    # Filtrando apenas o áudio do vídeo
    stream = video.streams.filter(only_audio=True)

    # Faz o download do audio e salva na pasta 'saída'
    stream[0].download(output_path='./saida')


if __name__ == '__main__':
    main_audio()
