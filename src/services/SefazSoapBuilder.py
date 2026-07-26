class SefazSoapBuilder:

    def __init__(self):

        self.versao = "1.01"

    # -------------------------------------------------

    def montarConsultaNSU(self, cnpj, ultimoNSU):

        xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<distDFeInt xmlns="http://www.portalfiscal.inf.br/nfe" versao="{self.versao}">
    <tpAmb>1</tpAmb>
    <cUFAutor>35</cUFAutor>
    <CNPJ>{cnpj}</CNPJ>
    <distNSU>
        <ultNSU>{ultimoNSU}</ultNSU>
    </distNSU>
</distDFeInt>
"""

        return xml