from urllib import response

from src.config.ConfigManager import ConfigManager
from src.services.SefazConnection import SefazConnection
from src.services.SefazSoapBuilder import SefazSoapBuilder


class SefazClient:

    def __init__(self):

        self.certificado = None
        self.conectado = False

        # Configurações da SEFAZ
        self.uf = "35"              # São Paulo
        self.ambiente = "1"         # 1=Produção | 2=Homologação
        self.versao = "1.01"

        self.url = ""

        self.config = ConfigManager()

        self.tipoCertificado = ""
        self.arquivoCertificado = ""
        self.thumbprint = ""

    # -------------------------------------------------

    def configurarCertificado(self, certificado):

        self.certificado = certificado

    # -------------------------------------------------

    def configurarAmbiente(self, ambiente):

        self.ambiente = ambiente

        if ambiente == "1":

            print("Ambiente: Produção")

        else:

            print("Ambiente: Homologação")

    # -------------------------------------------------

    def carregarConfiguracao(self):

        self.tipoCertificado = self.config.get(
            "CERTIFICADO",
            "tipo",
            ""
        )

        self.arquivoCertificado = self.config.get(
            "CERTIFICADO",
            "arquivo",
            ""
        )

        self.thumbprint = self.config.get(
            "CERTIFICADO",
            "thumbprint",
            ""
        )

        print("Tipo:", self.tipoCertificado)
        print("Arquivo:", self.arquivoCertificado)
        print("Thumbprint:", self.thumbprint)

    # -------------------------------------------------

    def conectar(self):

        self.carregarConfiguracao()

        print("Conectando à SEFAZ...")

        builder = SefazSoapBuilder()

        ultimoNSU = self.config.get(
            "SEFAZ",
            "ultimonsu",
            "000000000000000"
        )

        print("Último NSU:", ultimoNSU)

        xml = builder.montarConsultaNSU(
            self.config.get("GERAL", "cnpj"),
           ultimoNSU
        )

    

        soap = builder.montarEnvelopeSOAP(xml)

        conexao = SefazConnection()

        response = conexao.enviar(
            "https://www1.nfe.fazenda.gov.br/NFeDistribuicaoDFe/NFeDistribuicaoDFe.asmx",
            soap
        )

        if response:

            dados = builder.lerRespostaDistribuicao(response.text)

            print("=" * 40)
            print("DADOS EXTRAÍDOS")
            print("=" * 40)
            print(dados)
            self.conectado = True

            return True

        return False
    # -------------------------------------------------

    def desconectar(self):

        self.conectado = False

        print("Desconectado.")

    # -------------------------------------------------

    def consultarUltimoNSU(self):

        if not self.conectado:

            raise Exception("Cliente não conectado.")

        print("Consultando último NSU...")

        return "000000000000000"

    # -------------------------------------------------

    def baixarDocumentos(self, ultimoNSU):

        if not self.conectado:

            raise Exception("Cliente não conectado.")

        print(f"Baixando documentos a partir do NSU {ultimoNSU}")

        return []