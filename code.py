from PyQt6.QtWidgets import (
    QMainWindow, QFrame, QHBoxLayout,
    QVBoxLayout, QGridLayout, QScrollArea,
    QLabel, QPushButton, QLineEdit, QTextEdit, QComboBox
)
from modules.app import app
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

# ==========================================
# БЛОК 1: Налаштування та розміри головного вікна
# ==========================================
MAIN_WINDOW_WIDTH = 1024
MAIN_WINDOW_HEIGHT = 800

main_window = QMainWindow()
primary_screen = app.primaryScreen()
primary_screen_size = primary_screen.size()

# Центрування вікна по центру екрана монітора
main_window.setGeometry(
    (primary_screen_size.width() // 2) - (MAIN_WINDOW_WIDTH // 2),
    (primary_screen_size.height() // 2) - (MAIN_WINDOW_HEIGHT // 2),
    MAIN_WINDOW_WIDTH,
    MAIN_WINDOW_HEIGHT
)
main_window.setWindowTitle('Practice')

# ==========================================
# БЛОК 2: Головний контейнер та загальний Layout
# ==========================================
# Створюємо головну рамку (фрейм) та встановлюємо чорний фон
main_frame = QFrame(parent=main_window)
main_frame.setFixedSize(MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT)
main_frame.setStyleSheet('background-color: #000000')

# Головний вертикальний компонувальник для розміщення елементів зверху вниз
main_layout = QVBoxLayout()
main_layout.setSpacing(15)
main_layout.setContentsMargins(20, 20, 20, 20)
main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
main_frame.setLayout(main_layout)

# ==========================================
# БЛОК 3: Верхнє поле введення (Перший елемент)
# ==========================================
top_line_edit = QLineEdit(parent=main_frame)
top_line_edit.setStyleSheet("""
    border: 2px solid white;
    color: white; 
    background-color: #1a1a1a;
    font-size: 16px;
""")
top_line_edit.setFixedSize(400, 40)
top_line_edit.setPlaceholderText("enter text 1")
main_layout.addWidget(top_line_edit)

# ==========================================
# БЛОК 4: Горизонтальний рядок з двома елементами (Другий блок)
# ==========================================
second_line_layout = QHBoxLayout()
second_line_layout.setSpacing(10)
second_line_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

# Ліве поле у рядку (ширше)
line_edit_left = QLineEdit(parent=main_frame)
line_edit_left.setStyleSheet("""
    border: 2px solid white;
    color: white; 
    background-color: #1a1a1a;
    font-size: 16px;
""")
line_edit_left.setFixedSize(280, 40)
line_edit_left.setPlaceholderText("enter text")

# Праве поле у рядку (вужче)
line_edit_right = QLineEdit(parent=main_frame)
line_edit_right.setStyleSheet("""
    border: 2px solid white;
    color: white; 
    background-color: #1a1a1a;
    font-size: 16px;
""")
line_edit_right.setFixedSize(110, 40)
line_edit_right.setPlaceholderText("text")

# Додаємо обидва поля в горизонтальний Layout
second_line_layout.addWidget(line_edit_left)
second_line_layout.addWidget(line_edit_right)

# Додаємо весь горизонтальний рядок у головний вертикальний Layout
main_layout.addLayout(second_line_layout)

# ==========================================
# БЛОК 5: Велике текстове поле по центру (Третій блок)
# ==========================================
text_edit = QTextEdit(parent=main_frame)
text_edit.setStyleSheet("""
    border: 2px solid white;
    color: white; 
    background-color: #1a1a1a;
    font-size: 16px;
""")
text_edit.setFixedSize(400, 300)
text_edit.setPlaceholderText("enter large text...")
main_layout.addWidget(text_edit)

# ==========================================
# БЛОК 6: Кнопка внизу (Четвертий блок)
# ==========================================
bottom_button = QPushButton("Button", parent=main_frame)
bottom_button.setStyleSheet("""
    border: 2px solid white;
    color: white; 
    background-color: #333333;
    font-size: 16px;
""")
bottom_button.setFixedSize(150, 40)
main_layout.addWidget(bottom_button)