import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QLineEdit, QLabel, QWidget, QVBoxLayout,
                             QHBoxLayout, QDoubleSpinBox, QSpinBox,
                             QWidget, )


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(350, 550))
        self.setWindowTitle("Tip Calculator")
        layout = QVBoxLayout()

        title = QLabel("Tip Calculator")
        font = title.font()
        font.setPointSize(30)
        title.setFont(font)
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter | 
                           Qt.AlignmentFlag.AlignVCenter)

        price_row = QHBoxLayout()
        price_label = QLabel("Price:")
        self.price_spinbox = QDoubleSpinBox()
        self.price_spinbox.setMinimum(0)
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
        people_spinbox = QSpinBox()
        people_spinbox.setMinimum(1)
        

        people_row.addWidget(people_label)
        people_row.addWidget(people_spinbox)


        button = QPushButton("Calculate")


        # Add widgets to the layout
        layout.addWidget(title)
        layout.addLayout(price_row)
        layout.addLayout(percentage_row)
        layout.addLayout(people_row)
        layout.addWidget(button)

        # Set the central widget of the Window.
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Setting Alignment for Each row widget
        price_row.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        percentage_row.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        people_row.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        # Set the main layout
        gui = QWidget()
        gui.setLayout(layout)
        self.setCentralWidget(gui)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()