import pandas as pd
from IPython.core.display_functions import display

tabela = pd.read_excel("Vendas.xlsx")
display(tabela)

faturamento_total = tabela["Valor Final"].sum()
print(f"O faturamento total da empresa foi {faturamento_total} reais.")

#faturamento por loja

faturamento_por_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
display(faturamento_por_loja)

#faturamento por produto
faturamento_produto = tabela[["ID Loja","Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
display(faturamento_produto)

#Assim, podemos observar que a bermuda lisa, presente no shopping de Iguatemi Campinas foi responsável pela maior parte do faturamento da empresa. Deve-se instruir os responsáveis para disponibilizar esse modelo em outras unidades para ver se o comportamento de vendas se mantém.