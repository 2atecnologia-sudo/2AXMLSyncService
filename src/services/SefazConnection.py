class SefazConnection:

    def __init__(self):

        self.certificado = None
        self.timeout = 30

    # -------------------------------------------------

    def configurarCertificado(self, certificado):

        self.certificado = certificado

    # -------------------------------------------------

    def enviar(self, url, soap):

        print("=" * 60)
        print("ENVIO PARA SEFAZ")
        print("=" * 60)

        print("URL:")
        print(url)

        print()

        print("SOAP:")
        print(soap)

        print()

        # Aqui amanhã faremos o envio HTTPS real
        return None