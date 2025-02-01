import ofxparse
import pandas as pd
import os
from unidecode import unidecode

def process_ofx_files(directory="extratos"):
    df = pd.DataFrame()

    for extrato in os.listdir(directory):
        with open(f'{directory}/{extrato}', encoding='ISO-8859-1') as ofx_file:
            ofx = ofxparse.OfxParser.parse(ofx_file)
        
        transactions_data = []
        for account in ofx.accounts:
            for transaction in account.statement.transactions:
                transactions_data.append({
                    "Data": transaction.date,
                    "Valor": transaction.amount,
                    "Descrição": unidecode(transaction.memo) if transaction.memo else "",  # Remover acentos
                    "ID": transaction.id,
                })
        
        # Converte as transações para um DataFrame
        df_temp = pd.DataFrame(transactions_data)
        if not df_temp.empty:
            df_temp["Valor"] = df_temp["Valor"].astype(float)
            df_temp["Data"] = df_temp["Data"].apply(lambda x: x.date())
            df = pd.concat([df, df_temp], ignore_index=True)

    # Define "ID" como índice
    if not df.empty:
        df = df.set_index("ID")
    return df
