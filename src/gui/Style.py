"""
===========================================================
2A XML Sync Service

Arquivo.......: Style.py
Descrição.....: Tema visual da aplicação

===========================================================
"""


def load_style():

    return """

QMainWindow{

    background:#202124;

}

/*----------------------------------------------------*/

QWidget{

    background:#202124;

    color:white;

    font-family:Segoe UI;

    font-size:10pt;

}

/*----------------------------------------------------*/

QLabel{

    color:white;

    background:transparent;

}

/*----------------------------------------------------*/

QLineEdit{

    background:#2B2D31;

    border:1px solid #3D4045;

    border-radius:6px;

    padding:6px;

    color:white;

}

/*----------------------------------------------------*/

QComboBox{

    background:#2B2D31;

    border:1px solid #3D4045;

    border-radius:6px;

    padding:6px;

    color:white;

}

/*----------------------------------------------------*/

QSpinBox{

    background:#2B2D31;

    border:1px solid #3D4045;

    border-radius:6px;

    padding:6px;

    color:white;

}

/*----------------------------------------------------*/

QPushButton{

    background:#0078D7;

    color:white;

    border:none;

    border-radius:6px;

    padding:8px;

    font-weight:bold;

}

QPushButton:hover{

    background:#1890ff;

}

QPushButton:pressed{

    background:#005A9E;

}

/*----------------------------------------------------*/

QGroupBox{

    border:1px solid #404040;

    border-radius:8px;

    margin-top:12px;

    font-weight:bold;

}

QGroupBox::title{

    subcontrol-origin:margin;

    left:12px;

    padding:0 4px;

}

/*----------------------------------------------------*/

QStatusBar{

    background:#181818;

    color:white;

}

"""