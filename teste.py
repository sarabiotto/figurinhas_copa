from figurinha import Figurinha
from album import Album

album = Album()

album.adicionar(Figurinha(1, "Vinícius Jr.", "Brasil", "Atacante", "ouro"))
album.adicionar(Figurinha(2, "Messi", "Argentina", "Atacante", "lendária"))
album.adicionar(Figurinha(3, "Mbappé", "França", "Atacante", "ouro"))

print("--- Álbum completo ---")
album.listar()

print("\n--- Buscando a figurinha 2 ---")
print(album.buscar(2))

print("\n--- Tentando adicionar a 2 de novo ---")
repetida = album.adicionar(Figurinha(2, "Messi", "Argentina", "Atacante", "lendária"))
print("Foi adicionada?", repetida)   

print("\n--- Removendo a figurinha 2 (do meio) ---")
album.remover(2)
album.listar()   

print("\n--- Removendo a figurinha 1 (a primeira) ---")
album.remover(1)
album.listar()   

print("\n--- Porcentagem (supondo álbum de 10 figurinhas) ---")
print(f"{album.porcentagem(10):.1f}% concluído")  

print("\n=== TESTE DE REPETIDAS ===")
album2 = Album()

album2.adicionar(Figurinha(1, "Vinícius Jr.", "Brasil", "Atacante", "ouro"))
album2.adicionar(Figurinha(2, "Messi", "Argentina", "Atacante", "lendária"))


album2.adicionar(Figurinha(1, "Vinícius Jr.", "Brasil", "Atacante", "ouro"))
album2.adicionar(Figurinha(1, "Vinícius Jr.", "Brasil", "Atacante", "ouro"))
album2.adicionar(Figurinha(2, "Messi", "Argentina", "Atacante", "lendária"))

print("--- Repetidas ---")
album2.listar_repetidas()
print("Total de repetidas:", album2.contar_repetidas())   

print("\n=== TESTE DE BUSCAS ===")
from album import imprimir_lista

album3 = Album()
album3.adicionar(Figurinha(1, "Vinícius Jr.", "Brasil", "Atacante", "ouro"))
album3.adicionar(Figurinha(2, "Casemiro", "Brasil", "Volante", "prata"))
album3.adicionar(Figurinha(3, "Messi", "Argentina", "Atacante", "lendária"))

print("--- Por número (#2) ---")
print(album3.buscar(2))

print("\n--- Por jogador ('vini') ---")
imprimir_lista(album3.buscar_por_jogador("vini"))

print("\n--- Por seleção ('Brasil') ---")
imprimir_lista(album3.buscar_por_selecao("Brasil"))