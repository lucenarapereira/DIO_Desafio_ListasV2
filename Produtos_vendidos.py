def produto_mais_vendido(entrada):
    # Converte a entrada em uma lista de strings, removendo espaços extras
    produtos = [produto.strip() for produto in entrada.split(',')]
    
    # Dicionário para contar a frequência de cada produto
    contagem = {}
    
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1

    # Encontrar o produto mais vendido
    max_produto = None
    max_count = 0

    for produto, count in contagem.items():
        if count > max_count:
            max_count = count
            max_produto = produto

    return max_produto

# Exemplo de uso
entrada = input("Digite a lista de produtos vendidos, separados por vírgula: ")
print(produto_mais_vendido(entrada))
