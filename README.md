# api-validacao-genero
API em FastAPI para validação automatizada de gênero a partir de nomes, utilizando modelos de Machine Learning treinados com dados do IBGE. Gera relatórios em Excel com campos validados, status de correção e probabilidade de classificação


# 🧠 API de Validação de Gênero — FastAPI

Este projeto implementa uma API simples para **validação automática de gênero** com base no **primeiro nome**.  
A API recebe um arquivo `.csv` ou `.xlsx` contendo colunas como:

```
Nome, Data de Nascimento, CPF, Sexo
```

E retorna um arquivo Excel com colunas adicionais:
```
Sexo Validado | Status
```

---

📊 Fonte de Dados e Treinamento do Modelo

O modelo utilizado nesta API foi treinado a partir de uma planilha pública disponibilizada em:
```
🔗 https://brasil.io/dataset/genero-nomes/nomes/
```
Esta base contém a classificação de gênero de nomes brasileiros, elaborada com dados do Censo Demográfico de 2010 do IBGE (Instituto Brasileiro de Geografia e Estatística).
O conjunto de dados foi liberado por Álvaro Justen através do projeto Brasil.io
, e está disponível sob a licença Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).

Os dados foram utilizados exclusivamente para fins de pesquisa e desenvolvimento de modelo preditivo, com o objetivo de treinar um classificador de nomes capaz de inferir o provável gênero (Masculino, Feminino ou Unissex) a partir do primeiro nome.

## ⚙️ Requisitos

- **Python 3.11.9**
- Sistema operacional Windows, Linux ou macOS

---

## 🐍 2️⃣ Criar o ambiente virtual

```bash
python -m venv .venv
```

---

## 🚀 3️⃣ Ativar o ambiente virtual

### 🔹 Windows (PowerShell)
```bash
.venv\Scripts\Activate.ps1
```

### 🔹 Windows (CMD)
```bash
.venv\Scripts\activate.bat
```

### 🔹 Linux / macOS
```bash
source .venv/bin/activate
```

> Quando ativado corretamente, o terminal mostrará algo como:
> ```
> (.venv) PS C:\3it\api-validacao-dados-ia>
> ```

---

## 📦 4️⃣ Instalar as dependências

```bash
pip install -r requirements.txt
```

> Isso instalará o FastAPI, Uvicorn, Pandas, Joblib e todas as demais bibliotecas necessárias para rodar a aplicação.

---

## ⚡ 5️⃣ Rodar o servidor

```bash
uvicorn main:app --reload
```

Se tudo estiver certo, você verá:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

---

## 🌐 6️⃣ Acessar a interface interativa

Abra o navegador e vá para:

👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 7️⃣ Testar o endpoint `/validar`

1. Clique em **POST /validar**  
2. Clique em **Try it out**
3. No campo **arquivo**, selecione sua tabela `.csv` ou `.xlsx`  
4. Clique em **Execute**
5. Aguarde a resposta

Abaixo aparecerá:

```
Response body
Download file
```

Clique em **Download file** para baixar o arquivo Excel com os resultados da validação.

---

## 📁 8️⃣ Exemplo de tabela de entrada

```csv
Nome,Data de Nascimento,CPF,Sexo
Maria Clara Souza,1995-03-10,12345678900,F
João Pedro Silva,1990-07-22,98765432100,M
Alex Santana,1988-11-05,11122233344,M
```

---

## ✅ 9️⃣ Estrutura resumida do projeto

```
api-validacao-dados-ia/
│
├── main.py
├── requirements.txt
├── infra/
│   └── path_models.py
├── api/
│   └── reconhecimento_genero/
│       ├── reconhecimento_genero_router.py
│       ├── reconhecimento_genero_service.py
│       ├── reconhecimento_genero_model.py
│       └── status_enum.py
└── models/
|   └── genero_model/
|       └── modelo_genero.pkl
```

---

## 💬 Status Codes

| Código | Descrição |
|--------|------------|
| 200 | Sucesso — retorna arquivo Excel validado |
| 400 | Erro no processamento (arquivo inválido ou modelo ausente) |
| 500 | Erro interno do servidor |

---

## 🧹 Dica final

Para garantir um ambiente limpo, sempre ative o ambiente virtual antes de rodar os comandos:

```bash
.venv\Scripts\activate
```

E para sair do ambiente virtual:

```bash
deactivate
```

---

💡 **Autor:** Lazaro Natanael da Silva  
📚 **Tecnologias:** FastAPI, Pandas, Scikit-learn, Joblib  
