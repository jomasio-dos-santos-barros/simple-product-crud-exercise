import tkinter as tk

from src.views import styles

class SideBar(tk.Frame):
    def __init__(self, master: tk.Frame):
        super().__init__(
            master,
            bg=styles.BACKGROUND_COLOR,
            border=2,
            borderwidth=1,
            relief=tk.RAISED,
            width=200,
            height=720
        )
        self.master = master
        self.buttons = []

        self.pack(
            side=tk.LEFT,
            fill=tk.Y,
        )

    def add_button(self, button: tk.Button):
        self.buttons.append(button)
        button.pack(pady=5, padx=5, fill=tk.X)
    def remove_button(self, button: tk.Button):
        if button in self.buttons:
            self.buttons.remove(button)
            button.pack_forget()
        else:
            print("Button not found in sidebar.")
    def clear_buttons(self):
        for button in self.buttons:
            button.pack_forget()
        self.buttons.clear()
    def show_buttons(self):
        for button in self.buttons:
            button.pack(pady=5, padx=5, fill=tk.X)
    def hide_buttons(self):
        for button in self.buttons:
            button.pack_forget()