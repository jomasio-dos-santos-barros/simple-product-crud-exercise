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
        self.master = master
        self.pages = {
            "add_product": AddProductPage,
            "list_products": ListProductsPage,
            "search_product": None,
            "update_product": None,
            "delete_product": None,
        }

        self.create_widgets()

        self.pack(fill="both", expand=True)
    

    def create_widgets(self):

        self.create_sidebar()

    def create_sidebar(self):
        """
        Create the sidebar with buttons to navigate between pages.
        The sidebar contains buttons for adding a product, listing products,
        searching for a product by name, searching for a product by quantity,
        updating a product, and deleting a product.
        """
        self.side_bar = SideBar(self)

        self.add_product = SidebarButton(
            self.side_bar,
            "Adicionar Produto",
            command=lambda: self.set_content(
                self.pages["add_product"]
            )
        )

        self.get_all_products = SidebarButton(
            self.side_bar,
            "Listar Produtos",
            command=lambda: self.set_content(
                self.pages["list_products"]
            )
        )

        self.get_product_by_name = SidebarButton(
            self.side_bar,
            "Buscar Produto por Nome",
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
        
        self.side_bar.add_buttons(
            [
                self.add_product,
                self.get_all_products,
                self.get_product_by_name,
                self.get_product_by_quantity,
                self.update_product,
                self.delete_product
            ]
        )

    def set_content(self, content: tk.Frame = AddProductPage):
        """
        Set the content of the main frame to the specified page.
        Args:
            content (tk.Frame): The page to display in the main frame.
        Returns:
            None
        """
        if hasattr(self, "content"):
            self.content.destroy()

        self.content = content(self)

        