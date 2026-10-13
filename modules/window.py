
from PyQt6.QtWidgets import (
    QMainWindow,QFrame,QHBoxLayout,
    QVBoxLayout,QGridLayout,QScrollArea,
    QLabel
)
from modules.app import app
from PyQt6.QtCore import Qt
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
