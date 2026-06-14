class Figurinha:
    """Representa uma figurinha da Copa do Mundo."""

    def __init__(self, id, nome, pais, posicao, raridade):
        self.id = id              
        self.nome = nome         
        self.pais = pais          
        self.posicao = posicao    
        self.raridade = raridade  

    def __str__(self):
        
        return (f"#{self.id} | {self.nome} ({self.pais}) "
                f"- {self.posicao} - {self.raridade}")