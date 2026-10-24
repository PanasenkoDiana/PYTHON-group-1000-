from PyQt6.QtWidgets import (
    QMainWindow, QFrame, QHBoxLayout,
    QVBoxLayout, QGridLayout, QScrollArea,
    QLabel, QPushButton, QLineEdit, QTextEdit, QComboBox
)
from modules.app import app
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

MAIN_WINDOW_WIDTH = 1024
MAIN_WINDOW_HEIGHT = 800

main_window = QMainWindow()
primary_screen = app.primaryScreen()
primary_screen_size = primary_screen.size()

main_window.setGeometry(
    (primary_screen_size.width() // 2) - (MAIN_WINDOW_WIDTH // 2),
    (primary_screen_size.height() // 2) - (MAIN_WINDOW_HEIGHT // 2),
    MAIN_WINDOW_WIDTH,
    MAIN_WINDOW_HEIGHT
)
main_window.setWindowTitle('Practice')

main_frame = QFrame(parent=main_window)
main_frame.setFixedSize(MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT)
main_frame.setStyleSheet('background-color: #1e1e1e')

main_layout = QVBoxLayout()
main_layout.setSpacing(15)
main_layout.setContentsMargins(20, 20, 20, 20)
main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
main_frame.setLayout(main_layout)

top_line_edit = QLineEdit(parent=main_frame)
top_line_edit.setStyleSheet("""
    border: 2px solid #555555;
    border-radius: 6px;
    color: white; 
    background-color: #2d2d2d;
    font-size: 16px;
    padding: 5px;
""")
top_line_edit.setFixedSize(400, 40)
top_line_edit.setPlaceholderText("enter text 1")
main_layout.addWidget(top_line_edit)

combo_box = QComboBox(parent= main_frame)

combo_box.addItems(["option 1", "option 2", "option 3"])
combo_box.addItem("option 4")
combo_box.addItem("option 5")
combo_box.addItem("option 6")
combo_box.addItem("option 7")

combo_box.setStyleSheet("""
    QComboBox {
        background-color: #2d2d2d;
        color: white;
        border: 2px solid #555555;
        border-radius: 6px;
        padding: 5px;
        font-size: 16px;
    }
    QComboBox QAbstractItemView {
        background-color: #2d2d2d;
        color: white;
        selection-background-color: #007acc;
        border: 2px solid #555555;
    }
""")
combo_box.setFixedSize(400, 40)


text_edit = QTextEdit(parent= main_frame)
text_edit.setStyleSheet("""
    border: 2px solid #555555;
    border-radius: 6px;
    color: white; 
    background-color: #2d2d2d;
    font-size: 16px;
""")
text_edit.setFixedSize(400, 200)
text_edit.setPlaceholderText("enter text")


button = QPushButton(
    parent=main_frame,
    text="Click"
)

button.setStyleSheet("""
    border: 2px solid #555555;
    border-radius: 6px;
    color: white;
    background-color: #db4540;
    font-size: 16px;
""")
button.setFixedSize(150, 40)

main_layout.addWidget(top_line_edit, alignment=Qt.AlignmentFlag.AlignCenter)
main_layout.addWidget(combo_box, alignment=Qt.AlignmentFlag.AlignCenter)
main_layout.addWidget(text_edit, alignment=Qt.AlignmentFlag.AlignCenter)
main_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

def clear_fields():
    top_line_edit.clear()
    text_edit.clear()       
    combo_box.setCurrentIndex(0)

button.clicked.connect(clear_fields)