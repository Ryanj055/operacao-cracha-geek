class Participante:
    """Representa uma pessoa inscrita em um evento geek."""

    # Contador usado para gerar o identificador de cada participante
    __total_cadastrados = 0

    def __init__(self, nome, email, tipo_participacao):
        # Gera o identificador automaticamente (1, 2, 3...)
        Participante.__total_cadastrados += 1
        self.__id = Participante.__total_cadastrados

        # Os dados passam pelos setters, que validam as informações
        self.__nome = ""
        self.__email = ""
        self.__tipo_participacao = ""
        self.nome = nome
        self.email = email
        self.tipo_participacao = tipo_participacao

    # ---------- Getters e Setters (propriedades) ----------

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if not novo_nome or not novo_nome.strip():
            raise ValueError("O nome não pode ser vazio.")
        self.__nome = novo_nome.strip()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, novo_email):
        if not novo_email or "@" not in novo_email:
            raise ValueError("O email informado é inválido.")
        self.__email = novo_email.strip()

    @property
    def tipo_participacao(self):
        return self.__tipo_participacao

    @tipo_participacao.setter
    def tipo_participacao(self, novo_tipo):
        if not novo_tipo or not novo_tipo.strip():
            raise ValueError("O tipo de participação não pode ser vazio.")
        self.__tipo_participacao = novo_tipo.strip()

    # ---------- Método de exibição ----------

    def exibir_informacoes(self):
        print("-" * 40)
        print(f"ID: {self.__id}")
        print(f"Nome: {self.__nome}")
        print(f"Email: {self.__email}")
        print(f"Tipo de participação: {self.__tipo_participacao}")
