from src.services.CertificateManager import CertificateManager
from src.services.WindowsCertificateStore import WindowsCertificateStore
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QComboBox,
    QRadioButton,
    QButtonGroup,
    QGroupBox,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QFileDialog,
    QSpinBox,
    QRadioButton,
    QButtonGroup,
    QMessageBox
)


from src.config.ConfigManager import ConfigManager
from src.services.WindowsCertificateStore import WindowsCertificateStore

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.config = ConfigManager()
        self.setWindowTitle("2A XML Downloader")
        self.showMaximized()

        self.central = QWidget()
        self.setCentralWidget(self.central)

        self.layoutPrincipal = QVBoxLayout(self.central)

        self.criarCabecalho()
        self.criarConfiguracao()
        self.criarBotoes()
        self.criarStatus()
        self.criarLog()

        print(type(self))
        print(hasattr(self, "carregarConfiguracao"))
        print([m for m in dir(self) if "Configuracao" in m])

        self.atualizarTipoCertificado()
        self.carregarConfiguracao()

        self.conectarEventos()
        
        self.statusBar().showMessage("Sistema iniciado")

    # =====================================================

    def criarCabecalho(self):

        titulo = QLabel("2A XML Downloader")

        fonte = QFont()

        fonte.setPointSize(22)

        fonte.setBold(True)

        titulo.setFont(fonte)

        titulo.setAlignment(Qt.AlignCenter)

        self.layoutPrincipal.addWidget(titulo)

        subtitulo = QLabel("Download Automático de XML da NF-e")

        fonte2 = QFont()

        fonte2.setPointSize(11)

        subtitulo.setFont(fonte2)

        subtitulo.setAlignment(Qt.AlignCenter)

        self.layoutPrincipal.addWidget(subtitulo)

    # =====================================================

    def criarConfiguracao(self):

        grupo = QGroupBox("Configuração")

        layout = QGridLayout()

        layout.addWidget(QLabel("Tipo do Certificado"), 0, 0)

        self.rbA1 = QRadioButton("A1 (.PFX)")
        self.rbA3 = QRadioButton("A3 (Token)")
        self.rbCloud = QRadioButton("Nuvem")

        self.rbA1.setChecked(True)

        linhaTipo = QHBoxLayout()
        linhaTipo.addWidget(self.rbA1)
        linhaTipo.addWidget(self.rbA3)
        linhaTipo.addWidget(self.rbCloud)

        layout.addLayout(linhaTipo, 0, 1)

        layout.addWidget(QLabel("Empresa"), 1, 0)

        self.edEmpresa = QLineEdit()

        layout.addWidget(self.edEmpresa, 1, 1)

        layout.addWidget(QLabel("CNPJ"), 2, 0)

        self.edCNPJ = QLineEdit()

        layout.addWidget(self.edCNPJ, 2, 1)

        layout.addWidget(QLabel("Certificado"), 3, 0)

        linha = QHBoxLayout()

        self.edCertificado = QLineEdit()

        self.btCertificado = QPushButton("...")

        linha.addWidget(self.edCertificado)

        linha.addWidget(self.btCertificado)

        layout.addLayout(linha, 3, 1)

        layout.addWidget(QLabel("Senha"), 4, 0)

        self.edSenha = QLineEdit()

        self.edSenha.setEchoMode(QLineEdit.Password)

        layout.addWidget(self.edSenha, 4, 1)

        layout.addWidget(QLabel("Pasta XML"), 5, 0)

        linha2 = QHBoxLayout()

        self.edPasta = QLineEdit()

        self.btPasta = QPushButton("...")

        linha2.addWidget(self.edPasta)

        linha2.addWidget(self.btPasta)

        layout.addLayout(linha2, 5, 1)

        layout.addWidget(QLabel("Intervalo (segundos)"), 6, 0)

        self.spIntervalo = QSpinBox()

        self.spIntervalo.setMinimum(10)
        self.spIntervalo.setMaximum(3600)

        layout.addWidget(self.spIntervalo, 6, 1)

        # =====================================================
        # Controles do Certificado A3
        # =====================================================

        self.lbToken = QLabel("Certificado A3")

        self.cmbToken = QComboBox()
        self.lbStatusCertificado = QLabel("")
        layout.addWidget(self.lbToken, 7, 0)
        layout.addWidget(self.cmbToken, 7, 1)
        layout.addWidget(
        self.lbStatusCertificado,
        8,
        1
     )
        self.lbPin = QLabel("PIN do Token")

        self.edPin = QLineEdit()
        self.edPin.setEchoMode(QLineEdit.Password)

        layout.addWidget(self.lbPin, 8, 0)
        layout.addWidget(self.edPin, 8, 1)

        self.btAtualizarToken = QPushButton("Buscar Certificados")
        self.btAtualizarToken.hide()


        layout.addWidget(self.btAtualizarToken, 9, 1)

