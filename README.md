<h1 align="center"> 🤖 Analisador de Finanças com IA </h1>

## 📑 Tabela de conteúdos

- [Sobre o projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Dashboard](#layout)
- [Como executar o projeto](#como-executar-o-projeto)
  - [Pré-requisitos](#pre-requisitos)
  - [Processamento de dados](#processamento-de-dados)
  - [Rodando o dashboard](#rodando-o-dashboard)
- [Tecnologias](#tecnologias)
- [Como contribuir no projeto](#como-contribuir)
- [Autor](#autor)
- [Licença](#licenca)

---

## 💻 Sobre o projeto <a name="sobre-o-projeto"></a>

📊 O **Analisador de Finanças com IA** processa arquivos OFX, categoriza automaticamente as transações financeiras e exibe um dashboard interativo para análise dos gastos.

O objetivo é facilitar a organização financeira de forma prática e visual.

---

## ⚙️ Funcionalidades <a name="funcionalidades"></a>

- ✅ Processamento de arquivos OFX
- ✅ Categorização automática via IA
- ✅ Exportação dos dados categorizados para CSV
- ✅ Dashboard interativo para análise de despesas
- ✅ Filtros para visualizar os gastos por mês e categoria

---

## 🎨 Dashboard <a name="layout"></a>

O sistema conta com um dashboard interativo feito com **Streamlit** e gráficos gerados pelo **Plotly**.

<p align="center">
  <img alt="Screenshot do Dashboard" src="https://github.com/user-attachments/assets/1d088879-dc82-4d89-9d70-23a7686eb9cf" />
</p>

---

## 🚀 Como executar o projeto <a name="como-executar-o-projeto"></a>

### 🛠 Pré-requisitos <a name="pre-requisitos"></a>

Antes de iniciar, crie um ambiente virtual
```bash
python3 -m venv venv
```

Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

### 📥 Processamento de dados <a name="processamento-de-dados"></a>

1. Coloque seus arquivos OFX na pasta `extratos/`.
2. Acesse o site [GROQAPI](https://console.groq.com/keys) e gere sua chave de acesso aos modelos de IA.
3. Execute o processamento:
   ```bash
   python main.py
   ```
   Isso irá gerar o arquivo `finances.csv` com os dados categorizados.

### 📊 Rodando o dashboard <a name="rodando-o-dashboard"></a>

```bash
streamlit run dashboard.py
```

Acesse o dashboard pelo navegador.

---

## 🛠 Tecnologias <a name="tecnologias"></a>

O projeto foi desenvolvido com as seguintes tecnologias:

- **Python**
- **Pandas** (Manipulação de dados)
- **OFXParse** (Leitura de arquivos OFX)
- **LangChain** (IA para categorização de transações)
- Modelo utilizado: **llama-3.1-8b-instant**
- **Streamlit** (Criação do dashboard interativo)
- **Plotly** (Visualização de dados)

---

## 💪 Como contribuir no projeto <a name="como-contribuir"></a>

1. Faça um **fork** do repositório.
2. Crie uma branch: `git checkout -b minha-feature`
3. Faça suas alterações e salve com um commit: `git commit -m "feat: minha nova funcionalidade"`
4. Envie para o repositório: `git push origin minha-feature`

---

## 🦸 Autor <a name="autor"></a>

Desenvolvido por **[Rauane Lima](https://github.com/lrauane)** 🚀

---

## 📜 Licença <a name="licenca"></a>

Este projeto está sob a licença MIT - sinta-se à vontade para utilizá-lo e modificá-lo!
