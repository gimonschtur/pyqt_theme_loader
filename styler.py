import os
from enum import Enum, auto

class Theme(Enum):
    """Available themes for the application."""
    LIGHT = "light"
    DARK = "dark"

    def __str__(self) -> str:
        """Return the theme name as a string."""
        return self.value

def load_stylesheet(theme: Theme | str) -> str:
    """
    Load the QSS stylesheet content for the given theme.

    :param theme: Either Theme.LIGHT, Theme.DARK, or their string equivalents "light"/"dark".
    :return: QSS string content.
    :raises ValueError: If the theme name is invalid.
    :raises FileNotFoundError: If the QSS file is not found.
    """
    # Convert string to Theme enum if necessary
    if isinstance(theme, str):
        try:
            theme = Theme(theme.lower())
        except ValueError:
            raise ValueError(f"Unknown theme: {theme}. Expected 'light' or 'dark'.")

    # Get the directory where this script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    theme_file = os.path.join(current_dir, "themes", f"{theme.value}.qss")

    if not os.path.exists(theme_file):
        raise FileNotFoundError(f"Stylesheet not found: {theme_file}")

    with open(theme_file, 'r', encoding='utf-8') as f:
        return f.read()