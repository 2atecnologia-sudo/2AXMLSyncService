"""
===========================================================
2A XML Downloader

Arquivo: MainWindow.py
===========================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QGroupBox,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QFileDialog,
    QSpinBox,
    QStatusBar
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("2A XML Downloader")
        self.resize(1100, 700)

        self.central = QWidget()
        self.setCentralWidget(self.central)

        self.layoutPrincipal = QVBoxLayout(self.central)

        self.criarCabecalho()
        self.criarConfiguracao()
        self.criarBotoes()
        self.criarStatus()
        self.criarLog()
        self.conectarEventos()
        self.statusBar().showMessage("Sistema iniciado")

    # -----------------------------------------------------

    def criarCabecalho(self):

        titulo = QLabel("2A XML Downloader")

        fonte = QFont()
        fonte.setPointSize(18)
        fonte.setBold(True)

        titulo.setFont(fonte)
        titulo.setAlignment(Qt.AlignCenter)

        self.layoutPrincipal.addWidget(titulo)

    # -----------------------------------------------------

    def criarConfiguracao(self):

        grupo = QGroupBox("Configuração")

        layout = QGridLayout()

        layout.addWidget(QLabel("Empresa"),0,0)
        self.edEmpresa = QLineEdit()
        layout.addWidget(self.edEmpresa,0,1)

        layout.addWidget(QLabel("CNPJ"),1,0)
        self.edCNPJ = QLineEdit()
        layout.addWidget(self.edCNPJ,1,1)

        layout.addWidget(QLabel("Certificado"),2,0)

        linha = QHBoxLayout()

        self.edCertificado = QLineEdit()

        self.btCertificado = QPushButton("...")

        self.btCertificado.clicked.connect(self.selecionarCertificado)

        linha.addWidget(self.edCertificado)
        linha.addWidget(self.btCertificado)

        layout.addLayout(linha,2,1)

        layout.addWidget(QLabel("Senha"),3,0)

        self.edSenha = QLineEdit()

        self.edSenha.setEchoMode(QLineEdit.Password)

        layout.addWidget(self.edSenha,3,1)

        layout.addWidget(QLabel("Pasta XML"),4,0)

        linha2 = QHBoxLayout()

        self.edPasta = QLineEdit()

        self.btPasta = QPushButton("...")

        self.btPasta.clicked.connect(self.selecionarPasta)

        linha2.addWidget(self.edPasta)
        linha2.addWidget(self.btPasta)

        layout.addLayout(linha2,4,1)

        layout.addWidget(QLabel("Intervalo (segundos)"),5,0)

        self.spIntervalo = QSpinBox()

        self.spIntervalo.setMinimum(10)
        self.spIntervalo.setMaximum(3600)
        self.spIntervalo.setValue(60)

        layout.addWidget(self.spIntervalo,5,1)

        grupo.setLayout(layout)

        self.layoutPrincipal.addWidget(grupo)

    # -----------------------------------------------------

    def criarBotoes(self):

        linha = QHBoxLayout()

        self.btSalvar = QPushButton("Salvar")

        self.btTestar = QPushButton("Testar")

        self.btBaixar = QPushButton("Baixar Agora")

        self.btIniciar = QPushButton("Iniciar")

        self.btParar = QPushButton("Parar")

        linha.addWidget(self.btSalvar)
        linha.addWidget(self.btTestar)
        linha.addWidget(self.btBaixar)
        linha.addWidget(self.btIniciar)
        linha.addWidget(self.btParar)

        self.layoutPrincipal.addLayout(linha)

    # -----------------------------------------------------

    def criarStatus(self):

        grupo = QGroupBox("Status")

        layout = QGridLayout()

        self.lbLicenca = QLabel("Licença: aguardando")
        self.lbCertificado = QLabel("Certificado: aguardando")
        self.lbInternet = QLabel("Internet: aguardando")
        self.lbSefaz = QLabel("SEFAZ: aguardando")

        layout.addWidget(self.lbLicenca,0,0)
        layout.addWidget(self.lbCertificado,1,0)
        layout.addWidget(self.lbInternet,2,0)
        layout.addWidget(self.lbSefaz,3,0)

        grupo.setLayout(layout)

        self.layoutPrincipal.addWidget(grupo)

            # -----------------------------------------------------

    def criarLog(self):

        grupo = QGroupBox("Log")

        layout = QVBoxLayout()

        self.txtLog = QTextEdit()

        self.txtLog.setReadOnly(True)

        layout.addWidget(self.txtLog)

        grupo.setLayout(layout)

        self.layoutPrincipal.addWidget(grupo)

        self.log("Sistema iniciado.")

    # -----------------------------------------------------

    def selecionarCertificado(self):

        arquivo, _ = QFileDialog.getOpenFileName(
            self,
            "Selecionar Certificado",
            "",
            "Certificados (*.pfx *.p12);;Todos (*.*)"
        )

        if arquivo:

            self.edCertificado.setText(arquivo)

            self.log("Certificado selecionado.")

    # -----------------------------------------------------

    def selecionarPasta(self):

        pasta = QFileDialog.getExistingDirectory(
            self,
            "Selecionar Pasta dos XML"
        )

        if pasta:

            self.edPasta.setText(pasta)

            self.log("Pasta selecionada.")

    # -----------------------------------------------------

    def log(self, texto):

        self.txtLog.append(texto)

        self.statusBar().showMessage(texto)

    # -----------------------------------------------------

    def salvarConfiguracao(self):

        self.log("Salvar configuração - ainda não implementado.")

    # -----------------------------------------------------

    def testarConfiguracao(self):

        self.log("Teste de configuração - ainda não implementado.")

    # -----------------------------------------------------

    def baixarAgora(self):

        self.log("Download manual - ainda não implementado.")

    # -----------------------------------------------------

    def iniciarMonitoramento(self):

        self.log("Monitoramento iniciado.")

        self.lbLicenca.setText("Licença: OK")
        self.lbInternet.setText("Internet: OK")

    # -----------------------------------------------------

    def pararMonitoramento(self):

        self.log("Monitoramento parado.")

    # -----------------------------------------------------

    def conectarEventos(self):

        self.btSalvar.clicked.connect(self.salvarConfiguracao)

        self.btTestar.clicked.connect(self.testarConfiguracao)

        self.btBaixar.clicked.connect(self.baixarAgora)

        self.btIniciar.clicked.connect(self.iniciarMonitoramento)

        self.btParar.clicked.connect(self.pararMonitoramento)