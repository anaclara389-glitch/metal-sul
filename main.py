from models.funcionario import Funcionario
from models.setor import setor

Setor1 = setor(1, "TA")
Funcionario1 = Funcionario(1, "Jonas", "Dev", 5500.00, Setor1)

Funcionario1.aumentar_salario(500)
Funcionario1.apresentar()


#----------------------------------------------------------------------------------

'''Setor1.nome = "Tech"
Setor1.apresentar'''
#parece que estamos acessando o atributo diretamente
#entretanto o python executa o método definido @nome.setter
#permit que ocorra validações
#Setor1.nome = "" #devolve erro

#----------------------------------------------------------------------------------

"""Funcionario1.apresentar()
print()
print(Funcionario.nome)
print(Funcionario.salario)
print()
Funcionario1.salario = 7000
Funcionario1.cargo = "dev S
Funcionario1.apresentar()"""


#----------------------------------------------------------------------------------

'''Funcionario1.apresentar()
print("="*50)
Funcionario1.aumentar_salario(15)
Funcionario1.trocar_cargo("Gerente")
print()
Funcionario1.apresentar()'''

#---------------------------------------------------------------------------------

"""
print(Funcionario1.get_id())
print(Funcionario1.get_nome())
print(Funcionario1.get_cargo())
print(Funcionario1.get_salario())

Funcionario1.set_nome("Matias")
Funcionario1.set_cargo("Dev TI")
Funcionario1.set_salario(7000.00)
Funcionario1.apresentar()
"""

    #restrição por encapsulamento != validação
"""
    A distinção entre encapsular e validar é um pilar fundamental da Programação Orientada a Objetos, pois o encapsulamento, 
    por si só, apenas restringe os canais de acesso e modificação dos atributos. 
    A garantia de que um dado é íntegro e condizente com as regras do negócio permanece sob a responsabilidade do desenvolvedor, que deve programar os critérios de validação. 
    É exatamente por essa razão que métodos modificadores como set_nome(), set_salario() e set_cargo() tornam-se indispensáveis: 
    eles atuam como pontos centralizados de alteração dentro da classe, 
    o que viabiliza a implementação e a futura manutenção de regras de validação sem a necessidade de reescrever ou impactar o restante do sistema.
"""
    
#COMPOSIÇÃO
#funcionario possui um setor
#produto possui um fornecedor
#produto pertence a um setor

#HERANÇA
#Gerente é um funcionário
#Supervisor é um funcionário
#ADM é um funcionário

