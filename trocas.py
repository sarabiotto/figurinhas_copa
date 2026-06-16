def efetuar_troca(album_a, album_b, id_que_a_quer, id_que_b_quer, historico):

    if not album_b.tem_repetida(id_que_a_quer):
        print(f"Troca cancelada: B não tem a #{id_que_a_quer} repetida.")
        return False
    if not album_a.tem_repetida(id_que_b_quer):
        print(f"Troca cancelada: A não tem a #{id_que_b_quer} repetida.")
        return False


    figurinha_para_a = album_b.remover_repetida(id_que_a_quer)
    figurinha_para_b = album_a.remover_repetida(id_que_b_quer)


    album_a.adicionar(figurinha_para_a)
    album_b.adicionar(figurinha_para_b)


    historico.registrar(
        f"Troca feita: A recebeu a #{id_que_a_quer}, "
        f"B recebeu a #{id_que_b_quer}."
    )
    print("Troca realizada com sucesso!")
    return True