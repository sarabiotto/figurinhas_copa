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
print("Foi adicionada?", repetida)   # deve dar False