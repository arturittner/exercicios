# c) Implemente um sistema para cadastrar produtos contendo os seguintes
# dados: nome do produto, marca, valor, quantidade em estoque. As
# funcionalidades que esse sistema deverá ter são:
# ● Cadastrar produtos
# ● Selecionar produtos
# ● Alterar produtos
# ● Excluir produtos
# ● Pesquisar produtos através do nome
# Algumas regras para esse sistema:
# ● Não pode haver produtos com o mesmo nome
# ● Não poderão ser cadastrados com valor zero ou negativos
# ● Quando cadastrado um produto, a quantidade em estoque precisa ser
# de pelo menos um.


lista_nome = []
lista_marca = []
lista_valor = []
lista_estoque = []
escolha_user = 0

produtos = [lista_nome, lista_marca, lista_valor, lista_estoque]

def Cadastrar_Produto():
    print("Insira os dados do produto para cadastro")
    nome_produto = input("Nome: ")
    marca_produto = input("Marca: ")
    valor_produto = float(input(("Valor: ")))
    estoque_produto = int(input(("Quantidade em estoque: ")))
    lista_nome.append(nome_produto)
    lista_marca.append(marca_produto)
    lista_valor.append(round(valor_produto, 2))
    lista_estoque.append(estoque_produto)

def Selecionar_Produto():
    for index in range(0, len(lista_nome), 1):
        print(index, "-", lista_nome[index])
    escolha_user = int(input("Escolha o código (númerico, à esquerda) do produto que você deseja selecionar"))
    print(lista_nome[escolha_user], lista_marca[escolha_user], lista_valor[escolha_user], lista_estoque[escolha_user])

def Alterar_Produto():
    for index in range(0, len(lista_nome), 1):
        print(index, "-", lista_nome[index], "-", lista_marca[index], "-", lista_valor[index], "-", lista_estoque[index])
    escolha_alteracao = int(input("Escolha pelo índice os dados de qual produto você deseja alterar: "))
    info_nome = input("Escolha o nome que você deseja inserir: ")
    lista_nome[escolha_alteracao] = info_nome
    info_marca = input("Escolha a marca que deseja inserir: ")
    lista_marca[escolha_alteracao] = info_marca
    info_valor = float(input("Escolha o valor que deseja inserir: "))
    lista_valor[escolha_alteracao] = info_valor
    info_estoque = int(input("Escolha a cidade que deseja inserir: "))
    lista_estoque[escolha_alteracao] = info_estoque

def Excluir_Produto():
    for index in range(0, len(lista_nome), 1):
        print(index, "-", lista_nome[index])
    escolha_remocao = int(input("Escolha a linha que você deseja remover: "))
    lista_nome.pop(escolha_remocao)
    lista_marca.pop(escolha_remocao)
    lista_valor.pop(escolha_remocao)
    lista_estoque.pop(escolha_remocao)

def Pesquisa():
    user_choice = int(input("Digite qual informação você deseja buscar você deseja buscar, visto que\n"
              "[1] Nome\n"
              "[2] Marca\n"
              "[3] Valor\n"
              "[4] Estoque\n"))
    if user_choice == 1:
        nome_busca = input("Qual produto você deseja buscar? ")
        for index in range(0, len(lista_nome), 1):
            if nome_busca == lista_nome[index]:
                print(lista_nome[index], lista_marca[index], lista_valor[index], lista_estoque[index])
            pass
    elif user_choice == 2:
        marca_busca = input("Qual marca você deseja buscar? ")
        for index in range(0, len(lista_marca), 1):
            if marca_busca == lista_marca[index]:
                print(lista_nome[index], lista_marca[index], lista_valor[index], lista_estoque[index])
            pass
    elif user_choice == 3:
        valor_busca = float(input("Qual o valor específico que você está buscando? "))
        for index in range(0, len(lista_valor), 1):
            if valor_busca == lista_valor[index]:
                print(lista_nome[index], lista_marca[index], lista_valor[index], lista_estoque[index])
            pass
    elif user_choice == 4:
        estoque_busca = int(input("Qual a quantidade específica de estoque que você está buscando? "))
        for index in range(0, len(lista_estoque), 1):
            if estoque_busca == lista_estoque[index]:
                print(lista_nome[index], lista_marca[index], lista_valor[index], lista_estoque[index])
            pass
    else: Pesquisa()

resposta = 0
while (resposta != 6):
    resposta = int(input("Olá, o que você deseja fazer na lista? \n"
                             "[1] Cadastrar produto\n"
                             "[2] Alterar produto\n"
                             "[3] Remover produto\n"
                             "[4] Selecionar produto\n"
                             "[5] Pesquisar informação\n"
                             "[6] Finalizar\n"
                             "Digite aqui: "))
    if resposta == 1:
            Cadastrar_Produto()
    elif resposta == 2:
            Alterar_Produto()
    elif resposta == 3:
            Excluir_Produto()
    elif resposta == 4:
            Selecionar_Produto()
    elif resposta == 5:
            Pesquisa()
    pass