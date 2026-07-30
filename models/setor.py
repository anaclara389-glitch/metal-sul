class setor:
    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome
        
    @property
    def id(self):
        return self.__id
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def apresentar(self):
        print("=== Setor ===")
        print(f"ID: {self.id}")
        print(f"Nome do Setor: {self.nome}")
        
    @nome.setter
    def nome(self, novo_nome): #Validação ocorre antes da alteração do atributo
        if not novo_nome.strip():
            raise ValueError("O cargo não pode estar vazio")
        self.__nome = novo_nome