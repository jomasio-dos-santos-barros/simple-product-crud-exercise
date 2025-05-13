import tkinter as tk
from tkinter import messagebox

from src.controllers import ProductController
from src.schemas import ProductRequest
from src.views.components import Button, Input, Form

class AddProductPage(Form):
    """
    Class representing the Add Product page.
    This class inherits from the Form class and is responsible for
    creating the widgets and handling the logic for adding a product.
    It contains methods for adding a product, canceling the addition,
    creating the widgets, and cleaning the input fields.
    Attributes:
        master (tk.Tk): The main application window.
        controller (ProductController): The controller for handling product operations.
        product_name (Input): Input field for the product name.
        product_quantity (Input): Input field for the product quantity.
        product_price (Input): Input field for the product price.
        confirm (Button): Button to confirm the addition of the product.
        cancel_button (Button): Button to cancel the addition of the product.
    Methods:
        add_product(event=None): Method to add a product.
        cancel_product(event=None): Method to cancel the addition of a product.
        create_widgets(): Method to create the widgets for the page.
        clean_widgets(): Method to clean the input fields.
    """
    def __init__(self, master: tk.Frame):
        super().__init__(master, title="Adicionar Produto")
        self.master = master
        self.controller = ProductController()
        self.create_widgets()

    def add_product(self, event=None):
        """
        Método para adicionar um produto.
        Este método deve ser chamado quando o botão de confirmação for pressionado.
        """
        product_name = self.product_name.get()
        product_quantity = self.product_quantity.get()
        product_price = self.product_price.get()

        if not product_name or not product_quantity or not product_price:
            messagebox.showerror(
                "Erro no cadastro",
                "Preencha todos os campos obrigatórios."
            )
            return None

        try:
            product_quantity = int(product_quantity)
        except:
            messagebox.showerror(
                "Erro no cadastro",
                "Quantidade deve ser um número inteiro."
            )
            return None

        try:
            product_price = float(product_price)
        except:
            messagebox.showerror(
                "Erro no cadastro",
                "Preço deve ser um número decimal."
            )
            return None

        request = ProductRequest(
            name=product_name,
            quantity=product_quantity,
            price=product_price,
        )

        response = self.controller.add_product(request)

        messagebox.showinfo(
            "Produto adicionado com sucesso",
            f"Produto {response.name} adicionado com sucesso!"
        )
        self.clean_widgets()

    def cancel_product(self, event=None):
        """
        Método para cancelar a adição de um produto.
        Este método deve ser chamado quando o botão de cancelamento for pressionado.
        """
        self.clean_widgets()

        messagebox.showinfo(
            "Cancelamento",
            "Adição de produto cancelada com sucesso!"
        )

    def create_widgets(self):
        """
        Crate the widgets for the Add Product page.
        """
        self.product_name = Input(self, "Ex: Bolo de Chocolate")
        self.product_quantity = Input(self, "10")
        self.product_price = Input(self, "20")
        self.confirm = Button(
            self,
            text="Adicionar Produto",
            command=self.add_product,
            type="confirm",
        )
        self.cancel_button = Button(
            self,
            text="Cancelar",
            command=self.cancel_product,
            type="cancel",
        )

        self.add_input(self.product_name, "Nome do Produto")
        self.add_input(self.product_quantity, "Quantidade do Produto")
        self.add_input(self.product_price, "Preço do Produto (R$)")

        self.add_buttons(
            [self.cancel_button, self.confirm]
        )

        self.pack(
            fill="both", expand=True
        )

    def clean_widgets(self):
        """
        Método para limpar os widgets da página.
        Este método deve ser chamado quando a página for fechada ou limpa.
        """
        self.product_name.delete(0, "end")
        self.product_quantity.delete(0, "end")
        self.product_price.delete(0, "end")