import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QLineEdit, QLabel, QWidget, QVBoxLayout)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(500, 400))
        self.setWindowTitle("Tip Calculator")
        layout = QVBoxLayout()

        button = QPushButton("calculate")

        text = QLineEdit()
        text.setMaxLength(900)
        text.setPlaceholderText("Enter your text")

        title = QLabel("Tip Calculator")
        font = title.font()
        font.setPointSize(30)
        title.setFont(font)
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter | 
                           Qt.AlignmentFlag.AlignTop)

        # Add widgets to the layout
        layout.addWidget(title)
        layout.addWidget(text)
        layout.addWidget(button)

        # Set the central widget of the Window.
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()