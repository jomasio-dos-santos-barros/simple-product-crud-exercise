import tkinter as tk

from src.views import styles

class MainContent(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(
            master=master,
            bg=styles.BACKGROUND_COLOR,
            border=styles.BORDER_THICKNESS,
            borderwidth=styles.BORDER_WIDTH,
            width=styles.MAIN_CONTENT_WIDTH,
            height=styles.MAIN_CONTENT_HEIGHT,
        )
        self.master = master
        

        self.pack(fill="both", expand=True)  # Garante que o frame ocupe a tela