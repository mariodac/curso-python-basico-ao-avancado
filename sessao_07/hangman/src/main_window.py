import sys
import random
from PySide6.QtCore import Qt, Slot
from window import Ui_MainWindow
from PySide6.QtGui import QIcon, QKeyEvent
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QApplication,
    QMessageBox,
    QSpacerItem,
    QSizePolicy,
    QLineEdit,
    QLabel,
)
from PySide6.QtGui import QPixmap
from constants import (
    IMGS_DIR,
    WINDOW_ICON_PATH,
    INFORMATION,
    WARNING,
    CRITICAL,
    BIG_FONT_SIZE,
)


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, dic_words: dict, parent: QWidget | None = None) -> None:

        super().__init__(parent)
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.setupUi(self)
        self._word_list = dic_words
        self._word, self._category = self._choice_word(dic_words)
        self.label_category = QLabel(self)
        self.gridLayout.addWidget(self.label_category, 1, 0)
        self._setup_word()
        self.pushButton.clicked.connect(self._do_a_try)
        self.attempts = []
        self.error_count = 0
        self.hangman_parts = [
            "head",
            "body",
            "left_arm",
            "right_arm",
            "left_leg",
            "right_leg",
        ]
        # Criar e configurar o QLabel para a imagem da forca
        self.hangman_label = QLabel(self)
        self.hangman_label.setGeometry(50, 50, 200, 300)  # Ajuste conforme necessário
        self.centralwidget.layout().addWidget(self.hangman_label)
        self._update_hangman_display()
        self.letter_try.setFocus()

    def _choice_word(self, dic_words):
        keys = list(dic_words.keys())
        choiced_key = random.choice(keys)
        choiced_word = random.choice(dic_words[choiced_key])
        self._guessed_word = ["*" if x != " " else " " for x in choiced_word]
        # print(f"Categoria: {choiced_key} | Palavra: {choiced_word}")
        return choiced_word, choiced_key

    def _setup_word(self):
        self.statusbar.showMessage("Nenhuma tentativa")
        for index in range(len(self._word)):
            button = Field(self._word[index].upper())
            if self._word[index] == " ":
                horizontalSpacer = QSpacerItem(
                    30, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum
                )
                self.gridLayout.addItem(horizontalSpacer, 0, index)
                continue
            else:
                self.gridLayout.addWidget(button, 0, index)
        self.label_category.setText(f"Categoria: {self._category}")
        self.label_category.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.label_category.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_category.setGeometry(500, 100, 200, 50)

    @Slot()
    def _do_a_try(self):
        letters = self.letter_try.text().lower()
        for letter in letters:
            if letter in self.attempts:
                self._showInfo(f"Letra '{letter.upper()}' já tentada", WARNING, False)
                continue
            self.attempts.append(letter)
            letter_found = False
            for row in range(self.gridLayout.rowCount()):
                for col in range(self.gridLayout.columnCount()):
                    item = self.gridLayout.itemAtPosition(row, col)
                    if item and isinstance(item.widget(), Field):
                        field = item.widget()
                        if isinstance(field, Field) and field.text().lower() == letter:
                            for i in range(len(self._word)):
                                if self._word[i] == letter:
                                    self._guessed_word[i] = letter
                            field.setProperty("cssClass", "visible")
                            field.style().unpolish(field)
                            field.style().polish(field)
                            letter_found = True
            if not letter_found:
                self._add_hangman_part()

        self.statusbar.showMessage(f"Tentativas: {' '.join(self.attempts)}")
        self.letter_try.clear()
        self.letter_try.setFocus()

        if "*" not in self._guessed_word:
            self._showInfo("Parabéns! Você venceu.", INFORMATION, True)
        elif self.error_count >= len(self.hangman_parts):
            self._showInfo(f"Você perdeu! A palavra era: {self._word}", CRITICAL, True)

    def _add_hangman_part(self):
        if self.error_count < len(self.hangman_parts):
            self.error_count += 1
            self._update_hangman_display()
            if self.error_count >= len(self.hangman_parts):
                self._showInfo(
                    f"Você perdeu! A palavra era: {self._word}", CRITICAL, True
                )

    def _update_hangman_display(self):
        image_path = IMGS_DIR / f"hangman_{self.error_count}.png"
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print(f"Erro ao carregar a imagem: {image_path}")
        else:
            self.hangman_label.setPixmap(pixmap)
            self.hangman_label.setScaledContents(True)

    def makeMsgBox(self):
        return QMessageBox(self)

    def _makeDialog(self, text: str, icon: QMessageBox.Icon):
        msgBox = self.makeMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(icon)
        return msgBox

    def _showInfo(self, text: str, level: QMessageBox.Icon, restart_game: bool):
        msgBox = self._makeDialog(text, level)
        result = msgBox.exec()
        if result == QMessageBox.StandardButton.Ok and restart_game:
            self._restart_game()

    def _restart_game(self):
        for row in range(self.gridLayout.rowCount()):
            for col in range(self.gridLayout.columnCount()):
                item = self.gridLayout.itemAtPosition(row, col)
                if item and isinstance(item.widget(), Field):
                    field = item.widget()
                    if field:
                        self.gridLayout.removeWidget(field)
                        field.deleteLater()
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self._word, self._category = self._choice_word(self._word_list)
        self._setup_word()
        self.attempts = []
        self.error_count = 0
        self._update_hangman_display()
        self.statusbar.showMessage("Nenhuma tentativa")
        self.letter_try.clear()
        self.letter_try.setFocus()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        key = event.key()
        KEYS = Qt.Key
        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]
        if isEnter:
            self._do_a_try()
        elif isEsc:
            self._restart_game()


