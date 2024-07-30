# SOLUÇÃO PRÓXIMA AULA: qdarktheme deixou de funcionar (use qdarkstyle)

Na próxima aula, vou falar sobre a instalação de temas no PySide6. No entanto, o tema que escolhi não funciona nas versões atuais do Python. Estou escrevendo isso antes da aula para que você não perca tempo pesquisando ou tentando resolver um problema da própria biblioteca usada (qdarktheme).

Como o aluno [Mauricio Ittner mencionou nas perguntas e respostas da aula](https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/36631958#questions/21644092), uma alternativa que funciona bem é a biblioteca "[qdarkstyle](https://pypi.org/project/QDarkStyle/)".

Seguem as instruções:

Instalação do **qdarkstyle**:

```python
pip install qdarkstyle
```

No arquivo "`styles.py`":

```python
    import qdarkstyle
    from variables import (DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR,
                           PRIMARY_COLOR)
     
    qss = f"""
        PushButton[cssClass="specialButton"] {{
            color: #fff;
            background: {PRIMARY_COLOR};
            border-radius: 5px;
        }}
        PushButton[cssClass="specialButton"]:hover {{
            color: #fff;
            background: {DARKER_PRIMARY_COLOR};
        }}
        PushButton[cssClass="specialButton"]:pressed {{
            color: #fff;
            background: {DARKEST_PRIMARY_COLOR};
        }}
    """
     
     
    def setupTheme(app):
        # Aplicar o estilo escuro do qdarkstyle
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
     
        # Sobrepor com o QSS personalizado para estilização adicional
        app.setStyleSheet(app.styleSheet() + qss)

```

No arquivo "`main.py`": 

```python
    import sys
     
    from buttons import ButtonsGrid
    from display import Display
    from info import Info
    from main_window import MainWindow
    from PySide6.QtGui import QIcon
    from PySide6.QtWidgets import QApplication
    from styles import setupTheme
    from variables import WINDOW_ICON_PATH
     
    if __name__ == '__main__':
        # Cria a aplicação
        app = QApplication(sys.argv)
        setupTheme(app)
        window = MainWindow()
     
        # Define o ícone
        icon = QIcon(str(WINDOW_ICON_PATH))
        window.setWindowIcon(icon)
        app.setWindowIcon(icon)
     
        # Info
        info = Info('Sua conta')
        window.addWidgetToVLayout(info)
     
        # Display
        display = Display()
        window.addWidgetToVLayout(display)
     
        # Grid
        buttonsGrid = ButtonsGrid(display, info, window)
        window.vLayout.addLayout(buttonsGrid)
     
        # Executa tudo
        window.adjustFixedSize()
        window.show()
        app.exec()
```

Espero que ajude. Agora você pode seguir para a próxima aula, pois, a única mudança é a biblioteca usada, o propósito continua o mesmo.