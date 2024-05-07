from os import system
from model.produto import Produto
from repo.produto import ProdutoRepo
from util.database import obter_conexao

ProdutoRepo.criar_tabela()

def mostrar_menu():
    print("CADASTRO DE PRODUTOS")
    print("--------------------")
    print("1. Inserir")
    print("2. Listar")
    print("3. Alterar")
    print("4. Excluir")
    print("5. Detalhes")
    print("6. Sair")

def obter_opcao() -> int:
    opcao = int(input("Opcao desejada: "))
    return opcao

def inserir():
    print("INSERIR PRODUTO")
    print("---------------")
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    estoque = int(input("Estoque: "))
    preco = float(input("Preço: "))
    p = Produto(None, nome, descricao, estoque, preco)
    ProdutoRepo.inserir(p)
    input("\nPressione ENTER para prosseguir...")

def listar():
    produtos = ProdutoRepo.obter_todos()
    for p in produtos:
        print(f"{p.id:02d} {p.nome}")
    input("\nPressione ENTER para prosseguir...")

def alterar():
    print("ALTERAR PRODUTO")
    print("---------------")
    id = int(input("Código: "))
    p = ProdutoRepo.obter_um(id)
    nome = input(f"Nome ({p.nome}): ")
    descricao = input(f"Descrição ({p.descricao}): ")
    estoque = int(input(f"Estoque ({p.estoque}): "))
    preco = float(input(f"Preço ({p.preco}): "))
    p = Produto(id, nome, descricao, estoque, preco)
    ProdutoRepo.alterar(p)
    input("\nPressione ENTER para prosseguir...")

def excluir():
    print("EXCLUIR PRODUTO")
    print("---------------")
    id = int(input("Código: "))
    p = ProdutoRepo.obter_um(id)
    resposta = input(f"Deseja realmente excluir o produto {p.nome}? (S/N): ")
    if resposta.upper() == "S":
        ProdutoRepo.excluir(id)
    input("\nPressione ENTER para prosseguir...")

def detalhes():
    print("DETALHAR PRODUTO")
    print("---------------")
    id = int(input("Código: "))
    p = ProdutoRepo.obter_um(id)
    print(f"Nome: {p.nome}")
    print(f"Descrição: {p.descricao}")
    print(f"Estoque: {p.estoque}")
    print(f"Preço: {p.preco}")
    input("\nPressione ENTER para prosseguir...")

while True:
    system("cls")
    mostrar_menu()
    opcao = obter_opcao()
    system("cls")
    match(opcao):
        case 1: inserir()
        case 2: listar()
        case 3: alterar()
        case 4: excluir()
        case 5: detalhes()
        case 6: break
        case _: input("Opção inválida, pressione ENTER para voltar ao menu...")

print("\nSistema de cadastro de produtos finalizado!")
