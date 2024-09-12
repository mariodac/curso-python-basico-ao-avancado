from pathlib import Path
from PySide6.QtWidgets import QMessageBox

INFORMATION = QMessageBox.Icon.Information
WARNING = QMessageBox.Icon.Warning
CRITICAL = QMessageBox.Icon.Critical

ROOT_DIR = Path(__file__).parent.parent
IMGS_DIR = ROOT_DIR / "images"
# Sizing
BIG_FONT_SIZE = 40
MEDIUM_FONT_SIZE = 24
SMALL_FONT_SIZE = 18
TEXT_MARGIN = 15
MINIMUM_WIDTH = 600

WINDOW_ICON_PATH = IMGS_DIR / "icon.png"

DARKER_PRIMARY_COLOR = "#16658a"
DARKEST_PRIMARY_COLOR = "#115270"
PRIMARY_COLOR = "#1e81b0"
