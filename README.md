# figurinhas_copa

# Álbum de Figurinhas — Copa 2026

Sistema de gerenciamento de figurinhas da Copa do Mundo, desenvolvido como
terceiro projeto da disciplina de **Estrutura de Dados** (Fatec Rio Claro).

O sistema permite colecionar, organizar e trocar figurinhas de jogadores e
seleções, usando **estruturas de dados implementadas do zero** — lista
encadeada e filas FIFO construídas com nós encadeados, sem usar `list`,
`deque` ou qualquer estrutura pronta do Python para isso.

## Como executar

Requisito: Python 3 instalado.

```bash
python main.py
```

O programa abre um menu no terminal. Ao iniciar, ele tenta carregar um álbum
salvo (`album.json`); ao sair, salva automaticamente.

## Estrutura do projeto

| Arquivo            | Responsabilidade                                              |
|--------------------|--------------------------------------------------------------|
| `figurinha.py`     | Classe `Figurinha` — representa uma figurinha (id, nome, país, posição, raridade). |
| `nodos.py`         | Classes `NodoLista` e `NodoFila` — os "elos" das estruturas encadeadas. |
| `album.py`         | Classe `Album` — o álbum como lista encadeada (inserir, remover, buscar, repetidas, porcentagem). |
| `fila.py`          | Classe `Fila` — fila FIFO própria (enqueue, dequeue, peek, limpar). |
| `historico.py`     | Classe `Historico` — registra as trocas usando uma `Fila`.   |
| `trocas.py`        | Função `efetuar_troca` — troca repetidas entre dois álbuns.   |
| `persistencia.py`  | Salvar e carregar o álbum em arquivo JSON.                   |
| `main.py`          | Menu interativo que integra todas as funcionalidades.        |

## Funcionalidades

**Álbum**
- Inserir, remover e consultar figurinhas
- Ver o álbum completo
- Ver a porcentagem concluída

**Figurinhas repetidas**
- Armazenar repetidas em uma lista separada
- Listar e contar as repetidas

**Buscas**
- Por número da figurinha
- Por jogador (busca por parte do nome)
- Por seleção

**Trocas**
- Verificar se ambos os colecionadores têm a repetida desejada
- Efetuar a troca automaticamente
- Registrar cada troca no histórico

**Persistência**
- Salvar e carregar os dados em arquivo JSON
- Tratamento de erro quando o arquivo não existe

## Sobre as estruturas de dados

O requisito técnico do projeto proíbe o uso de `list`, `deque` ou estruturas
prontas do Python para implementar a lista e as filas. Por isso:

- **Lista encadeada (Album):** cada figurinha fica em um `NodoLista`, que guarda
  o dado e uma referência (`proximo`) para o próximo nó. O álbum mantém apenas
  o ponteiro para o primeiro nó (`_cabeca`) e percorre a corrente nó a nó.

- **Fila FIFO (Fila):** implementada com `NodoFila`, mantendo ponteiros para o
  início (de onde as figurinhas saem) e o fim (onde entram). Isso garante que a
  primeira figurinha a entrar seja a primeira a sair.

A única `list` do Python presente no projeto está no arquivo de persistência,
usada apenas como formato temporário para gravar/ler o JSON — e **não** para
implementar as estruturas de dados, o que respeita o requisito.

Tratamento de entradas inválidas é feito ao longo do programa (números
inválidos no menu, campos vazios no cadastro, arquivo inexistente ao carregar).

## Autora

Projeto desenvolvido por Sara — disciplina de Estrutura de Dados, Fatec Rio Claro.