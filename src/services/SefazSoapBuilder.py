class SefazSoapBuilder:

    def __init__(self):

        self.versao = "1.01"

    # -------------------------------------------------

    def montarConsultaNSU(self, cnpj, ultimoNSU):

        xml = f"""<distDFeInt xmlns="http://www.portalfiscal.inf.br/nfe" versao="{self.versao}">
    <tpAmb>1</tpAmb>
    <cUFAutor>35</cUFAutor>
    <CNPJ>{cnpj}</CNPJ>
    <distNSU>
        <ultNSU>{ultimoNSU}</ultNSU>
    </distNSU>
</distDFeInt>"""

        return xml

    # -------------------------------------------------

    def montarEnvelopeSOAP(self, xmlNFe):

        soap = f"""<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">

    <soap12:Header>

        <nfeCabecMsg xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeDistribuicaoDFe">

            <cUF>35</cUF>

            <versaoDados>{self.versao}</versaoDados>

        </nfeCabecMsg>

    </soap12:Header>

    <soap12:Body>

        <nfeDistDFeInteresse xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeDistribuicaoDFe">

            <nfeDadosMsg>

                {xmlNFe}

            </nfeDadosMsg>

        </nfeDistDFeInteresse>

    </soap12:Body>

</soap12:Envelope>
"""

        return soap