import json
from figurinha import Figurinha


def salvar(album, nome_arquivo):

    figurinhas = []  

    atual = album._cabeca
    while atual is not None:
        f = atual.figurinha
        figurinhas.append({
            "id": f.id,
            "nome": f.nome,
            "pais": f.pais,
            "posicao": f.posicao,
            "raridade": f.raridade
        })
        atual = atual.proximo

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(figurinhas, arquivo, ensure_ascii=False, indent=4)

    print(f"Álbum salvo em '{nome_arquivo}' ({len(figurinhas)} figurinhas).")


def carregar(album, nome_arquivo):

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            figurinhas = json.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado. Começando vazio.")
        return

    for dados in figurinhas:
        figurinha = Figurinha(
            dados["id"],
            dados["nome"],
            dados["pais"],
            dados["posicao"],
            dados["raridade"]
        )
        album.adicionar(figurinha)

    print(f"Álbum carregado de '{nome_arquivo}' ({len(figurinhas)} figurinhas).")