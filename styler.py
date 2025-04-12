import os
from enum import Enum, auto

class Theme(Enum):
    """Available themes for the application."""
    LIGHT = "light"
    DARK = "dark"

    def __str__(self) -> str:
        """Return the theme name as a string."""
        return self.value

def load_stylesheet(theme: Theme) -> str:
    """
    Load the QSS stylesheet content for the given theme.
    This will combine the base stylesheet with the theme-specific colors.

    :param theme: Either Theme.LIGHT, Theme.DARK, or their string equivalents "light"/"dark".
    :return: Combined QSS string content.
    :raises ValueError: If the theme name is invalid.
    :raises FileNotFoundError: If any of the QSS files are not found.
    """
    # Convert string to Theme enum if necessary
    if isinstance(theme, str):
        try:
            theme = Theme(theme.lower())
        except ValueError:
            raise ValueError(f"Unknown theme: {theme}. Expected 'light' or 'dark'.")

    # Get the directory where this script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_file = os.path.join(current_dir, "themes", "base.qss")
    theme_file = os.path.join(current_dir, "themes", f"{theme.value}.qss")

    # Check if files exist
    if not os.path.exists(base_file):
        raise FileNotFoundError(f"Base stylesheet not found: {base_file}")
    if not os.path.exists(theme_file):
        raise FileNotFoundError(f"Theme stylesheet not found: {theme_file}")

    # Load and combine stylesheets
    with open(base_file, 'r', encoding='utf-8') as f:
        base_style = f.read()

    with open(theme_file, 'r', encoding='utf-8') as f:
        theme_style = f.read()

    # Combine styles - theme-specific styles should override base styles
    return f"{base_style}\n\n{theme_style}"