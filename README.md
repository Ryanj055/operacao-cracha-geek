# Operação Crachá Geek – Cadastro de Participantes

Foi desenvolvido um pequeno sistema em Python, orientado a objetos, para cadastrar participantes de eventos geek, como campeonatos, cosplay e palestras.
A classe `Participante` representa uma pessoa inscrita no evento e guarda os dados dela.
Seus atributos são: `id` (gerado automaticamente), `nome`, `email` e `tipo_participacao`.
Os métodos utilizados são: o construtor `__init__` (recebe e cadastra os dados), os getters e setters (propriedades) de cada atributo e o método `exibir_informacoes()`.
O encapsulamento foi aplicado deixando todos os atributos privados (com `__`), de modo que só podem ser lidos ou alterados pelos getters e setters, que também validam os dados.
Os três objetos (campeonato, cosplay e palestra) foram testados no `main.py`, que os cria com dados diferentes e chama `exibir_informacoes()` para mostrar cada cadastro no terminal.

## Como executar
1. Abra a pasta do projeto no Visual Studio Code.
2. No terminal, execute: `python main.py`
