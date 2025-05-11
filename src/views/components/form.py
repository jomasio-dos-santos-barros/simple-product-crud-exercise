import tkinter as tk

from src.views import styles
from src.views.components.line_buttons import LineButtons

class Form(tk.Frame):
    """
    A class that represents a form in the application.

    Attributes:
        master (tk.Tk): The main application window.
        widgets (dict): A dictionary to store the widgets in the form. Keys are "labels", "inputs", and "buttons". Values are lists of the respective widgets.
    Methods:
        add_input(input: tk.Entry, label: str = None): Adds an input field to the form.
        add_button(button: tk.Button): Adds a button to the form.
    """
    def __init__(self, master: tk.Tk, title: str = None):
        super().__init__(
            master=master,
            bg=styles.FOREGROUND_COLOR,
            border=styles.BORDER_THICKNESS,
            borderwidth=styles.BORDER_WIDTH,
            width=styles.FORM_WIDTH,
            height=styles.FORM_HEIGHT,
        )
        self.master = master
        self.widgets = {
            "labels": [],
            "inputs": [],
            "buttons": [],
        }
        if title:
            self.title = tk.Label(
                self,
                text=title,
                bg=styles.FOREGROUND_COLOR,
                foreground=styles.TEXT_COLOR_DARK,
                font=styles.TITLE_FONT,
            )
            self.title.pack(pady=5, anchor="center")
            self.widgets["labels"].append(self.title)
        

    def add_input(self, input: tk.Entry, label: str = None):
        if label:
            label = tk.Label(self, text=label, bg=styles.FOREGROUND_COLOR, foreground=styles.TEXT_COLOR_DARK, font=styles.LABEL_FONT)
            label.pack(pady=20, anchor="center") 
            self.widgets["labels"].append(label)
        self.widgets["inputs"].append(input)
        input.pack(padx=10, pady=20, anchor="center")  # Removido fill="x" para evitar que o input ocupe toda a largura

    def add_buttons(self, buttons: list[tk.Button]):
        # Cria o Frame para os botões
        self.div_buttons = LineButtons(
            self,
            buttons=buttons,
        )
        self.widgets["buttons"].extend(buttons)