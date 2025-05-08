products = []
id_counter = 0

def add_product(
        product_list: list[dict], 
        id: int, 
        name: str, 
        price: float, 
        quantity: int
    )-> list[dict]:
    """
    Adiciona um novo produto à lista.
    Verifica se o ID já existe.

    :param product_list: Lista de produtos
    :param id: ID do produto
    :param name: Nome do produto
    :param price: Preço do produto
    :param quantity: Quantidade do produto
    :return: Lista de produtos atualizada
    """
    
    product = {
        "id": id,
        "name": name,
        "price": price,
        "quantity": quantity
    }

    for p in product_list:
        if p["id"] == id:
            print(f"Produto com ID {id} já existe.")
            return product_list
        
    product_list.append(product)
    print(f"Produto {name} adicionado com sucesso.")
    return product_list

def find_by_id(
        product_list: list[dict], 
        id: int
    ) -> dict | None:
    """
    Retorna o produto com o ID especificado.

    :param product_list: Lista de produtos
    :param id: ID do produto
    :return: Produto encontrado ou None
    """
    for p in product_list:
        if p["id"] == id:
            return p
    print(f"Produto com ID {id} não encontrado.")
    return None

def find_by_name(product_list: list[dict], name: str) -> dict | None:
    """
    Retorna todos os produtos cujo nome contenha a string fornecida (case insensitive).

    :param product_list: Lista de produtos
    :param name: Nome do produto
    :return: Produto encontrado ou None
    """
    
    for p in product_list:
        if name.lower() in p["name"].lower():
            return p
    print(f"Produto com nome {name} não encontrado.")
    return None


def find_by_quantity(product_list: list[dict], quantity: int) -> dict | None:
    """
    Retorna todos os produtos com a quantidade exata fornecida.

    :param product_list: Lista de produtos
    :param quantity: Quantidade do produto
    :return: Produto encontrado ou None
    """

    for p in product_list:
        if p["quantity"] == quantity:
            return p
    print(f"Produto com quantidade {quantity} não encontrado.")
    return None


def update_product(
        product_list: list[dict], 
        id: int, 
        name: str | None = None, 
        price: float | None = None, 
        quantity: int | None = None
    ) -> list[dict]:
    """
    Atualiza o nome, preço ou quantidade de um produto com base no ID.
    Se o ID não for encontrado, imprime uma mensagem de erro.

    :param product_list: Lista de produtos
    :param id: ID do produto
    :param name: Novo nome do produto
    :param price: Novo preço do produto
    :param quantity: Nova quantidade do produto
    :return: Lista de produtos atualizada
    """
    for p in product_list:
        if p["id"] == id:
            if name is not None:
                p["name"] = name
            if price is not None:
                p["price"] = price
            if quantity is not None:
                p["quantity"] = quantity
            print(f"Produto com ID {id} atualizado com sucesso.")
    
    return product_list


def delete_product(
        product_list: list[dict], 
        id: int
    ) -> list[dict]:
    """
    Remove o produto da lista com o ID especificado.

    :param product_list: Lista de produtos
    :param id: ID do produto
    """
    for p in product_list:
        if p["id"] == id:
            product_list.remove(p)
            print(f"Produto com ID {id} removido com sucesso.")
            return product_list
    print(f"Produto com ID {id} não encontrado.")
    return product_list


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

        global id_counter

        if op == "1":
            id_counter += 1
            id = id_counter
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
