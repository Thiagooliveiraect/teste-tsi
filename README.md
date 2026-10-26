# Geração de Embeddings com Ollama e Python

## 1. Objetivo

Este projeto demonstra como transformar um texto simples em um vetor numérico (*embedding*) usando o Ollama executado localmente e Python.

Embeddings são representações numéricas de textos que podem ser usados em aplicações como busca semântica e comparação de similaridade.

## 2. Tecnologias

- Python 3
- Ollama
- Modelo `nomic-embed-text`
- Biblioteca Python `ollama`

## 3. Arquivos do projeto

```text
atividade-ollama-embeddings/
├── embeddings.py
├── requirements.txt
└── README.md
```

## 4. Pré-requisitos e instalação

1. Instale o Ollama pelo site oficial: https://ollama.com/download
2. Instale Python 3, caso ainda não esteja instalado: https://www.python.org/downloads/
3. Abra o PowerShell ou terminal.
4. Baixe o modelo de embeddings:

```powershell
ollama pull nomic-embed-text
```

Confira se o modelo aparece na lista:

```powershell
ollama list
```

O Ollama normalmente inicia o serviço local automaticamente após a instalação. Se não estiver em execução, abra o aplicativo Ollama. Como alternativa, execute `ollama serve` em um terminal; se a porta já estiver ocupada, o serviço provavelmente já está ativo.

## 5. Instalar a dependência Python

Na pasta do projeto, execute:

```powershell
python -m pip install -r requirements.txt
```

Se o comando `python` não estiver disponível no Windows, tente:

```powershell
py -m pip install -r requirements.txt
```

## 6. Executar

Na pasta onde está `embeddings.py`, execute:

```powershell
python embeddings.py
```

Ou, no Windows:

```powershell
py embeddings.py
```

O script envia a frase `A inteligência artificial pode auxiliar no aprendizado.` ao modelo local e apresenta a quantidade de dimensões, os dez primeiros valores e o vetor completo.

## 7. Saída esperada

A saída deve conter mensagens semelhantes a estas (os valores são produzidos na execução e não devem ser copiados como resultados reais):

```text
ATIVIDADE: GERAÇÃO DE EMBEDDINGS COM OLLAMA
Modelo: nomic-embed-text
Texto de entrada: A inteligência artificial pode auxiliar no aprendizado.

SUCESSO: embedding gerado!
Quantidade de dimensões: [valor calculado]
Primeiros 10 valores:
  Dimensão 1: [valor numérico]
  ...
Vetor completo:
[lista de valores numéricos]
Atividade concluída com sucesso.
```

O número de dimensões e os valores exatos são apresentados pelo próprio modelo durante a execução.

## 8. Como funciona

- `ollama.embed()` solicita ao serviço local a geração do embedding.
- `resposta["embeddings"][0]` acessa o vetor correspondente ao texto.
- `len(vetor)` informa a quantidade de dimensões.
- `vetor[:10]` seleciona os dez primeiros valores.

A API local padrão do Ollama fica disponível em `http://localhost:11434`. A documentação oficial de embeddings está em https://docs.ollama.com/capabilities/embeddings.

## 9. Demonstração em vídeo

Para gravar um vídeo de até três minutos:

1. Mostre `ollama list` no terminal, com o modelo instalado.
2. Mostre que o serviço responde em `http://localhost:11434` ou execute `ollama serve` se necessário.
3. Execute `python embeddings.py`.
4. Mostre a quantidade de dimensões e alguns valores do vetor.
5. Abra o repositório público no GitHub para mostrar os arquivos.

O vídeo precisa ser gravado pelo aluno em seu próprio computador, pois depende da instalação e execução locais do Ollama.

## 10. Publicação no GitHub

Crie um repositório público chamado `atividade-ollama-embeddings` no GitHub e envie os três arquivos deste projeto. Depois, copie o endereço público do repositório para a entrega da atividade.

GitHub: https://github.com/

## 11. Autor

Projeto acadêmico desenvolvido para a atividade de geração local de embeddings utilizando Ollama e Python.
