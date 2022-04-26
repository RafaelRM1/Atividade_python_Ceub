"""1.	Resolva estes itens com funções de lista:
a. Crie uma lista vazia e acrescente alguns valores numéricos usando pelo menos dois métodos diferentes.
b. Leia um valor e verifique se ele está na lista. Se estiver, mostre também a posição (índice) do valor encontrado na pesquisa;
c. Mostre a lista na ordem crescente.
d. Insira (acrescente) o valor 55 na posição (índice) 1 da lista.
e. Mostre a lista na ordem decrescente.
f. Elabore o enunciado e a implementação de mais uma questão na lista cria
f. Elabore o enunciado e a implementação de mais uma questão na lista criada. A complexidade do enunciado e da implementação da questão serão considerados para mensurar a avaliação da questão.
Não faça exercício igual aos ministrados nas aulas."""

#Rafael Rodrigues Martins


"""Abaixo uma lista de carros.Acrescente alguns carros a lista """
"""
lista1 = []
lista1.append(1)
lista1.append(2)
lista1.append(3)
lista1.append(4)
lista1.append(5)
lista1.index(4,1,5)
print("A posição do carro 4 é :")
print(lista1.index(4,1,5))
print(lista1)
lista1.insert(1,55)
print('-'*30)
print(lista1)
listar = lista1 [::-1]
print(listar)
acrescenta = input("Deseja acrescentar algum carro a lista:")
if (acrescenta == 'sim'):
    for cont in range(0,4):
        l = lista1.append(int(input("Digite o numero a ser acrescentado:")))
print(lista1)"""




"""2. Crie a classe conta corrente com as características titular, número da conta , saldo. Crie o método construtor recebendo self e os três parâmetros, coloque pelo menos um desses parâmetros com valor default (padrão).
Crie pelo menos um método get e pelo menos um método set e faça crítica no método set.
Crie o método funcional depósito, ele recebe um valor que será depositado na conta corrente, faça crítica.

No método main, instancie dois objetos dessa classe. Crie o objeto conta1 passando os três argumentos e o crie o objeto conta2 passando apenas dois argumentos. Use (teste) todos os método criados na classe para os objetos conta1 e conta2.

Elabore o enunciado e a implementação de mais um método funcional na classe Livro. A complexidade do enunciado e da implementação do método serão considerados para mensurar a avaliação do método.
Obs.: este método deve ser diferente dos métodos vistos nos exemplos usados nas aulas."""
"""
class ContaCorrente:
    def __init__(self,titular,numero_conta,saldo):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo

    def get_saldo(self):
        return self.saldo

    def set_saldo(self,n_saldo):
        self.saldo = n_saldo

    def Deposito(self):
        depositar = 0
        self.saldo += depositar

    def MostraDados(self):
        print(f"O nome do titular é {self.titular}")
        print(f"O numero da conta é {self.numero_conta}")
        print(f"O saldo do cliente é {self.saldo}")


if __name__ == '__main__':
    conta1 = ContaCorrente("Pedro",1123,"R$400.00")
    conta2 = ContaCorrente("Satanas",1212,"")
    print("******************************************")
    saldo1 = input("Digite o novo saldo:",conta1.get_saldo())
    saldo2 = input("Digite o novo saldo:",conta2.get_saldo())
    conta1.set_saldo(saldo1)
    conta2.set_saldo(saldo2)
    print('******************************************')
    conta1.Deposito()
    conta2.Deposito()
    conta1.MostraDados()
    conta2.MostraDados()"""