class Field(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setDisabled(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._config_style()
        self.setProperty("cssClass", "hidden")

    def _config_style(self):
        font = self.font()
        font.setPixelSize(BIG_FONT_SIZE)
        font.setBold(True)
        self.setFont(font)


if __name__ == "__main__":

    dic_words = {
        "Tecnologia": [
            "python",
            "programacao",
            "desenvolvimento",
            "computador",
            "ciencia de dados",
            "inteligencia artificial",
            "algoritmo",
            "estrutura de dados",
            "logica de programacao",
            "programacao orientada a objetos",
            "software livre",
        ],
        "Esportes": [
            "futebol",
            "basquete",
            "tenis",
            "futebol americano",
            "volei",
            "natacao",
            "parapente",
            "rafting",
            "kitesurf",
            "escalada",
            "mountain bike",
            "rapel",
            "bungee jumping",
            "sandboard",
            "canoagem",
            "asa delta",
        ],
        "Animais": [
            "cachorro",
            "gato",
            "elefante",
            "tigre",
            "leao",
            "macaco",
            "girafa",
            "pinguim",
            "cavalo",
            "cobra",
            "tartaruga",
            "macaco",
            "elefante",
            "tigre",
            "leao",
        ],
        "Profissões": [
            "medico",
            "professor",
            "engenheiro",
            "advogado",
            "chef",
            "jornalista",
            "arquiteto",
            "bombeiro",
            "policial",
            "dentista",
        ],
        "Comidas": [
            "pizza",
            "hamburguer",
            "macarrao",
            "lasanha",
            "feijoada",
            "churrasco",
            "tapioca",
            "pudim",
            "brigadeiro",
            "beijinho",
        ],
        "Cidades": [
            "sao paulo",
            "rio de janeiro",
            "belo horizonte",
            "salvador",
            "fortaleza",
            "recife",
            "teresina",
            "sao luis",
            "sao jose dos campos",
            "sao carlos",
            "sao jose",
            "sao paulo",
        ],
        "Animes": [
            "naruto",
            "bleach",
            "one piece",
            "dragon ball",
            "fairy tail",
            "attack on titan",
            "death note",
            "fullmetal alchemist",
            "hunter x hunter",
            "one punch man",
            "tokyo ghoul",
            "demon slayer",
            "jujutsu kaisen",
            "my hero academia",
            "naruto shippuden",
        ],
        "Filmes": [
            "vingadores",
            "batman",
            "superman",
            "homem de ferro",
            "thor",
            "hulk",
            "capitao america",
            "mulher maravilha",
            "joker",
            "matrix",
            "star wars",
            "harry potter",
            "senhor dos aneis",
            "cronicas de narnia",
            "percy jackson",
            "diario de um banana",
        ],
        "Series": [
            "the office",
            "friends",
            "the big bang theory",
            "the simpsons",
            "the walking dead",
            "the 100",
            "the vampire diaries",
            "the witcher",
            "the boys",
            "the office",
            "evil",
        ],
        "Música": [
            "the beatles",
            "queen",
            "michael jackson",
            "elvis presley",
            "prince",
            "madonna",
            "samba",
            "bossa nova",
            "rock",
            "mpb",
            "funk",
            "forro",
            "axe",
            "sertanejo",
            "pagode",
            "frevo",
        ],
        "Livros": [
            "harry potter",
            "senhor dos aneis",
            "cronicas de narnia",
            "percy jackson",
            "diario de um banana",
            "jogos vorazes",
            "corte de espinhos e rosas",
            "a culpa e das estrelas",
            "percy jackson e o ladrao de raios",
            "percy jackson e a cidade dos aneis",
            "percy jackson e o ladrao de raios",
            "percy jackson e a cidade dos aneis",
            "percy jackson e o ladrao de raios",
            "percy jackson e a cidade dos aneis",
        ],
        "Jogos": [
            "league of legends",
            "valorant",
            "minecraft",
            "fortnite",
            "call of duty",
            "grand theft auto",
            "the witcher",
        ],
        "Paises": [
            "brasil",
            "argentina",
            "chile",
            "uruguai",
            "paraguai",
            "peru",
            "bolivia",
            "colombia",
            "venezuela",
            "chile",
            "uruguai",
            "paraguai",
            "peru",
            "bolivia",
        ],
        "Cores": [
            "azul",
            "vermelho",
            "verde",
            "amarelo",
            "roxo",
            "laranja",
            "rosa",
            "preto",
            "branco",
            "cinza",
            "marrom",
        ],
        "Frutas": [
            "banana",
            "maca",
            "pera",
            "uva",
            "laranja",
            "limao",
            "melao",
            "abacate",
            "amora",
            "banana",
            "mamao",
            "abacaxi",
            "caju",
            "coco",
            "caju",
        ],
        "Instrumentos": [
            "guitarra",
            "piano",
            "violino",
            "flauta",
            "bateria",
            "saxofone",
            "clarinete",
            "trompete",
            "trombone",
            "trompa",
            "violoncelo",
        ],
    }
    app = QApplication(sys.argv)
    mainWindow = MainWindow(dic_words)
    qss = """QLineEdit[cssClass="hidden"] {
        background: transparent;
        color: transparent;
    }
    QLineEdit[cssClass="visible"] {
        color: black;
    }"""
    icon = QIcon(str(WINDOW_ICON_PATH))
    mainWindow.setWindowIcon(icon)
    # app.setWindowIcon(icon)
    if sys.platform.startswith("win"):
        import ctypes

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            "CompanyName.ProductName.SubProduct.VersionInformation"
        )
    app.setStyleSheet(app.styleSheet() + qss)
    mainWindow.show()
    app.exec()
