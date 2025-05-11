import tkinter as tk

from src.views.components import SidebarButton, SideBar
from src.views.pages import AddProductPage, ListProductsPage
from src.views import styles


class Home(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(
            master=master,
            bg=styles.BACKGROUND_COLOR,
        )
        self.master
        self.pages = {
            "add_product": AddProductPage,
            "list_products": None,  # Placeholder for future pages
            "search_product": None,
            "update_product": None,
            "delete_product": None,
        }

        self.create_widgets()

        self.pack(fill="both", expand=True)  # Garante que o frame ocupe a tela
    

    def create_widgets(self):

        self.create_sidebar()

    def create_sidebar(self):
        self.side_bar = SideBar(self)

        self.add_product = SidebarButton(
            self.side_bar,
            "Adicionar Produto",
            command=lambda: self.set_content(AddProductPage)
        )

        self.get_all_products = SidebarButton(
            self.side_bar,
            "Listar Produtos",
            command=lambda: self.set_content(ListProductsPage)
        )

        self.get_product_by_name = SidebarButton(
            self.side_bar,
            "Buscar Produto",
            command=lambda: print("Buscar Produto")
        )

        self.get_product_by_quantity = SidebarButton(
            self.side_bar,
            "Buscar Produto por Quantidade",
            command=lambda: print("Buscar Produto por Quantidade")
        )

        self.update_product = SidebarButton(
            self.side_bar,
            "Atualizar Produto",
            command=lambda: print("Atualizar Produto")
        )

        self.delete_product = SidebarButton(
            self.side_bar,
            "Deletar Produto",
            command=lambda: print("Deletar Produto")
        )
        

        self.side_bar.add_button(self.add_product)
        self.side_bar.add_button(self.get_all_products)
        self.side_bar.add_button(self.get_product_by_name)
        self.side_bar.add_button(self.get_product_by_quantity)
        self.side_bar.add_button(self.update_product)
        self.side_bar.add_button(self.delete_product)

    def set_content(self, content: tk.Frame = AddProductPage):

        if hasattr(self, "content"):
            self.content.destroy()

        self.content = content(self)
        self.content.pack(fill="both", expand=True)