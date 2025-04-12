from PySide2.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QPushButton, QLabel, QLineEdit, QComboBox, QCheckBox, QRadioButton,
    QSlider, QProgressBar, QTabWidget, QTextEdit, QListView, QScrollArea,
    QTreeView, QTableView, QGroupBox, QSpinBox, QDateEdit, QTimeEdit, QMenuBar,
    QStatusBar, QToolBar, QMenu, QToolButton, QFontComboBox, QDial, QCalendarWidget,
    QDoubleSpinBox, QPlainTextEdit, QScrollBar, QSplitter, QStackedWidget,
    QFrame, QLCDNumber, QSizeGrip
)
from PySide2.QtCore import Qt, QDate, QTime, QStringListModel
from PySide2.QtGui import QStandardItemModel, QStandardItem
import sys
import traceback
import os

# Add the parent directory to the Python path so we can import styler
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styler import load_stylesheet

class DemoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide2 Modern Theme Demo")
        self.resize(1200, 800)

        # Setup MenuBar
        self.setup_menubar()

        # Setup StatusBar
        self.statusBar().showMessage("Ready")

        # Setup ToolBar
        self.setup_toolbar()

        # Create main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # Theme selector
        theme_layout = QHBoxLayout()
        theme_layout.addWidget(QLabel("Theme:"))
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["light", "dark"])
        self.theme_combo.currentTextChanged.connect(self.change_theme)
        theme_layout.addWidget(self.theme_combo)
        theme_layout.addStretch()
        main_layout.addLayout(theme_layout)

        # Create scroll area for the content
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content_widget = QWidget()
        content_layout = QVBoxLayout()

        # Add all widget demonstrations
        self.setup_input_widgets(content_layout)
        self.setup_buttons_widgets(content_layout)
        self.setup_display_widgets(content_layout)
        self.setup_container_widgets(content_layout)
        self.setup_advanced_widgets(content_layout)

        content_widget.setLayout(content_layout)
        scroll.setWidget(content_widget)
        main_layout.addWidget(scroll)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def setup_menubar(self):
        menubar = self.menuBar()

        # File Menu
        file_menu = menubar.addMenu("File")
        file_menu.addAction("New")
        file_menu.addAction("Open")
        file_menu.addSeparator()
        file_menu.addAction("Exit")

        # Edit Menu
        edit_menu = menubar.addMenu("Edit")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")

        # Help Menu
        help_menu = menubar.addMenu("Help")
        help_menu.addAction("About")

    def setup_toolbar(self):
        toolbar = self.addToolBar("Main Toolbar")
        toolbar.addAction("New")
        toolbar.addAction("Open")
        toolbar.addSeparator()

        tool_button = QToolButton()
        tool_button.setText("More")
        tool_menu = QMenu()
        tool_menu.addAction("Action 1")
        tool_menu.addAction("Action 2")
        tool_button.setMenu(tool_menu)
        toolbar.addWidget(tool_button)

    def setup_input_widgets(self, layout):
        group = QGroupBox("Input Widgets")
        grid = QGridLayout()

        # Text inputs
        grid.addWidget(QLabel("QLineEdit:"), 0, 0)
        grid.addWidget(QLineEdit("Sample text"), 0, 1)

        grid.addWidget(QLabel("QTextEdit:"), 1, 0)
        grid.addWidget(QTextEdit("Sample multi-line text"), 1, 1)

        grid.addWidget(QLabel("QPlainTextEdit:"), 2, 0)
        grid.addWidget(QPlainTextEdit("Plain text editor"), 2, 1)

        # Numeric inputs
        grid.addWidget(QLabel("QSpinBox:"), 3, 0)
        spin = QSpinBox()
        spin.setValue(42)
        grid.addWidget(spin, 3, 1)

        grid.addWidget(QLabel("QDoubleSpinBox:"), 4, 0)
        double_spin = QDoubleSpinBox()
        double_spin.setValue(3.14)
        grid.addWidget(double_spin, 4, 1)

        # Date and time inputs
        grid.addWidget(QLabel("QDateEdit:"), 5, 0)
        grid.addWidget(QDateEdit(QDate.currentDate()), 5, 1)

        grid.addWidget(QLabel("QTimeEdit:"), 6, 0)
        grid.addWidget(QTimeEdit(QTime.currentTime()), 6, 1)

        # Combo boxes
        grid.addWidget(QLabel("QComboBox:"), 7, 0)
        combo = QComboBox()
        combo.addItems(["Option 1", "Option 2", "Option 3"])
        grid.addWidget(combo, 7, 1)

        grid.addWidget(QLabel("QFontComboBox:"), 8, 0)
        grid.addWidget(QFontComboBox(), 8, 1)

        group.setLayout(grid)
        layout.addWidget(group)

    def setup_buttons_widgets(self, layout):
        group = QGroupBox("Buttons and Switches")
        grid = QGridLayout()

        # Regular button
        grid.addWidget(QLabel("QPushButton:"), 0, 0)
        grid.addWidget(QPushButton("Click Me"), 0, 1)

        # Tool button
        grid.addWidget(QLabel("QToolButton:"), 1, 0)
        tool_btn = QToolButton()
        tool_btn.setText("Tool")
        grid.addWidget(tool_btn, 1, 1)

        # Checkbox
        grid.addWidget(QLabel("QCheckBox:"), 2, 0)
        check = QCheckBox("Check me")
        check.setChecked(True)
        grid.addWidget(check, 2, 1)

        # Radio buttons
        grid.addWidget(QLabel("QRadioButton:"), 3, 0)
        radio_layout = QHBoxLayout()
        radio1 = QRadioButton("Option 1")
        radio2 = QRadioButton("Option 2")
        radio1.setChecked(True)
        radio_layout.addWidget(radio1)
        radio_layout.addWidget(radio2)
        radio_container = QWidget()
        radio_container.setLayout(radio_layout)
        grid.addWidget(radio_container, 3, 1)

        group.setLayout(grid)
        layout.addWidget(group)

    def setup_display_widgets(self, layout):
        group = QGroupBox("Display Widgets")
        grid = QGridLayout()

        # Progress bar
        grid.addWidget(QLabel("QProgressBar:"), 0, 0)
        progress = QProgressBar()
        progress.setValue(75)
        grid.addWidget(progress, 0, 1)

        # Slider
        grid.addWidget(QLabel("QSlider:"), 1, 0)
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(50)
        grid.addWidget(slider, 1, 1)

        # Dial
        grid.addWidget(QLabel("QDial:"), 2, 0)
        dial = QDial()
        dial.setValue(30)
        grid.addWidget(dial, 2, 1)

        # LCD Number
        grid.addWidget(QLabel("QLCDNumber:"), 3, 0)
        lcd = QLCDNumber()
        lcd.display(42)
        grid.addWidget(lcd, 3, 1)

        group.setLayout(grid)
        layout.addWidget(group)

    def setup_container_widgets(self, layout):
        group = QGroupBox("Container Widgets")
        container_layout = QVBoxLayout()

        # Tab Widget
        tabs = QTabWidget()

        # List View Tab
        list_tab = QWidget()
        list_layout = QVBoxLayout()
        list_view = QListView()
        model = QStringListModel()
        model.setStringList(["Item 1", "Item 2", "Item 3"])
        list_view.setModel(model)
        list_layout.addWidget(list_view)
        list_tab.setLayout(list_layout)
        tabs.addTab(list_tab, "QListView")

        # Tree View Tab
        tree_tab = QWidget()
        tree_layout = QVBoxLayout()
        tree_view = QTreeView()
        tree_model = QStandardItemModel()
        root = tree_model.invisibleRootItem()
        item1 = QStandardItem("Item 1")
        item1.appendRow(QStandardItem("Subitem 1"))
        root.appendRow(item1)
        tree_view.setModel(tree_model)
        tree_layout.addWidget(tree_view)
        tree_tab.setLayout(tree_layout)
        tabs.addTab(tree_tab, "QTreeView")

        # Table View Tab
        table_tab = QWidget()
        table_layout = QVBoxLayout()
        table_view = QTableView()
        table_model = QStandardItemModel(3, 3)
        for row in range(3):
            for col in range(3):
                item = QStandardItem(f"Item {row},{col}")
                table_model.setItem(row, col, item)
        table_view.setModel(table_model)
        table_layout.addWidget(table_view)
        table_tab.setLayout(table_layout)
        tabs.addTab(table_tab, "QTableView")

        container_layout.addWidget(tabs)

        # Splitter
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(QTextEdit("Left"))
        splitter.addWidget(QTextEdit("Right"))
        container_layout.addWidget(splitter)

        group.setLayout(container_layout)
        layout.addWidget(group)

    def setup_advanced_widgets(self, layout):
        group = QGroupBox("Advanced Widgets")
        advanced_layout = QVBoxLayout()

        # Calendar
        calendar = QCalendarWidget()
        advanced_layout.addWidget(calendar)

        # Stacked Widget
        stack = QStackedWidget()
        stack.addWidget(QLabel("Page 1"))
        stack.addWidget(QLabel("Page 2"))
        advanced_layout.addWidget(stack)

        # Frame
        frame = QFrame()
        frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        frame.setLineWidth(2)
        frame_layout = QVBoxLayout()
        frame_layout.addWidget(QLabel("Frame Content"))
        frame.setLayout(frame_layout)
        advanced_layout.addWidget(frame)

        group.setLayout(advanced_layout)
        layout.addWidget(group)

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
        sys.exit(app.exec_())
    except Exception as e:
        print("Error running demo:", str(e))
        print("Traceback:")
        traceback.print_exc()
        sys.exit(1)
