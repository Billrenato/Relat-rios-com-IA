# 🧠 Sistema de Relatórios com IA usando Django

Este projeto é uma aplicação web desenvolvida com Django e Python 3.12 que permite aos usuários gerar relatórios de forma inteligente, utilizando **perguntas em linguagem natural**.<br>
Através da integração com um modelo de linguagem (como o GPT-4), o sistema interpreta as perguntas do usuário, converte em SQL, executa a consulta e retorna os resultados em forma de tabela ou gráficos.

---

## 🚀 Funcionalidades

- 📝 Entrada de perguntas em linguagem natural
- 🤖 Tradução automática da pergunta para SQL via IA
- 🗃️ Consulta ao banco de dados relacional (SQLite ou PostgreSQL)
- 📊 Exibição dos resultados em tabela HTML e gráficos
- 📁 Possibilidade de exportar relatórios (PDF, Excel etc.)
- 🔐 Autenticação de usuário com Django

---

## 🧰 Tecnologias Utilizadas

### 🔙 Backend
- [Python 3.12](https://www.python.org/)
- [Django 4.x](https://www.djangoproject.com/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib / Plotly](https://matplotlib.org/), para visualização de dados

### 🧠 Inteligência Artificial
- [OpenAI API](https://platform.openai.com/) – Para interpretação de linguagem natural (GPT-3.5 / GPT-4)
- ou [Hugging Face Transformers](https://huggingface.co/models) – Para modelos locais de Text-to-SQL

### 💾 Banco de Dados
- SQLite (desenvolvimento)
- PostgreSQL (produção)

### 🌐 Frontend
- Django Templates
- Bootstrap (para layout responsivo)
- HTML + JavaScript


