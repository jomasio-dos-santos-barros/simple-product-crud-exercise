import tkinter as tk

from src.views import styles

class SideBar(tk.Frame):
    def __init__(self, master: tk.Frame):
        super().__init__(
            master,
            bg=styles.BACKGROUND_COLOR,
            border=styles.BORDER_THICKNESS,
            borderwidth=styles.BORDER_WIDTH,
            relief=tk.RAISED,
            width=styles.SIDEBAR_WIDTH
        )
        self.master = master
        self.buttons = []

        self.pack(
            side=tk.LEFT,
            fill=tk.Y,
        )

    def add_button(self, button: tk.Button):
        """
        Add a button to the sidebar.
        
        Args:
            button (tk.Button): The button to add.
        
        Returns:
            None
        """
        self.buttons.append(button)
        button.pack(pady=5, padx=5, fill=tk.X)
        
    def add_buttons(self, buttons: list[tk.Button]):
        """
        Add multiple buttons to the sidebar.
        
        Args:
            buttons (list[tk.Button]): A list of buttons to add.
        
        Returns:
            None
        """
        for button in buttons:
            self.add_button(button)
        
    def remove_button(self, button: tk.Button):
        """
        Remove a button from the sidebar.
        Args:
            button (tk.Button): The button to remove.
        Returns:
            None
        """
        if button in self.buttons:
            self.buttons.remove(button)
            button.destroy()
        else:
            print("Button not found in sidebar.")
    def clear_buttons(self):
        """
        Clear all buttons from the sidebar.
        """
        for button in self.buttons:
            button.destroy()
    def show_buttons(self):
        """
        Show all buttons in the sidebar.
        This method is used to display the buttons after they have been hidden.
        """
        for button in self.buttons:
            button.pack(pady=5, padx=5, fill=tk.X)
    def hide_buttons(self):
        """
        Hide all buttons in the sidebar.
        """
        for button in self.buttons:
            button.pack_forget()