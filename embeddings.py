"""
Atividade acadêmica: geração de embeddings com Ollama e Python.

Pré-requisitos:
1. Ollama instalado e em execução localmente.
2. Modelo instalado: ollama pull nomic-embed-text
3. Dependência instalada: python -m pip install -r requirements.txt
"""

import sys
import ollama

MODELO = "nomic-embed-text"
TEXTO = "A inteligência artificial pode auxiliar no aprendizado."


def gerar_embedding():
    print("=" * 60)
    print("ATIVIDADE: GERAÇÃO DE EMBEDDINGS COM OLLAMA")
    print("=" * 60)
    print(f"Modelo: {MODELO}")
    print(f"Texto de entrada: {TEXTO}")
    print("\nSolicitando embedding ao Ollama local...\n")

    try:
        resposta = ollama.embed(model=MODELO, input=TEXTO)
        embeddings = resposta.get("embeddings", [])

        if not embeddings:
            raise RuntimeError("A resposta do Ollama não contém embeddings.")

        vetor = embeddings[0]

        print("SUCESSO: embedding gerado!")
        print(f"Quantidade de dimensões: {len(vetor)}")
        print("\nPrimeiros 10 valores:")
        for indice, valor in enumerate(vetor[:10], start=1):
            print(f"  Dimensão {indice}: {valor:.8f}")

        print("\nVetor completo:")
        print(vetor)
        print("\nAtividade concluída com sucesso.")

    except Exception as erro:
        print("ERRO: não foi possível gerar o embedding.")
        print("Verifique se o Ollama está instalado e em execução e se")
        print(f"o modelo '{MODELO}' foi baixado com: ollama pull {MODELO}")
        print(f"\nDetalhes técnicos: {erro}")
        sys.exit(1)


if __name__ == "__main__":
    gerar_embedding()
