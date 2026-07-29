from requests_schannel.adapters import create_session
from src.config.ConfigManager import ConfigManager

class SefazConnection:

    def __init__(self):

        self.certificado = None
        self.timeout = 30
        self.session = None
        self.config = ConfigManager()

    # -------------------------------------------------

    def configurarCertificado(self, certificado):

        self.certificado = certificado

    # -------------------------------------------------

    # -------------------------------------------------

    def criarSessaoHTTPS(self):

        print("=" * 60)
        print("CRIANDO SESSÃO HTTPS")
        print("=" * 60)

        thumbprint = self.config.get(
            "CERTIFICADO",
            "thumbprint",
            ""
        )

        print("Thumbprint:", thumbprint)

        self.session = create_session(
            client_cert_thumbprint=thumbprint
        )

        print("✓ Sessão HTTPS criada com sucesso.")



    def enviar(self, url, soap):

        if self.session is None:

            self.criarSessaoHTTPS()

        print("=" * 60)
        print("ENVIANDO SOAP PARA A SEFAZ")
        print("=" * 60)

        print("URL:")
        print(url)
        print("SOAP:")
        print(soap)
        print()

        headers = {
            "Content-Type": 'application/soap+xml; charset=utf-8; action="http://www.portalfiscal.inf.br/nfe/wsdl/NFeDistribuicaoDFe/nfeDistDFeInteresse"',
            "SOAPAction": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeDistribuicaoDFe/nfeDistDFeInteresse"
        }

        try:

            response = self.session.post(
                url,
                data=soap.encode("utf-8"),
                headers=headers,
                timeout=self.timeout
            )

            print("=" * 60)
            print("RESPOSTA DA SEFAZ")
            print("=" * 60)

            print("HTTP:", response.status_code)
            print()
            print(response.text)

            return response

        except Exception as e:

            print("=" * 60)
            print("ERRO NA COMUNICAÇÃO")
            print("=" * 60)

            print(type(e).__name__)
            print(e)

            return None