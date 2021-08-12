# -*- coding: utf-8 -*-

import qrcode


def main():
    '''
    Função principal que, realiza todo o escopo de código da conversão.
    '''

    # Item que estará embutido no qrcode
    link = 'www.pythondicas.com'

    # Cria o objeto do QR Code
    qr_code = qrcode.QRCode(
        version=1,
        box_size=4,
        border=5
    )

    qr_code.add_data(link)
    qr_code.make(fit=True)

    # Cria a imagem com o QR Code
    imagem = qr_code.make_image(fill_color='#e50e52', back_color='#151718')
    imagem.show()


if __name__ == '__main__':
    main()
