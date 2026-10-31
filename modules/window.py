
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QMainWindow,
    QScrollArea,
    QVBoxLayout
)
from PyQt6.QtGui import QMouseEvent, QKeyEvent

from modules.app import app


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        MAIN_WINDOW_WIDTH = 1200
        MAIN_WINDOW_HEIGHT = 800

        primary_screen = app.primaryScreen()
        primary_screen_size = primary_screen.size()

        primary_screen_width = primary_screen_size.width()
        primary_screen_height = primary_screen_size.height()

        self.setGeometry(
            (primary_screen_width // 2) - (MAIN_WINDOW_WIDTH // 2),
            (primary_screen_height // 2) - (MAIN_WINDOW_HEIGHT // 2),
            MAIN_WINDOW_WIDTH,
            MAIN_WINDOW_HEIGHT
        )

        self.setWindowTitle("Weather app")

        main_frame = QFrame(parent=self)
        main_frame.setStyleSheet("background-color: #202124;")

        self.setCentralWidget(main_frame)

        main_layout = QHBoxLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_frame.setLayout(main_layout)

        scroll_area = QScrollArea(parent=main_frame)
        scroll_area.setFixedSize(370, 800)

        # Вказує, що вкладений віджет не буде успадковувати розміри scroll area
        scroll_area.setWidgetResizable(False)

        # Відключає горизонтальний скролбар
        scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        scroll_area.setStyleSheet(
            "background-color: #3b4252;"
        )

        scroll_content = QFrame(parent=scroll_area)
        scroll_content.setFixedWidth(370)
        scroll_content.setStyleSheet(
            "background-color: #434c5e;"
        )

        scroll_layout = QVBoxLayout()
        scroll_layout.setSpacing(20)
        scroll_layout.setContentsMargins(0, 0, 0, 0)

        # Для того щоб елементи завжди відображалися зверху
        scroll_layout.setAlignment(
            Qt.AlignmentFlag.AlignTop
        )

        scroll_content.setLayout(scroll_layout)

        for i in range(50):
            item = QFrame(parent=scroll_content)
            item.setFixedSize(370, 90)
            item.setStyleSheet("background-color: gray;")
            scroll_layout.addWidget(item)

        scroll_area.setWidget(scroll_content)
        main_layout.addWidget(scroll_area)

        right_frame = QFrame(parent=main_frame)
        right_frame.setFixedSize(828, 800)
        right_frame.setStyleSheet(
            "background-color: #d08770;"
        )

        right_frame_layout = QHBoxLayout()
        right_frame.setLayout(right_frame_layout)

        main_layout.addWidget(right_frame)

    def mousePressEvent(self, event: QMouseEvent):

        if event.button() == Qt.MouseButton.LeftButton:
            print("left down")

        elif event.button() == Qt.MouseButton.RightButton:
            print("right down")

        # вызывает стандартный обработчик события нажатия мыши, 
        # который определён в родительском классе QMainWindow.
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        
        # Демонструємо можливість отримання координат курсору
        # (без пояснення локальних та глобальних координат)
        print(event.pos())
        
        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
            
        # Ті ж самі перевірки, що і у .mousePressEvent()
        # Таким чином демонструємо, що перевірки між press та release не відрізняються
        if event.button() == Qt.MouseButton.LeftButton:
            print("left up")
        elif event.button() == Qt.MouseButton.RightButton:
            print("right up")
        
        return super().mouseReleaseEvent(event)

    def keyPressEvent(self, event: QKeyEvent):
            
        # Пояснюємо різницю між key і text
        key = event.key()
        text = event.text()
        
        print(key, text)
        
        # Перевірка будь-якої клавіши
        if key == Qt.Key.Key_A:
            print("key A pressed")
        
        # Перевірки для Enter та Return
        if key == Qt.Key.Key_Enter or key == Qt.Key.Key_Return:
            print("Enter/Return pressed")

        return super().keyPressEvent(event)
        
    def keyReleaseEvent(self, event: QKeyEvent):
        
        # Повторюємо перевірки з keyPressEvent
        # Таким чином демонструємо, 
        # що між press та release перевірки не відрізняються
        key = event.key()
        text = event.text()
        
        if key == Qt.Key.Key_A:
            print("key A released")
        
        return super().keyReleaseEvent(event)

main_window = MainWindow()
main_window.show()
