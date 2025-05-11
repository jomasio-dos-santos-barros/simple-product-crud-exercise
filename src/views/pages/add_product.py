from src.views.components import Button, Input, Form

class AddProductPage(Form):
    def __init__(self, master):
        super().__init__(master, title="Adicionar Produto")
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Aqui você pode adicionar os widgets necessários para o conteúdo de adicionar produto
        self.product_name = Input(self, "Ex: Bolo de Chocolate")
        self.product_quantity = Input(self, "10")
        self.product_price = Input(self, "20")
        self.confirm = Button(
            self,
            text="Adicionar Produto",
            command=lambda: print("Produto adicionado!"),
            type="confirm",
        )
        self.cancel_button = Button(
            self,
            text="Cancelar",
            command=lambda: print("Adição de produto cancelada!"),
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