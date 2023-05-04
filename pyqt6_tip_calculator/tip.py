import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QLineEdit, QLabel, QWidget, QVBoxLayout,
                             QHBoxLayout, QDoubleSpinBox)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(500, 400))
        self.setWindowTitle("Tip Calculator")
        layout = QVBoxLayout()

        title = QLabel("Tip Calculator")
        font = title.font()
        font.setPointSize(30)
        title.setFont(font)
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter | 
                           Qt.AlignmentFlag.AlignTop)

        price_row = QHBoxLayout()
        price_label = QLabel("Price:")
        price_spinbox = QDoubleSpinBox()
        price_spinbox.setMinimum(0)
        price_spinbox.setPrefix("$")

        price_row.addWidget(price_label)
        price_row.addWidget(price_spinbox)


        percentage_row = QHBoxLayout()
        percentage_label = QLabel("Percentage:")
        percentage_spinbox = QDoubleSpinBox()
        percentage_spinbox.setMinimum(1)
        percentage_spinbox.setSuffix("%")

        percentage_row.addWidget(percentage_label)
        percentage_row.addWidget(percentage_spinbox)


        people_row = QHBoxLayout()
        people_label = QLabel("People:")
        people_spinbox = QDoubleSpinBox()
        people_spinbox.setMinimum(1)

        people_row.addWidget(people_label)
        people_row.addWidget(people_spinbox)


        button = QPushButton("calculate")

        text = QLineEdit()
        text.setMaxLength(900)
        text.setPlaceholderText("Enter your text")

        
        # Add widgets to the layout
        layout.addWidget(title)
        layout.addLayout(price_row)
        layout.addLayout(percentage_row)
        layout.addLayout(people_row)
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