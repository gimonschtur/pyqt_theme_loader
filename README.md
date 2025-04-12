# PyQt Theme Loader

A modern theme loader for PyQt/PySide applications that provides consistent light and dark themes across different Qt widgets. This project includes ready-to-use stylesheets and demo applications showing their usage with PyQt5, PyQt6, and PySide2.

## Features

- Modern flat design themes (Light and Dark)
- Comprehensive widget coverage
- Cross-framework compatibility (PyQt5, PyQt6, PySide2)
- Easy-to-use theme loading mechanism
- Demo applications showcasing all styled widgets
- Type-safe theme selection using enums

## Requirements

- Python 3.9 or higher
- One of the following Qt frameworks:
  - PyQt5 (>= 5.15.0)
  - PyQt6 (>= 6.0.0)
  - PySide2 (>= 5.15.0)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pyqt_theme_loader.git
cd pyqt_theme_loader
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from styler import load_stylesheet, Theme

# Load a theme
stylesheet = load_stylesheet(Theme.LIGHT)  # or Theme.DARK

# Apply to your application
app = QApplication([])
app.setStyleSheet(stylesheet)
```

### Theme Switching Example

```python
from PyQt5.QtWidgets import QApplication, QMainWindow
from styler import load_stylesheet, Theme

class MainWindow(QMainWindow):
    def change_theme(self, theme: Theme):
        stylesheet = load_stylesheet(theme)
        QApplication.instance().setStyleSheet(stylesheet)

    def switch_to_dark(self):
        self.change_theme(Theme.DARK)

    def switch_to_light(self):
        self.change_theme(Theme.LIGHT)
```

### Running the Demo Applications

The project includes three demo applications showcasing all styled widgets:

```bash
# PyQt5 Demo
python demo/pyqt5_theme_demo.py

# PyQt6 Demo
python demo/pyqt6_theme_demo.py

# PySide2 Demo
python demo/pyside2_theme_demo.py
```

## Styled Widgets

The themes provide consistent styling for the following Qt widgets:

1. Input Widgets
   - QLineEdit
   - QTextEdit
   - QPlainTextEdit
   - QSpinBox
   - QDoubleSpinBox
   - QDateEdit
   - QTimeEdit
   - QComboBox
   - QFontComboBox

2. Buttons and Switches
   - QPushButton
   - QToolButton
   - QCheckBox
   - QRadioButton

3. Display Widgets
   - QProgressBar
   - QSlider
   - QDial
   - QLCDNumber

4. Container Widgets
   - QTabWidget
   - QListView
   - QTreeView
   - QTableView
   - QSplitter

5. Advanced Widgets
   - QCalendarWidget
   - QStackedWidget
   - QFrame

6. Window Components
   - QMenuBar
   - QToolBar
   - QStatusBar
   - QScrollArea

## Theme Customization

The theme files are located in the `themes` directory:
- `themes/light.qss` - Light theme stylesheet
- `themes/dark.qss` - Dark theme stylesheet

You can modify these files to customize the appearance of your application.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.