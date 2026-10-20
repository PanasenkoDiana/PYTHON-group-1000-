from PyQt6.QtWidgets import (
    QMainWindow,QFrame,QHBoxLayout,
    QVBoxLayout,QGridLayout,QScrollArea,
    QLabel,
    QPushButton,
    QLineEdit, QTextEdit, QComboBox
)
from modules.app import app
from PyQt6.QtCore import Qt

# QFont - відповідає за не складні стилі
from PyQt6.QtGui import QFont

# Створюємо змінну в якій вказуємо шрифт та його розмір
font = QFont("Arial", 50)

MAIN_WINDOW_WIDTH = 1024
MAIN_WINDOW_HEIGHT = 800

main_window = QMainWindow()
primary_screen = app.primaryScreen()

primary_screen_size = primary_screen.size()
primary_screen_width = primary_screen_size.width()
primary_screen_height = primary_screen_size.height()

main_window.setGeometry(
    (primary_screen_width//2)-(MAIN_WINDOW_WIDTH//2),
    (primary_screen_height//2)-(MAIN_WINDOW_HEIGHT//2),
    MAIN_WINDOW_WIDTH,
    MAIN_WINDOW_HEIGHT
)

main_window.setWindowTitle('Weather Project')
main_frame = QFrame(parent= main_window)
main_frame.setFixedSize(MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT)
main_frame.setStyleSheet('background-color: white')

main_layout= QHBoxLayout()
main_layout.setSpacing(0)
main_layout.setContentsMargins(0, 0, 0, 0)
main_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
main_frame.setLayout(main_layout)

scroll_area = QScrollArea(parent=main_frame)
scroll_area.setFixedSize(400,MAIN_WINDOW_HEIGHT)
scroll_area.setStyleSheet("background-color: #5c5959")
scroll_area.setWidgetResizable(True)
scroll_area.setHorizontalScrollBarPolicy(
    Qt.ScrollBarPolicy.ScrollBarAlwaysOff
)
main_layout.addWidget(scroll_area)

scroll_content = QFrame(parent=scroll_area)
scroll_content.setFixedWidth(390)
scroll_layout = QVBoxLayout()
scroll_layout.setSpacing(5)
scroll_layout.setContentsMargins(0, 0, 0, 0)
scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
scroll_content.setLayout(scroll_layout)
scroll_area.setWidget(scroll_content)

for i in range(50):
    item = QFrame(parent=scroll_content)
    item.setFixedSize(390, 50)
    item.setStyleSheet("background-color: #7d358f")

    item_layout = QHBoxLayout()
    item_layout.setContentsMargins(0,0,0,0)
    item_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    item.setLayout(item_layout)

    item_text = QLabel(
        text = f"item {i+1}",
        parent=item
    )
    item_text.setStyleSheet("""
        font-size:32px;
        color: #ff8c00;  
    """)
    item_layout.addWidget(item_text)
    scroll_layout.addWidget(item)


element_2 = QFrame(parent = main_frame)
element_2.setFixedSize(624,MAIN_WINDOW_HEIGHT)
element_2.setStyleSheet("background-color: #dcfcc5")
main_layout.addWidget(element_2)

# button = QPushButton(
#     parent=element_2,
#     text="Click"
# )

# border: 1px solid black - товщина стиль колір
# border-radius: 5px - закруглення кутів
# color: red; - колір для тексту кнопки
# padding: 10px; - внутрішні відступи в середині кнопки
# font-family: "Open Sans", Arial, sans-serif; - вказуємо шрифт
# button.setStyleSheet(
#     '''
#         border: 1px solid black;
#         border-radius: 5px;
#         color: red;
#         background-color: lightgray;
#         padding: 30px;
#         font-family: "Open Sans", Arial, sans-serif;
#         font-size: 50px;
#     '''
# )

# button.setFixedSize(250, 100)
# setFont - встанавлюємо наш шрифт для кнопки
# button.setFont(font)

# сигнал - дозволяє викликати якусь функцію при якійсь дії

# def button_click():
#     print("click")

# button.clicked.connect - обробка події
# button - наша кнопка
# clicked - подія натискання на кнопку
# connect - приєднуємо функцію
# button.clicked.connect(button_click)

element_2_layout = QHBoxLayout()
element_2_layout.setContentsMargins(10,10,10,10)
element_2_layout.setSpacing(20)
element_2_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
element_2.setLayout(element_2_layout) 

# QLineEdit - клас який створює поле для вводу (короткого тексту - тексту в один рядок)
line_edit = QLineEdit(parent = element_2)
line_edit.setStyleSheet("""
    border: 2px solid black;
    color: black; 
    background-color: red;
    font-size: 20px;
""")
line_edit.setFixedSize(150, 50)

# setPlaceholderText - створює текст-підказку для користувача у полі для вводу
line_edit.setPlaceholderText("enter text")

# Створюємо функцію яка приймає текст який вводить користувач у QLineEdit
def line_edit_text_changed(text):
    print(f"text: {text}")

# line_edit.textChanged.connect - обробка події змінення тексту
# line_edit - наше поле вводу
# textChanged - подія змінення тексту
# connect - приєднуємо відповідну функцію для обробки події
line_edit.textChanged.connect(line_edit_text_changed)

element_2_layout.addWidget(line_edit)

# QTextEdit - клас який створю велике поле для вводу (багаторядкове поле)
# text_edit = QTextEdit(parent= element_2)

# text_edit.setStyleSheet("""
#     border: 2px solid black;
#     color: black; 
#     background-color: red;
#     font-size: 20px;
# """)
# line_edit.setFixedSize(150, 50)
# element_2_layout.addWidget(text_edit)
# text_edit.setPlaceholderText("enter text")

# # Створюємо функцію яка обробляє текст який вводиться у QTextEdit
# # !Функція не приймає параментрів
# # Текст отримується завдяки методу text_edit.toPlainText() - повертає звичайний текст без форматування
# # Якщо потрібно повернути текст зі збереженням формату використовуємо text_edit.toHtml()
# def text_edit_text_change():
#     print(f'text: {text_edit.toPlainText()}')

# text_edit.textChanged.connect(text_edit_text_change)


# QComboBox - клас для створеня випадаючого меню
combo_box = QComboBox(parent= element_2)

# Ми можемо додавати до нього єлементи двома спосібами
# 1. addItems - додає одразу декілька єлементів
combo_box.addItems(["option 1", "option 2", "option 3"])
# 2. addItem - додає тілько по одному элементу
combo_box.addItem("option 4")
combo_box.addItem("option 5")
combo_box.addItem("option 6")
combo_box.addItem("option 7")
element_2_layout.addWidget(combo_box)

# QComboBox{в середині задає стилі} - задає стилі для основного меню
# QComboBox QAbstractItemView{в середині задає стилі} - задає стилі для випадаючих єлементів
combo_box.setStyleSheet("""
    QComboBox{
        background-color: blue;
        color: black;
        border: 2px solid black 
    }
    QComboBox QAbstractItemView{
        background-color: red;
        color: black;
        border: 2px solid black;
    }
""")

def combo_box_option_changed(option):
    print(f"Selected option: {option}")

# combo_box.currentTextChanged.connect() - обробляє подію зміни вибору
combo_box.currentTextChanged.connect(combo_box_option_changed)