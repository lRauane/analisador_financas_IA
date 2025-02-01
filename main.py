from data_processing import process_ofx_files
from model import categorize_transactions

# Processar arquivos OFX
df = process_ofx_files()

# Categorizar transações
df["Categoria"] = categorize_transactions(df["Descrição"].tolist())

df.to_csv("finances.csv", index=False)
print("Dados processados e salvos em 'finances.csv'")