# Inicialmente ocultos

        self.lbToken.hide()
        self.cmbToken.hide()

        self.lbPin.hide()
        self.edPin.hide()

        self.btAtualizarToken.hide()

        grupo.setLayout(layout)

        self.layoutPrincipal.addWidget(grupo)

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

    def atualizarTipoCertificado(self):

        a1 = self.rbA1.isChecked()
        a3 = self.rbA3.isChecked()

        # ---------- Controles A1 ----------
        self.edCertificado.setVisible(a1)
        self.btCertificado.setVisible(a1)
        self.edSenha.setVisible(a1)

        # ---------- Controles A3 ----------
        self.lbToken.setVisible(a3)
        self.cmbToken.setVisible(a3)

        self.lbPin.setVisible(a3)
        self.edPin.setVisible(a3)

        self.btAtualizarToken.setVisible(a3)

    # =====================================================

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

        self.btAtualizarToken.clicked.connect(self.atualizarListaCertificados)

        self.rbA1.toggled.connect(self.atualizarTipoCertificado)
        self.rbA3.toggled.connect(self.atualizarTipoCertificado)
        self.rbCloud.toggled.connect(self.atualizarTipoCertificado)
        self.cmbToken.currentIndexChanged.connect(self.certificadoSelecionado)
                                                 
        
        
        # =====================================================

    # =====================================================

    def log(self, texto):

         self.txtLog.append(texto)

         self.statusBar().showMessage(texto)

            # =====================================================
    def atualizarListaCertificados(self):
         # Volta para modo edição
         self.cmbToken.show()
         self.cmbToken.setEnabled(True)

         self.lbPin.show()
         self.edPin.show()

         self.btAtualizarToken.setText(
             "Buscar Certificados"
         )
         print("=== Atualizando certificados ===")

         manager = CertificateManager()

         certificados = manager.listarCertificadosWindows()

         print("Certificados encontrados:", len(certificados))

         self.cmbToken.clear()

         if len(certificados) == 0:

          QMessageBox.information(
            self,
            "Certificados",
            "Nenhum certificado encontrado."
          )

          return

         self.certificados = certificados
         for cert in certificados:

            print("CERTIFICADO:", cert)

            texto = (
            f"{cert['nome']} | "
            f"CNPJ: {cert['cnpj']} | "
            f"Validade: {cert['validade']}"
            )

            print("Texto:", texto)

            self.cmbToken.addItem(texto)


                    # Seleciona certificado salvo

            thumbprint_salvo = self.config.get(
            "CERTIFICADO",
            "thumbprint"
        )

         if thumbprint_salvo:

            for indice, cert in enumerate(certificados):

                if cert["thumbprint"] == thumbprint_salvo:

                    self.cmbToken.setCurrentIndex(indice)

                    print(
                        "Certificado salvo localizado:",
                        cert["nome"]
                    )

                    self.btAtualizarToken.setText(
                        "Editar Certificado"
                    )

                    print("Certificado salvo localizado - aguardando PIN")
                    break                                  
        # Cursor vai para o PIN
         self.edPin.setFocus()
         self.edPin.selectAll()
    
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

    # ---------------- Tipo do certificado ----------------

        if self.rbA1.isChecked():

            self.config.set("CERTIFICADO", "tipo", "A1")
            self.config.set("CERTIFICADO", "arquivo", self.edCertificado.text())
            self.config.set("CERTIFICADO", "senha", self.edSenha.text())
            self.config.set("CERTIFICADO", "thumbprint", "")
            self.config.set("CERTIFICADO", "nome", "")

        elif self.rbA3.isChecked():

            self.config.set("CERTIFICADO", "tipo", "A3")

            indice = self.cmbToken.currentIndex()

            if indice >= 0 and hasattr(self, "certificados"):

                cert = self.certificados[indice]

                self.config.set(
                "CERTIFICADO",
                "thumbprint",
                cert["thumbprint"]
               )

            self.config.set(
                "CERTIFICADO",
                "nome",
                cert["nome"]
            )

            self.config.set("CERTIFICADO", "arquivo", "")
            self.config.set("CERTIFICADO", "senha", "")

        else:

             self.config.set("CERTIFICADO", "tipo", "CLOUD")

    # ---------------- XML ----------------

        self.config.set("XML", "pasta", self.edPasta.text())
        self.config.set("XML", "intervalo", self.spIntervalo.value())
        if self.rbA3.isChecked():

            self.config.set(
               "CERTIFICADO",
               "tipo",
               "A3"
        )

            self.config.set(
               "CERTIFICADO",
               "configurado",
               "sim"
        )

        self.config.save()

        self.log("Configuração salva com sucesso.")

        if self.rbA3.isChecked():

           if self.edPin.text().strip():

                self.lbPin.hide()
                self.edPin.hide()

                print("✓ Certificado A3 conectado")
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

            # Carrega tipo de certificado salvo

        tipo = self.config.get(
            "CERTIFICADO",
            "tipo",
            "A1"
        )
        thumbprint = self.config.get(
            "CERTIFICADO",
            "thumbprint",
           ""
       )

        print("Thumbprint salvo:", thumbprint)
        print("Tipo certificado salvo:", tipo)
        if tipo == "A3":

            self.rbA3.setChecked(True)

            self.atualizarTipoCertificado()

            self.atualizarListaCertificados()

            if thumbprint:

              # Mantém o certificado visível no combo
               self.cmbToken.show()
              # certificado já conectado, não pedir PIN novamente
               self.lbPin.hide()
               self.edPin.hide()

               # Altera o botão
               self.btAtualizarToken.setText("Editar Certificado")

               print("Modo conectado: certificado carregado")

    def certificadoSelecionado(self):

         # Quando escolher um certificado no combo,
         # libera o campo PIN

               self.lbPin.show()
               self.edPin.show()


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