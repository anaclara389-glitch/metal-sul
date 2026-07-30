class Funcionario:
    def __init__(self, id, nome, cargo, salario, setor):
        self.__id = id
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario
        self.__setor = setor

    def apresentar(self):
        print("===== Dados do usuário =====")
        print(f"Id do funcionario: {self.__id}")
        print(f"Nome do funcionario: {self.__nome}")
        print(f"Cargo do funcionario: {self.__cargo}")
        print(f"Salário do funcionario: R${self.__salario}")
        print(f"Setor: {self.setor.nome}")
        
    '''def aumentar_salario(self, percentual):
        aumento = self.__salario * (percentual/100)
        self.__salario += aumento'''

    def trocar_cargo(self, novo_cargo):
        self.__cargo = novo_cargo
        
        
    #getters
    @property
    def setor(self):
        return self.__setor
    
    @property
    def id(self):
        return self.__id
    
    @property
    def nome(self):
            return self.__nome
        
    @property
    def cargo(self):
            return self.__cargo
        
    @property
    def salario(self):
            return self.__salario
        
    
    
    
    #Setters
    #valor único de referência e não mutável
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @cargo.setter
    def cargo(self, novo_cargo):
        if novo_cargo == "":
            raise ValueError("O cargo não pode estar vazio.")
        self.__cargo = novo_cargo
        
    @salario.setter
    def salario(self, valor):
        if valor < 0:
            raise ValueError(f"O salário '{valor}' não pode ser negativo")
        self.__salario = valor
        
    
    def aumentar_salario(self, valor):
        if valor <= 0:
            raise ValueError(f"O aumento '{valor}' deve ser maior que zero.")
        self.__salario += valor