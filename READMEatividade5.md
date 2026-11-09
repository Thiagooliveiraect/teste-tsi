# Assistente Inteligente de Recuperação de Informações (RAG)

Projeto acadêmico que demonstra um sistema de recuperação de informações com **LangChain**, **FAISS**, **embeddings do Hugging Face** e **Ollama**.

## 1. Objetivo

O sistema recebe uma pergunta, transforma a pergunta em embedding, procura os trechos semanticamente mais próximos no banco vetorial FAISS e utiliza um modelo de linguagem local para elaborar uma resposta com base no conteúdo recuperado.

## 2. Tecnologias

- Python
- LangChain e RetrievalQA
- FAISS (banco/índice vetorial)
- Hugging Face Sentence Transformers (`all-MiniLM-L6-v2`) para embeddings
- Ollama (`llama3.2`) para geração local de respostas

Não é necessária uma chave de API paga.

## 3. Estrutura do projeto

```text
projeto_vectordb_faiss/
├── app.py
├── requirements.txt
├── README.md
├── documentos/
│   └── base_conhecimento.txt
└── faiss_index/          # criado automaticamente na primeira execução
```

## 4. Requisitos

- Python 3.10 ou superior (recomendado).
- Conexão com a internet na primeira execução para instalar pacotes e baixar o modelo de embeddings.
- Ollama instalado e em execução.
- Memória e espaço em disco suficientes para os modelos locais.

## 5. Instalação e execução

### Windows

1. Instale o Python: https://www.python.org/downloads/
2. Instale o Ollama: https://ollama.com/
3. Abra o PowerShell na pasta do projeto.
4. (Opcional, recomendado) Crie um ambiente virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

5. Instale as dependências:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

6. Baixe o modelo de linguagem:

```powershell
ollama pull llama3.2
```

7. Execute o sistema:

```powershell
python app.py
```

Na primeira execução, o programa lê os arquivos `.txt`, divide os documentos em chunks, gera embeddings e cria o índice FAISS. O índice é salvo na pasta `faiss_index` para reutilização.

> Se o PowerShell bloquear a ativação do ambiente virtual, é possível executar `\.venv\Scripts\python.exe -m pip install -r requirements.txt` e depois `\.venv\Scripts\python.exe app.py`, sem ativar o ambiente.

### Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
ollama pull llama3.2
python app.py
```

## 6. Exemplos de perguntas

Com a base de conhecimento fornecida, experimente:

1. O que é Inteligência Artificial?
2. Qual é a diferença entre aprendizado supervisionado e não supervisionado?
3. Quais são as camadas de uma rede neural?
4. O que é backpropagation?
5. Para que servem os embeddings?
6. Como funciona o FAISS?
7. O que significa RAG?
8. Qual é a função do RetrievalQA?

As respostas podem variar conforme o modelo local, mas devem ser fundamentadas nos trechos recuperados da base.

## 7. Como o pipeline funciona

1. **Carregamento:** os arquivos de texto da pasta `documentos/` são lidos.
2. **Chunking:** `RecursiveCharacterTextSplitter` divide os documentos em partes de 700 caracteres, com sobreposição de 100.
3. **Embeddings:** `HuggingFaceEmbeddings` converte cada chunk em um vetor numérico.
4. **Indexação:** `FAISS.from_documents` cria o índice vetorial e `save_local` o armazena.
5. **Recuperação:** o retriever procura os três chunks mais semelhantes à pergunta.
6. **Geração:** `RetrievalQA` envia a pergunta e os trechos ao Ollama, que gera a resposta.
7. **Fontes:** o programa exibe os arquivos dos documentos recuperados.

## 8. Personalização

Para adicionar conhecimento, crie ou coloque outros arquivos `.txt` dentro de `documentos/`. Se já existir a pasta `faiss_index`, apague-a antes de executar novamente para reconstruir o índice com os novos textos.

Para alterar o modelo Ollama, modifique `MODELO_OLLAMA` em `app.py` e baixe o modelo correspondente com `ollama pull nome-do-modelo`.

## 9. Observações técnicas

- O código usa a integração atual do LangChain com `langchain_classic.chains.RetrievalQA`. Em versões recentes, RetrievalQA é mantido por compatibilidade e pode emitir aviso de descontinuação; foi utilizado porque é o componente solicitado na atividade.
- `allow_dangerous_deserialization=True` é usado ao carregar o índice FAISS salvo localmente. Só carregue índices que você mesmo criou ou cuja origem seja confiável.
- O modelo de embeddings é baixado na primeira execução e roda em CPU neste exemplo.
- O Ollama precisa estar instalado e em execução para gerar respostas.
- O sistema é uma demonstração acadêmica; não deve ser usado para decisões críticas sem validação.

## 10. Referências

- LangChain: https://python.langchain.com/
- FAISS: https://github.com/facebookresearch/faiss
- Hugging Face: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
- Ollama: https://ollama.com/
