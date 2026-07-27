"""
===========================================================
WindowsCertificateStore.py

Leitura dos certificados instalados no Windows
utilizando .NET (pythonnet)

Compatível com:

- Certificado A1
- Certificado A3 (SafeNet)
- ICP-Brasil
===========================================================
"""

import clr

clr.AddReference("System")

from System.Security.Cryptography.X509Certificates import (
    X509Store,
    StoreName,
    StoreLocation,
    OpenFlags
    )


class WindowsCertificateStore:

    def __init__(self):
        pass

    # ----------------------------------------------------------

    def listarCertificados(self):

        certificados = []

        store = X509Store(
            StoreName.My,
            StoreLocation.CurrentUser
        )

        store.Open(OpenFlags.ReadOnly)

        try:

            for cert in store.Certificates:

                assunto = cert.Subject

                # Ignora certificados internos do Windows
                if "ICP-Brasil" not in assunto:
                    continue

                nome = ""
                cnpj = ""

                try:

                    partes = assunto.split(",")

                    primeira = partes[0]

                    if ":" in primeira:

                        nome, cnpj = primeira.replace("CN=", "").split(":", 1)

                    else:

                        nome = primeira.replace("CN=", "")

                except Exception:

                    nome = assunto

                certificados.append({

                    "nome": nome.strip(),

                    "cnpj": cnpj.strip(),

                    "assunto": assunto,

                    "emissor": cert.Issuer,

                    "validade": str(cert.NotAfter),

                    "thumbprint": cert.Thumbprint,

                    "certificado": cert

                })

        finally:

            store.Close()

        return certificados