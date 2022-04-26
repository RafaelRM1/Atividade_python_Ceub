'''class Empregado(object):
    def __init__(self,nome,idade,salario = 1100):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def get_nome(self):
        return self.nome

    def set_nome(self,n_nome):
        if isinstance(n_nome,str):
            self.nome= n_nome
        else:
            print(f'Erro: tipo invalido')

    def get_idade(self):
        return self.idade

    def set_idade(self,n_idade):
        if isinstance(n_idade,str):
            self.idade = n_idade
        else:
            print(f'Erro: tipo invalido')

    def get_salario(self):
        return self.salario
    def set_salario(self,n_salario):
        self.salario = n_salario

    def aumento_salario_pct(self):
        pct = float(input(f'Digite a porcentagem do aumento do salário(ex:0.15-0.80):'))
        if pct >= 0:
            x = self.salario + self.salario * pct
            print(f'O aumento do salario é:{x}')
        else:
            print(f'Valor inválido')

    def salario_ano(self):
        ano = self.salario * 12
        return ano

    def desconto_trans(self):                                       #desconto do vale transporte.
        des = self.salario - 500
        return des

    def __str__(self):
        s = f'Nome do empregado:{self.nome}\nIdade do empregado:{self.idade}\nSalario do empregado:{self.salario}'
        return s

if __name__ == '__main__':
    E1 = Empregado('Ailton','')
    E2 = Empregado('Cleiton','50')
    E3 = Empregado('Roberto','',4000)

    e1_nidade = input(f'Qual a idade do primeiro empregado?')
    E1.set_idade(e1_nidade)

    e1_nsalario = input(f'Qual o salario do primeiro empregado?')
    E1.set_salario(e1_nsalario)

    e2_nsalario = int(input(f'Qual o salario do segundo empregado?'))
    E2.set_salario(e2_nsalario)

    e3_nidade = input(f'Qual a idade do terceiro empregado?')
    E3.set_idade(e1_nidade)
    print('='*30)
    print(E1)
    print('=' * 30)
    print(E2)
    print('=' * 30)
    print(E3)
    print('=' * 30)
    print(f'O salario anual do empregado 2 é de {E2.salario_ano()}')
    E2.desconto_trans()
    E2.aumento_salario_pct()
    print('=' * 30)
    '''

class Pessoa(object):
    qntConta = 0
    def __init__(self,nome):
        self.nome = nome
        Pessoa.qntConta +=1

    def set_nome(self):
        return self.nome

    def get_nome(self,n_nome):
        self.nome = n_nome

    @classmethod
    def get_qtdContas(cls):
        return Pessoa.qntConta

class Professor(Pessoa):
    def __init__(self,nome,qtd_turma):
        self.nome = nome
        super().__init__(nome)
        self.qtd_turma = qtd_turma
    def get_qtd_turma(self):
        return self.qtd_turma
    def set_qtd_turma(self,n_qtd_turma):
        if isinstance(n_qtd_turma,str):
            self.qtd_turma = n_qtd_turma
        else:
            print(f'Erro: tipo invalido')
    def rendimentos(self):
        turma_sal = int(input(f"Quanto o professor recebe por turma?"))
        print(f'O professor recebe {turma_sal} por turma.')
        rend = self.qtd_turma * turma_sal
        print(f'Ja que o professor tem {self.qtd_turma} e recebe {turma_sal} por turma.\nO rendimento total é de {rend}. ')
    def __str__(self):
        s = f'O nome do professor é: {self.nome}\nQuantidade de turma do professor: {self.qtd_turma}'
        return s

class Funcionario(Pessoa):
    
    def __init__(self,nome,salario):
        self.nome = nome
        super().__init__(nome)
        self.salario = salario

    def get_salario(self):
        return self.salario

    def set_salario(self,n_salario):
        if isinstance(n_salario,str):
            self.salario = n_salario
        else:
            print(f'Erro: tipo invalido')

    def __str__(self):
        s = f'O nome do funcionario é :{self.nome}\nO salario do funcionario é:{self.salario}'
        return s
    
    
if __name__ == '__main__':
    p1 = Professor('Renato',5)
    f1 = Funcionario('Ivandro',3000)
    print(f'Quantidade de pessoas:',Pessoa.get_qtdContas())
    print('=' * 30)
    p1.rendimentos()
    print('=' * 30)
    print(f1)
    print('=' * 30)
    print(p1)
    print('=' * 30)






