# 🤖 Assistente de Análise Financeira com IA & RAG Estruturado

Este é um projeto de um **Assistente Financeiro Inteligente** capaz de ler extratos bancários reais em formato PDF e responder a perguntas complexas sobre gastos, faturamentos e históricos de transações com total precisão matemática.

O projeto foi desenvolvido focado em boas práticas de Garantia de Qualidade (QA) e engenharia de prompt, evoluindo de uma arquitetura RAG tradicional (fatiada) para uma abordagem de Contexto Longo Estruturado.

---

## 🔍 O Caso de Teste e Evolução do Projeto (Abordagem de QA)

Durante o ciclo de testes de fumaça (smoke tests) utilizando extratos bancários reais (como os emitidos pelo Nubank), a primeira versão do sistema apresentou uma falha crítica de "falso negativo" e alucinação matemática.

### ❌ O Bug Encontrado (Arquitetura Antiga: Chunking & FAISS)
Na abordagem inicial, o extrato em PDF era quebrado linha por linha e indexado em um banco de dados vetorial (`FAISS`). 
* **Sintoma:** Ao perguntar *"Quais as saídas do dia 02 de maio?"*, a IA respondia que não havia registros ou inventava um valor incorreto.
* **Causa Raiz:** Extratos bancários possuem dados tabulares altamente estruturados. O algoritmo de busca semântica quebrava o documento de forma que a data (ex: `02 MAI`) ficava em um fragmento de texto e a transação correspondente ficava em outro. Ao buscar, os dados entravam desalinhados e fragmentados no contexto do LLM.

### ✔️ A Solução Empregada (Arquitetura Atual: Contexto Longo)
Para mitigar o erro de fragmentação e garantir 100% de acerto nas operações matemáticas e agrupamentos por instituição, a lógica de busca semântica foi substituída pelo **RAG de Contexto Longo Estruturado**. O texto do PDF passou a ser extraído mantendo a ordem cronológica e o cabeçalho original de leitura do documento, sendo injetado por inteiro no modelo `gemini-2.5-flash` com temperatura controlada (`0.1`), anulando alucinações.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.13
* **Orquestração de IA:** LangChain (`langchain-google-genai`)
* **Modelo de Linguagem:** Google Gemini 2.5 Flash
* **Extração de Dados:** PyPDF
* **Ambiente Isolado:** Python venv

---

## 🚀 Como Executar o Projeto

### 1. Clonar o Repositório
```bash
git clone [https://github.com/giovannamarq/assistente-financeiro-ia.git](https://github.com/giovannamarq/assistente-financeiro-ia.git)
cd assistente-financeiro-ia