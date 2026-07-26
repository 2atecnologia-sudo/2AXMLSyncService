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
    QMessageBox
)

from src.config.ConfigManager import ConfigManager


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.config = ConfigManager()

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

        self.carregarConfiguracao()

        self.conectarEventos()

        self.statusBar().showMessage("Sistema iniciado")

    # =====================================================

    def criarCabecalho(self):

        titulo = QLabel("2A XML Downloader")

        fonte = QFont()
        fonte.setPointSize(18)
        fonte.setBold(True)

        titulo.setFont(fonte)
        titulo.setAlignment(Qt.AlignCenter)

        self.layoutPrincipal.addWidget(titulo)

    # =====================================================

    def criarConfiguracao(self):

        grupo = QGroupBox("Configuração")

        layout = QGridLayout()

        layout.addWidget(QLabel("Empresa"), 0, 0)

        self.edEmpresa = QLineEdit()

        layout.addWidget(self.edEmpresa, 0, 1)

        layout.addWidget(QLabel("CNPJ"), 1, 0)

        self.edCNPJ = QLineEdit()

        layout.addWidget(self.edCNPJ, 1, 1)

        layout.addWidget(QLabel("Certificado"), 2, 0)

        linha = QHBoxLayout()

        self.edCertificado = QLineEdit()

        self.btCertificado = QPushButton("...")

        linha.addWidget(self.edCertificado)

        linha.addWidget(self.btCertificado)

        layout.addLayout(linha, 2, 1)

        layout.addWidget(QLabel("Senha"), 3, 0)

        self.edSenha = QLineEdit()

        self.edSenha.setEchoMode(QLineEdit.Password)

        layout.addWidget(self.edSenha, 3, 1)

        layout.addWidget(QLabel("Pasta XML"), 4, 0)

        linha2 = QHBoxLayout()

        self.edPasta = QLineEdit()

        self.btPasta = QPushButton("...")

        linha2.addWidget(self.edPasta)

        linha2.addWidget(self.btPasta)

        layout.addLayout(linha2, 4, 1)

        layout.addWidget(QLabel("Intervalo (segundos)"), 5, 0)

        self.spIntervalo = QSpinBox()

        self.spIntervalo.setMinimum(10)
        self.spIntervalo.setMaximum(3600)

        layout.addWidget(self.spIntervalo, 5, 1)

        grupo.setLayout(layout)

        self.layoutPrincipal.addWidget(grupo)

            # =====================================================

    def criarBotoes(self):

        layout = QHBoxLayout()

        self.btSalvar = QPushButton("Salvar")

        self.btTestar = QPushButton("Testar Configuração")

        self.btIniciar = QPushButton("Iniciar Serviço")

        self.btParar = QPushButton("Parar Serviço")

        layout.addWidget(self.btSalvar)

        layout.addWidget(self.btTestar)

        layout.addStretch()

        layout.addWidget(self.btIniciar)

        layout.addWidget(self.btParar)

        self.layoutPrincipal.addLayout(layout)

    # =====================================================

    def criarStatus(self):

        grupo = QGroupBox("Status")

        layout = QGridLayout()

        layout.addWidget(QLabel("Licença:"), 0, 0)

        self.lbLicenca = QLabel("Não verificada")

        layout.addWidget(self.lbLicenca, 0, 1)

        layout.addWidget(QLabel("Certificado:"), 1, 0)

        self.lbCertificado = QLabel("Não testado")

        layout.addWidget(self.lbCertificado, 1, 1)

        layout.addWidget(QLabel("Serviço:"), 2, 0)

        self.lbServico = QLabel("Parado")

        layout.addWidget(self.lbServico, 2, 1)

        grupo.setLayout(layout)

        self.layoutPrincipal.addWidget(grupo)

    # =====================================================

    def criarLog(self):

        grupo = QGroupBox("Log")

        layout = QVBoxLayout()

        self.txtLog = QTextEdit()

        self.txtLog.setReadOnly(True)

        layout.addWidget(self.txtLog)

        grupo.setLayout(layout)

        self.layoutPrincipal.addWidget(grupo)

    # =====================================================

    def conectarEventos(self):

        self.btCertificado.clicked.connect(self.selecionarCertificado)

        self.btPasta.clicked.connect(self.selecionarPasta)

        self.btSalvar.clicked.connect(self.salvarConfiguracao)

        self.btTestar.clicked.connect(self.testarConfiguracao)

    # =====================================================

    def log(self, texto):

        self.txtLog.append(texto)

        self.statusBar().showMessage(texto)

            # =====================================================

    def selecionarCertificado(self):

        arquivo, _ = QFileDialog.getOpenFileName(
            self,
            "Selecionar Certificado",
            "",
            "Certificado (*.pfx)"
        )

        if arquivo:
            self.edCertificado.setText(arquivo)

    # =====================================================

    def selecionarPasta(self):

        pasta = QFileDialog.getExistingDirectory(
            self,
            "Selecionar Pasta XML"
        )

        if pasta:
            self.edPasta.setText(pasta)

    # =====================================================

    def salvarConfiguracao(self):

        self.config.set("GERAL", "empresa", self.edEmpresa.text())
        self.config.set("GERAL", "cnpj", self.edCNPJ.text())

        self.config.set("CERTIFICADO", "arquivo", self.edCertificado.text())
        self.config.set("CERTIFICADO", "senha", self.edSenha.text())

        self.config.set("XML", "pasta", self.edPasta.text())
        self.config.set("XML", "intervalo", self.spIntervalo.value())

        self.config.save()

        self.log("Configuração salva com sucesso.")

    # =====================================================

    def carregarConfiguracao(self):

        self.edEmpresa.setText(
            self.config.get("GERAL", "empresa")
        )

        self.edCNPJ.setText(
            self.config.get("GERAL", "cnpj")
        )

        self.edCertificado.setText(
            self.config.get("CERTIFICADO", "arquivo")
        )

        self.edSenha.setText(
            self.config.get("CERTIFICADO", "senha")
        )

        self.edPasta.setText(
            self.config.get("XML", "pasta")
        )

        intervalo = self.config.get(
            "XML",
            "intervalo",
            "60"
        )

        try:
            self.spIntervalo.setValue(int(intervalo))
        except:
            self.spIntervalo.setValue(60)

                # =====================================================

    def testarConfiguracao(self):

        erros = []

        if not self.edEmpresa.text().strip():
            erros.append("Empresa não informada.")

        if not self.edCNPJ.text().strip():
            erros.append("CNPJ não informado.")

        if not self.edCertificado.text().strip():
            erros.append("Certificado não informado.")

        if not self.edPasta.text().strip():
            erros.append("Pasta XML não informada.")

        if erros:

            QMessageBox.warning(
                self,
                "Configuração",
                "\n".join(erros)
            )

            self.log("Falha na validação da configuração.")

            return

        QMessageBox.information(
            self,
            "Configuração",
            "Configuração válida."
        )

        self.log("Configuração validada com sucesso.")

    # =====================================================

    def iniciarServico(self):

        self.lbServico.setText("Em desenvolvimento")

        self.log("Serviço ainda não implementado.")

    # =====================================================

    def pararServico(self):

        self.lbServico.setText("Parado")

        self.log("Serviço parado.")

    # =====================================================

    def closeEvent(self, event):

        self.log("Encerrando aplicação...")

        event.accept()