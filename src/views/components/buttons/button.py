import tkinter as tk
from typing import Callable, Literal

from src.views import styles

class Button(tk.Button):
    """
    Base class for creating buttons in the application.
    Inherits from tk.Button and applies custom styles.

    Parameters:
        master (tk.Frame) The parent widget.
        text (str): The text to display on the button.
        command (Callable): The function to call when the button is clicked.
        type (str): The type of button, either "confirm" or "cancel". Default is "confirm".
        width (int): The width of the button. Default is styles.BUTTON_WIDTH.
        height (int): The height of the button. Default is styles.BUTTON_HEIGHT.
    """
    def __init__(
            self, 
            master: tk.Frame, 
            text: str, 
            command=Callable,
            type: Literal["confirm", "cancel"] = "confirm",
            width: int = styles.BUTTON_WIDTH,
            height: int = styles.BUTTON_HEIGHT
            ):
        super().__init__(
            master=master,
            text=text,
            command=command,
            bg=styles.CONFIRM_BUTTON_COLOR if type == "confirm" else styles.CANCEL_BUTTON_COLOR,
            fg="#FFFFFF",
            font=styles.BUTTON_FONT,
            borderwidth=styles.BORDER_WIDTH,
            width=width,
            height=height,
            highlightthickness=styles.BORDER_THICKNESS,
            highlightbackground=styles.FOREGROUND_COLOR,
            highlightcolor=styles.FOREGROUND_COLOR,
            activebackground=styles.CONFIRM_BUTTON_ACTIVE_COLOR if type == "confirm" else styles.CANCEL_BUTTON_ACTIVE_COLOR,
            activeforeground=styles.TEXT_COLOR_LIGHT,
            bd=0,
            cursor="hand2",
        )