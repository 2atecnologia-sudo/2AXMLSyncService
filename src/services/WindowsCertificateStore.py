"""
===========================================================
WindowsCertificateStore.py

Responsável por acessar os certificados instalados
no Windows (A1 e A3).
===========================================================
"""
from py_cert_store import find_windows_cert_all

class WindowsCertificateStore:

    def __init__(self):
        pass

    # --------------------------------------------------

    def listarCertificados(self):
        """
        Retorna todos os certificados encontrados no Windows.
        """
        try:

            certificados = find_windows_cert_all()

            return certificados

        except Exception as erro:

            print(f"Erro ao listar certificados: {erro}")

        return []
        


    