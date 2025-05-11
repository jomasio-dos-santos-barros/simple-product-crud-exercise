import tkinter as tk

from src.views import Home

root = tk.Tk()

root.title("CRUD System")
root.geometry("1280x720+350+100")

home = Home(root)

home.pack()

root.mainloop()