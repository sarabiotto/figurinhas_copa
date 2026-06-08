class Figurinha:
    """Representa uma figurinha da Copa do Mundo."""

    def __init__(self, id, nome, pais, posicao, raridade):
        self.id = id              # número da figurinha no álbum
        self.nome = nome          # nome do jogador
        self.pais = pais          # seleção (ex: Brasil, Argentina)
        self.posicao = posicao    # posição em campo (ex: Atacante)
        self.raridade = raridade  # comum, prata, ouro, lendária...

    def __str__(self):
        # Define como a figurinha aparece quando damos print()
        return (f"#{self.id} | {self.nome} ({self.pais}) "
                f"- {self.posicao} - {self.raridade}")