import tkinter as tk
from tkinter import ttk

from src.controllers import ProductController
from src.schemas.product import ProductResponse
from src.views import styles
from src.views.components import MainContent

class ListProductsPage(MainContent):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.controller = ProductController()

        self.create_widgets()


    def create_widgets(self):
        """
        Método para criar os widgets da página de listagem de produtos.
        """
        self.title = tk.Label(
            self,
            text="Lista de Produtos",
            font=styles.TITLE_FONT,
            bg=styles.BACKGROUND_COLOR,
            fg=styles.TEXT_COLOR_DARK,
        )
        self.title.pack(pady=20)

    
        self.product_table = ttk.Treeview(
            self,
            columns=("name", "price", "quantity", "created_at", "updated_at"),
            show="headings",
            height=20,
        )
        self.product_table.pack(pady=20, padx=20, fill="both", expand=True)

        # Configura os cabeçalhos das colunas
        self.product_table.heading("name", text="Nome")
        self.product_table.heading("price", text="Preço")
        self.product_table.heading("quantity", text="Quantidade")
        self.product_table.heading("created_at", text="Criado em")
        self.product_table.heading("updated_at", text="Atualizado em")

        # Configura o tamanho das colunas
        self.product_table.column("name", width=200, anchor="w")
        self.product_table.column("price", width=100, anchor="center")
        self.product_table.column("quantity", width=100, anchor="center")
        self.product_table.column("created_at", width=150, anchor="center")
        self.product_table.column("updated_at", width=150, anchor="center")
        # Adiciona uma barra de rolagem
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.product_table.yview)
        self.product_table.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        # Configura a tabela para preencher o espaço disponível
        self.product_table.pack(fill="both", expand=True)
        # Adiciona um botão para atualizar a lista de produtos
        self.refresh_button = tk.Button(
            self,
            text="Atualizar Lista",
            command=self.update_product_list,
            bg=styles.BACKGROUND_COLOR,
            fg=styles.TEXT_COLOR_DARK,
            font=styles.BUTTON_FONT,
        )
        self.refresh_button.pack(pady=10)


        # Adiciona dados de exemplo
        self.get_product_list()

    def get_product_list(self):
        """
        Insere dados de exemplo na tabela.
        """
        products = self.controller.get_products()

        for product in products:
            self.product_table.insert(
                "", 
                tk.END, 
                iid=product.id,
                values=self.map_product_to_row(product)
            )
        
    def update_product_list(self):
        """
        Atualiza a lista de produtos na tabela.
        """
        # Limpa a tabela
        for item in self.product_table.get_children():
            self.product_table.delete(item)
        
        # Obtém todos os produtos do banco de dados
        products = self.controller.get_products()
        
        # Adiciona os produtos à tabela
        for product in products:
            self.product_table.insert(
                "", 
                tk.END, 
                iid=product.id,
                values=self.map_product_to_row(product)
            )


    def map_product_to_row(self, product: ProductResponse):
        """
        Mapeia os produtos para as linhas da tabela.
        """
        return (
            product.name,
            product.price,
            product.quantity,
            product.created_at.strftime("%Y-%m-%d %H:%M"),
            product.updated_at.strftime("%Y-%m-%d %H:%M"),
        )
    
    def get_selected_product_id(self):
        """
        Obtém o ID do produto selecionado na tabela.
        """
        selected_item = self.product_table.selection()
        print(selected_item)
        if selected_item:
            return selected_item[0]  # O iid é o ID do produto
        return None