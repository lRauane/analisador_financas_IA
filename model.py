from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from dotenv import load_dotenv, find_dotenv
import time

_ = load_dotenv(find_dotenv())

template = """
Você é um analista de dados, trabalhando em um projeto de limpeza de dados.
Seu trabalho é escolher uma categoria adequada para cada lançamento financeiro
que vou te enviar.

Todos são transações financeiras de uma pessoa física.

Escolha uma dentre as seguintes categorias:
- Alimentação
- Receitas
- Saúde
- Mercado
- Saúde
- Educação
- Compras
- Transporte
- Investimento
- Transferências para terceiros
- Telefone
- Moradia

Escola a categoria deste item:
{text}

Responda apenas com a categoria.
"""


def categorize_transactions(descriptions):
    prompt = PromptTemplate.from_template(template=template)
    chat = ChatGroq(model="llama-3.1-8b-instant")
    chain = prompt | chat | StrOutputParser()

    categories = []
    for transaction in descriptions:
        success = False
        while not success:
            try:
                categories.append(chain.invoke(transaction))
                success = True
            except groq.InternalServerError as e:
                print(f"Erro: {e}. Tentando novamente em 5 segundos...")
                time.sleep(5)
    return categories
