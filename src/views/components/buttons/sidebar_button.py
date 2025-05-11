import tkinter as tk
from typing import Callable

from src.views import styles

class SidebarButton(tk.Button):
    def __init__(self, master: tk.Tk, text: str, command: Callable=None):
        super().__init__(
            master=master,
            bg=styles.FOREGROUND_COLOR,
            border=2,
            borderwidth=1,
            command=command,
            text=text
        )
        self.master = master