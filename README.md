# 🧪 Tarefa: Sistema CRUD de Produtos

Implemente um sistema em Python para gerenciar um cadastro de produtos em uma pequena loja. Cada produto deve possuir os seguintes dados:

* `id`: int
* `name`: str
* `price`: float
* `quantity`: int

Os produtos devem ser armazenados em uma lista de dicionários.

## 🧩 Requisitos da Tarefa

Implemente as seguintes funções:

1. 🔹 `add_product(product_list, id, name, price, quantity)`

   * Adiciona um novo produto à lista.

2. 🔍 `find_by_id(product_list, id)`

   * Retorna o produto com o ID informado.

3. 🔍 `find_by_name(product_list, name)`

   * Retorna todos os produtos cujo nome contenha a string informada.

4. 🔍 `find_by_quantity(product_list, quantity)`

   * Retorna todos os produtos com a quantidade exata informada.

5. ✏️ `update_product(product_list, id, name=None, price=None, quantity=None)`

   * Altera nome, preço e/ou quantidade do produto com base no ID.

6. 🗑️ `delete_product(product_list, id)`

   * Remove o produto da lista com base no ID.

### 💡 Dicas

* Use uma lista para armazenar os produtos, cada um representado como um dicionário.
* Use estruturas condicionais e laços de repetição.
* Utilize boas práticas de função: funções com parâmetros e retornos claros.
* Para buscas por nome, utilize `lower` (case insensitive).
* Trate erros como ID duplicado ou produto não encontrado.

```python
# Lista que armazena os produtos
products = []

def add_product(product_list, id, name, price, quantity):
    """
    Adiciona um novo produto à lista.
    Verifica se o ID já existe.
    """
    # TODO: Implementar verificação de ID duplicado
    # TODO: Criar dicionário do produto e adicioná-lo à lista
    pass


def find_by_id(product_list, id):
    """
    Retorna o produto com o ID especificado.
    """
    # TODO: Percorrer a lista e retornar o produto com ID correspondente
    pass


def find_by_name(product_list, name):
    """
    Retorna todos os produtos cujo nome contenha a string fornecida (case insensitive).
    """
    # TODO: Usar operador "in" e comparar nomes minúsculos
    pass


def find_by_quantity(product_list, quantity):
    """
    Retorna todos os produtos com a quantidade exata fornecida.
    """
    # TODO: Percorrer a lista e retornar produtos com a quantidade exata
    pass


def update_product(product_list, id, name=None, price=None, quantity=None):
    """
    Atualiza o nome, preço ou quantidade de um produto com base no ID.
    """
    # TODO: Buscar o produto pelo ID e atualizar os campos fornecidos
    pass


def delete_product(product_list, id):
    """
    Remove o produto da lista com o ID especificado.
    """
    # TODO: Buscar o produto pelo ID e removê-lo da lista
    pass


# Exemplo de menu simples para testar as funções (opcional para os alunos)
def main():
    while True:
        print("\n--- MENU CRUD DE PRODUTOS ---")
        print("1. Adicionar produto")
        print("2. Buscar por ID")
        print("3. Buscar por nome")
        print("4. Buscar por quantidade")
        print("5. Atualizar produto")
        print("6. Deletar produto")
        print("7. Listar todos os produtos")
        print("0. Sair")

        op = input("Escolha uma opção: ")

        if op == "1":
            id = int(input("ID: "))
            name = input("Nome: ")
            price = float(input("Preço: "))
            quantity = int(input("Quantidade: "))
            add_product(products, id, name, price, quantity)

        elif op == "2":
            id = int(input("ID a buscar: "))
            print(find_by_id(products, id))

        elif op == "3":
            name = input("Nome a buscar: ")
            print(find_by_name(products, name))

        elif op == "4":
            quantity = int(input("Quantidade a buscar: "))
            print(find_by_quantity(products, quantity))

        elif op == "5":
            id = int(input("ID do produto a atualizar: "))
            name = input("Novo nome (ou Enter para manter): ")
            price_input = input("Novo preço (ou Enter): ")
            quantity_input = input("Nova quantidade (ou Enter): ")

            price = float(price_input) if price_input else None
            quantity = int(quantity_input) if quantity_input else None

            update_product(products, id, name or None, price, quantity)

        elif op == "6":
            id = int(input("ID do produto a deletar: "))
            delete_product(products, id)

        elif op == "7":
            for p in products:
                print(p)

        elif op == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

```

### 📦 Exemplo de estrutura de dados

```python
products = [
    {"id": 1, "name": "Caneta", "price": 2.5, "quantity": 100},
    {"id": 2, "name": "Caderno", "price": 15.0, "quantity": 50}
]
```

### 🎯 Objetivos de Aprendizado

* Manipular listas e dicionários
* Praticar a criação de funções reutilizáveis
* Utilizar estruturas condicionais e de repetição
* Pensamento estruturado para resolução de problemas
