from model.produto import Produto
from repo.produto import ProdutoRepo
from util.database import obter_conexao

ProdutoRepo.criar_tabela()

# p = Produto(2, "Notebook", "Smartphone Motorola E72", 25, 1800)
# ProdutoRepo.inserir(p)
# ProdutoRepo.alterar(p)
ProdutoRepo.excluir(2)

produtos = ProdutoRepo.obter_todos()
for p in produtos:
    print(f"Código: {p.id}")
    print(f"Nome: {p.nome}")
    print(f"Preço: {p.preco}\n")

produto = ProdutoRepo.obter_um(1)
print(f"{produto.nome}, {produto.descricao}, {produto.preco:.2f}, {produto.estoque}")

print(f"Quantidade de Produtos: {ProdutoRepo.quantidade()}.")