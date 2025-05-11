from tkinter import messagebox

from src.controllers import ProductController
from src.schemas import ProductRequest
from src.views.components import Button, Input, Form

class AddProductPage(Form):
    def __init__(self, master):
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
            exit()

        try:
            product_quantity = int(product_quantity)
        except:
            messagebox.showerror(
                "Erro no cadastro",
                "Quantidade deve ser um número inteiro."
            )
            exit()

        try:
            product_price = float(product_price)
        except:
            messagebox.showerror(
                "Erro no cadastro",
                "Preço deve ser um número decimal."
            )
            exit()

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
        # Aqui você pode adicionar os widgets necessários para o conteúdo de adicionar produto
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