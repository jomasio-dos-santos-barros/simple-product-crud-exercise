import tkinter as tk


class LineButtons(tk.Frame):
    """
    A class that represents a line of buttons in the application.

    Attributes:
        master (tk.Frame): The parent widget.
        buttons (list): A list to store the buttons in the line.
    """
    def __init__(self, master: tk.Frame, buttons: list[tk.Button] = None):
        super().__init__(master=master, bg=master.cget("bg"))
        self.buttons = buttons if buttons else []
        self.master = master
        self.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza o Frame no pai
        self.create_widgets()

    def create_widgets(self):
        # Obtém a largura e altura do Frame pai
        # self.update_idletasks()  # Garante que as dimensões estejam atualizadas
        # parent_width = self.master.winfo_width()
        # parent_height = self.master.winfo_height()

        # Calcula as coordenadas para centralizar os botões
        x = 225
        y = 550
        # Adiciona cada botão ao Frame e posiciona em coordenadas absolutas
        for index, button in enumerate(self.buttons, 1):
            button.place(x=x + (index * 200), y=y, anchor="center")  # Posiciona os botões lado a lado