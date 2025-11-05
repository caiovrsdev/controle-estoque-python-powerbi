import pandas as pd
from datetime import datetime

class Estoque:
    def __init__(self):
        self.produtos = pd.DataFrame(columns=["ID", "Produto", "Categoria", "Quantidade", "Preço_Unitário", "Data_Atualização"])

    def adicionar_produto(self, id_produto, nome, categoria, quantidade, preco):
        novo_produto = pd.DataFrame([{
            "ID": id_produto,
            "Produto": nome,
            "Categoria": categoria,
            "Quantidade": quantidade,
            "Preço_Unitário": preco,
            "Data_Atualização": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }])
        self.produtos = pd.concat([self.produtos, novo_produto], ignore_index=True)
        print(f"✅ Produto '{nome}' adicionado ao estoque.")

    def atualizar_quantidade(self, id_produto, nova_qtd):
        if id_produto in self.produtos["ID"].values:
            self.produtos.loc[self.produtos["ID"] == id_produto, ["Quantidade", "Data_Atualização"]] = [nova_qtd, datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
            print(f"🔄 Quantidade do produto ID {id_produto} atualizada para {nova_qtd}.")
        else:
            print("⚠️ Produto não encontrado.")

    def remover_produto(self, id_produto):
        self.produtos = self.produtos[self.produtos["ID"] != id_produto]
        print(f"🗑️ Produto ID {id_produto} removido do estoque.")

    def salvar_csv(self, nome_arquivo="estoque.csv"):
        self.produtos.to_csv(nome_arquivo, index=False)
        print(f"💾 Dados salvos em {nome_arquivo}")

# Exemplo de uso 
if __name__ == "__main__":
    estoque = Estoque()
    estoque.adicionar_produto(1, "Teclado Mecânico", "Periféricos", 25, 350.00)
    estoque.adicionar_produto(2, "Mouse Gamer", "Periféricos", 40, 150.00)
    estoque.adicionar_produto(3, "Monitor 24''", "Monitores", 10, 900.00)

    estoque.atualizar_quantidade(2, 35)
    estoque.remover_produto(1)

    estoque.salvar_csv()
