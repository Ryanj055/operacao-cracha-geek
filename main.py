from participante import Participante


def main():
    print("=== OPERAÇÃO CRACHÁ GEEK – CADASTRO DE PARTICIPANTES ===")
    print()

    # Três objetos, cada um com seus próprios dados
    participante_campeonato = Participante(
        "Lucas Almeida", "lucas.almeida@email.com", "Campeonato"
    )
    participante_cosplay = Participante(
        "Marina Costa", "marina.costa@email.com", "Cosplay"
    )
    participante_palestra = Participante(
        "Rafael Souza", "rafael.souza@email.com", "Palestra"
    )

    # Exibe os três cadastros no terminal
    participante_campeonato.exibir_informacoes()
    participante_cosplay.exibir_informacoes()
    participante_palestra.exibir_informacoes()
    print("-" * 40)


if __name__ == "__main__":
    main()
