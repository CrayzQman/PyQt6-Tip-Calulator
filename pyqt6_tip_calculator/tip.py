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

        self.price_row = QHBoxLayout()
        self.price_label = QLabel("Price:")
        self.price_spinbox = QDoubleSpinBox()
        self.price_spinbox.setMinimum(0)
        self.price_spinbox.setPrefix("$")
        

        self.price_row.addWidget(self.price_label)
        self.price_row.addWidget(self.price_spinbox)


        self.percentage_row = QHBoxLayout()
        self.percentage_label = QLabel("Percentage:")
        self.percentage_spinbox = QDoubleSpinBox()
        self.percentage_spinbox.setMinimum(1)
        self.percentage_spinbox.setSuffix("%")
        

        self.percentage_row.addWidget(self.percentage_label)
        self.percentage_row.addWidget(self.percentage_spinbox)


        self.people_row = QHBoxLayout()
        self.people_label = QLabel("People:")
        self.people_spinbox = QSpinBox()
        self.people_spinbox.setMinimum(1)
        

        self.people_row.addWidget(self.people_label)
        self.people_row.addWidget(self.people_spinbox)


        self.button = QPushButton("Calculate")


        # Add widgets to the layout
        layout.addWidget(title)
        layout.addLayout(self.price_row)
        layout.addLayout(self.percentage_row)
        layout.addLayout(self.people_row)
        layout.addWidget(self.button)

        # Set the central widget of the Window.
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Setting Alignment for Each row widget
        self.price_row.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.percentage_row.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.people_row.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        # Set the main layout
        gui = QWidget()
        gui.setLayout(layout)
        self.setCentralWidget(gui)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()