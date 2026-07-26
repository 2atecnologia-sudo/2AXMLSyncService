class SefazClient:

    def __init__(self):

        self.certificado = None
        self.conectado = False

        # Configurações da SEFAZ
        self.uf = "35"              # São Paulo
        self.ambiente = "1"         # 1=Produção | 2=Homologação
        self.versao = "1.01"

        self.url = ""

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

    def conectar(self):

        print("Conectando à SEFAZ...")

        self.conectado = True

        return True

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