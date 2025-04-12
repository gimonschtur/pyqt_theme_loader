from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QComboBox, QCheckBox, QRadioButton,
    QSlider, QProgressBar, QTabWidget, QTextEdit, QListView,
    QTreeView, QTableView, QGroupBox, QSpinBox, QDateEdit, QMenuBar,
    QStatusBar, QToolBar
)
from PyQt6.QtCore import Qt, QDate
import sys
import traceback
import os

# Add the parent directory to the Python path so we can import styler
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styler import load_stylesheet

class DemoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Modern Theme Demo")
        self.resize(800, 600)

        self.setMenuBar(QMenuBar())
        self.setStatusBar(QStatusBar())
        self.addToolBar(QToolBar("Toolbar"))

        central = QWidget()
        layout = QVBoxLayout()

        # Add theme selector at the top
        theme_layout = QHBoxLayout()
        theme_layout.addWidget(QLabel("Theme:"))
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["light", "dark"])
        self.theme_combo.currentTextChanged.connect(self.change_theme)
        theme_layout.addWidget(self.theme_combo)
        theme_layout.addStretch()
        layout.addLayout(theme_layout)

        layout.addWidget(QLabel("Label: Hello World"))
        layout.addWidget(QLineEdit("Line Edit"))

        combo = QComboBox()
        combo.addItems(["Item 1", "Item 2", "Item 3"])
        layout.addWidget(combo)

        layout.addWidget(QCheckBox("Check Me"))
        layout.addWidget(QRadioButton("Radio Me"))

        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(50)
        layout.addWidget(slider)

        progress = QProgressBar()
        progress.setValue(75)
        layout.addWidget(progress)

        tabs = QTabWidget()
        tab1 = QWidget()
        tab1.setLayout(QVBoxLayout())
        tab1.layout().addWidget(QTextEdit("This is a QTextEdit."))
        tab1.layout().addWidget(QListView())
        tab1.layout().addWidget(QTreeView())
        tab1.layout().addWidget(QTableView())
        tabs.addTab(tab1, "Tab 1")

        tab2 = QWidget()
        tab2.setLayout(QVBoxLayout())
        tab2.layout().addWidget(QSpinBox())
        tab2.layout().addWidget(QDateEdit(QDate.currentDate()))
        tabs.addTab(tab2, "Tab 2")

        layout.addWidget(tabs)

        group = QGroupBox("Grouped Controls")
        group_layout = QHBoxLayout()
        group_layout.addWidget(QPushButton("Button 1"))
        group_layout.addWidget(QPushButton("Button 2"))
        group.setLayout(group_layout)
        layout.addWidget(group)

        central.setLayout(layout)
        self.setCentralWidget(central)

    def change_theme(self, theme_name):
        try:
            stylesheet = load_stylesheet(theme_name)
            QApplication.instance().setStyleSheet(stylesheet)
        except Exception as e:
            print(f"Error changing theme to {theme_name}:", str(e))
            print("Traceback:")
            traceback.print_exc()

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        try:
            # Start with light theme by default
            stylesheet = load_stylesheet("light")
            app.setStyleSheet(stylesheet)
        except Exception as e:
            print("Error loading stylesheet:", str(e))
            print("Traceback:")
            traceback.print_exc()
            sys.exit(1)

        window = DemoApp()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        print("Error running demo:", str(e))
        print("Traceback:")
        traceback.print_exc()
        sys.exit(1)
