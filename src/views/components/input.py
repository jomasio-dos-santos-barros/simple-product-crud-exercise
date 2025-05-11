import tkinter as tk

from src.views import styles


class Input(tk.Entry):
    def __init__(self, master: tk.Frame, placeholder: str):
        super().__init__(
            master=master,
            bg=styles.FOREGROUND_COLOR,
            font=styles.TEXT_COLOR_DARK,
            borderwidth=styles.BORDER_WIDTH,
            highlightthickness=styles.BORDER_THICKNESS,
            width=styles.INPUT_WIDTH,
        )
        self.placeholder = placeholder
        self.placeholder_color = "gray"  # Cor do placeholder
        self.default_fg_color = self.cget("fg")  # Cor padrão do texto

        self.insert_placeholder()

        # Adiciona eventos para gerenciar o placeholder
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

    def insert_placeholder(self):
        """Insere o placeholder no campo de entrada."""
        self.insert(0, self.placeholder)
        self.config(fg=self.placeholder_color)

    def on_focus_in(self, event):
        """Remove o placeholder quando o campo ganha foco."""
        if self.get() == self.placeholder and self.cget("fg") == self.placeholder_color:
            self.delete(0, "end")
            self.config(fg=self.default_fg_color)

    def on_focus_out(self, event):
        """Reinsere o placeholder se o campo estiver vazio ao perder o foco."""
        if not self.get():
            self.insert_placeholder()