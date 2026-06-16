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

print("\n=== TESTE DA FILA FIFO ===")
from fila import Fila

fila = Fila()
fila.enqueue(Figurinha(1, "Vinícius Jr.", "Brasil", "Atacante", "ouro"))
fila.enqueue(Figurinha(2, "Messi", "Argentina", "Atacante", "lendária"))

print("Quem está na frente (peek):", fila.peek())    
print("Saiu (dequeue):", fila.dequeue())             
print("Saiu (dequeue):", fila.dequeue())             
print("Saiu de novo:", fila.dequeue())               

print("\n=== TESTE DO HISTÓRICO ===")
from historico import Historico

hist = Historico()
hist.registrar("Troca: dei a #1 e recebi a #5")
hist.registrar("Bafo: ganhei 3 figurinhas do João")
hist.listar()

print("\n=== TESTE DE TROCAS ===")
from trocas import efetuar_troca

hist_trocas = Historico()

# Ana tem a #5 repetida
ana = Album()
ana.adicionar(Figurinha(1, "Alisson", "Brasil", "Goleiro", "prata"))
ana.adicionar(Figurinha(5, "Neymar", "Brasil", "Atacante", "ouro"))
ana.adicionar(Figurinha(5, "Neymar", "Brasil", "Atacante", "ouro"))  


bruno = Album()
bruno.adicionar(Figurinha(1, "Alisson", "Brasil", "Goleiro", "prata"))
bruno.adicionar(Figurinha(9, "Haaland", "Noruega", "Atacante", "ouro"))
bruno.adicionar(Figurinha(9, "Haaland", "Noruega", "Atacante", "ouro"))  

print("--- Troca válida: Ana quer a #9, Bruno quer a #5 ---")
efetuar_troca(ana, bruno, 9, 5, hist_trocas)

print("\nÁlbum da Ana agora:")
ana.listar()  

print("\n--- Troca inválida: ninguém tem a #99 repetida ---")
efetuar_troca(ana, bruno, 99, 5, hist_trocas)

print("\n--- Histórico das trocas ---")
hist_trocas.listar()

print("\n=== TESTE DE PERSISTÊNCIA ===")
from persistencia import salvar, carregar

# salva o álbum da Ana num arquivo
salvar(ana, "album_ana.json")

# cria um álbum novo e carrega do arquivo
ana_carregada = Album()
carregar(ana_carregada, "album_ana.json")

print("\nÁlbum recarregado do arquivo:")
ana_carregada.listar()