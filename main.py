from figurinha import Figurinha
from album import Album, imprimir_lista
from historico import Historico
from trocas import efetuar_troca
from persistencia import salvar, carregar

TOTAL_ALBUM = 50
ARQUIVO = "album.json"


def ler_inteiro(mensagem):

    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")


def cadastrar_figurinha(album):
    print("\n--- Nova figurinha ---")
    id = ler_inteiro("Número da figurinha: ")
    nome = input("Nome do jogador: ").strip()
    pais = input("Seleção: ").strip()
    posicao = input("Posição: ").strip()
    raridade = input("Raridade (comum/prata/ouro/lendária): ").strip()

    if nome == "" or pais == "":
        print("Nome e seleção não podem ficar vazios.")
        return

    figurinha = Figurinha(id, nome, pais, posicao, raridade)
    if album.adicionar(figurinha):
        print("Figurinha adicionada ao álbum!")
    else:
        print("Você já tinha essa figurinha. Foi pra pilha de repetidas.")


def menu():
    album = Album()
    historico = Historico()

    carregar(album, ARQUIVO)

    while True:
        print("\n" + "=" * 40)
        print("   ÁLBUM DE FIGURINHAS - COPA 2026")
        print("=" * 40)
        print("1  - Adicionar figurinha")
        print("2  - Remover figurinha")
        print("3  - Consultar figurinha (por número)")
        print("4  - Ver álbum completo")
        print("5  - Ver porcentagem concluída")
        print("6  - Ver figurinhas repetidas")
        print("7  - Buscar por jogador")
        print("8  - Buscar por seleção")
        print("9  - Fazer uma troca")
        print("10 - Ver histórico de trocas")
        print("11 - Salvar álbum")
        print("0  - Sair")
        print("=" * 40)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_figurinha(album)

        elif opcao == "2":
            id = ler_inteiro("Número da figurinha a remover: ")
            if album.remover(id):
                print("Figurinha removida.")
            else:
                print("Figurinha não encontrada no álbum.")

        elif opcao == "3":
            id = ler_inteiro("Número da figurinha: ")
            figurinha = album.buscar(id)
            if figurinha is not None:
                print("Encontrada:", figurinha)
            else:
                print("Você ainda não tem essa figurinha.")

        elif opcao == "4":
            print("\n--- Álbum completo ---")
            album.listar()

        elif opcao == "5":
            pct = album.porcentagem(TOTAL_ALBUM)
            print(f"Álbum {pct:.1f}% concluído "
                  f"(de {TOTAL_ALBUM} figurinhas).")

        elif opcao == "6":
            print("\n--- Repetidas ---")
            album.listar_repetidas()
            print("Total de repetidas:", album.contar_repetidas())

        elif opcao == "7":
            nome = input("Nome (ou parte) do jogador: ").strip()
            print("\n--- Resultados ---")
            imprimir_lista(album.buscar_por_jogador(nome))

        elif opcao == "8":
            pais = input("Seleção: ").strip()
            print("\n--- Resultados ---")
            imprimir_lista(album.buscar_por_selecao(pais))

        elif opcao == "9":
            print("\n--- Troca ---")
            print("(Para o teste, criamos um segundo álbum simples.)")
            outro = Album()
            outro.adicionar(Figurinha(99, "Outro jogador", "Espanha", "Meia", "ouro"))
            outro.adicionar(Figurinha(99, "Outro jogador", "Espanha", "Meia", "ouro"))
            quero = ler_inteiro("Número que VOCÊ quer receber: ")
            dou = ler_inteiro("Número que você vai DAR (sua repetida): ")
            efetuar_troca(album, outro, quero, dou, historico)

        elif opcao == "10":
            print("\n--- Histórico de trocas ---")
            historico.listar()

        elif opcao == "11":
            salvar(album, ARQUIVO)

        elif opcao == "0":
            salvar(album, ARQUIVO)
            print("Até a próxima!")
            break

        else:
            print("Opção inválida. Escolha um número do menu.")


if __name__ == "__main__":
    menu()