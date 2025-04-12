import os

def load_stylesheet(theme_name: str) -> str:
    """
    Load the QSS stylesheet content for the given theme.

    :param theme_name: Either "light" or "dark".
    :return: QSS string content.
    :raises ValueError: If the theme name is invalid.
    :raises FileNotFoundError: If the QSS file is not found.
    """
    # Get the directory where this script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    theme_file = os.path.join(current_dir, "themes", f"{theme_name}.qss")

    if theme_name not in ["light", "dark"]:
        raise ValueError(f"Unknown theme: {theme_name}. Expected 'light' or 'dark'.")

    if not os.path.exists(theme_file):
        raise FileNotFoundError(f"Stylesheet not found: {theme_file}")

    with open(theme_file, 'r', encoding='utf-8') as f:
        return f.read()