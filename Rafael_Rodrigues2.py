class Carro(object):
    def __init__(self, modelo, ano=2021, cor = "preta"):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    def get_modelo(self):
        return self.modelo
    def set_modelo(self, n_modelo):
        self.modelo = n_modelo
    def get_ano(self):
        return self.ano
    def set_ano(self, n_ano):
        self.ano = n_ano
    def get_cor(self):
        return self.cor
    def set_cor(self,n_cor):
        self.cor = n_cor
    def mostrar_dado(self):
        print('Modelo:', self.modelo)
        print('Ano:', self.ano)
        print('Cor:',self.cor)
        print('\n')
    def info_completa(self):
        s = f'{self.modelo} {self.ano} {self.cor}'
        return s
    def __str__(self):
        s = f'{self.info_completa()}'
        return s




if __name__ == '__main__':
    carro1 = Carro('Uno', 2018 ,"verde")
    carro2 = Carro('Maverick', 2019)
    carro3 = Carro('Gol bolinha')
    print('*'*30)
    print('CARRO 1')
    print('Modelo:', carro1.get_modelo())
    print('Ano:', carro1.get_ano())
    print('Cor',carro1.get_cor())
    print('CARRO 2:')
    print(f'Modelo: {carro2.get_modelo()}')
    print(f'Ano: {carro2.get_ano()}')
    print(f'Cor: {carro2.get_cor()}')
    print('*'*30)
    print(carro1)
    print(carro2)
    print(carro3)
    print('*'*30)
    modelo1 = input('Digite o novo modelo do carro 1:')
    carro1.set_modelo(modelo1)
    print('Novo modelo carro 1:', carro1.get_modelo())
    carro2.set_modelo('Fusion')
    print('Novo modelo carro 2:', carro2.get_modelo())
    print('*'*30)
    ano1 = input('Digite o ano do carro 1:')
    ano3 = input('Digite o ano do carro 3:')
    carro1.set_ano(ano1)
    print('Novo Ano carro 1:', carro1.get_ano())
    carro2.set_ano(2012)
    print('Novo Ano carro 2:', carro2.get_ano())
    carro3.set_ano(ano3)
    print('Novo Ano carro 3:', carro3.get_ano())
    print('*'*30)
    cor3 = input("Digite a nova cor do carro 3:")
    carro3.set_cor(cor3)
    print(f'A nova cor do carro é {carro3.get_cor()} ')
    print('*'*30)
    carro1.mostrar_dado()
    carro2.mostrar_dado()
    carro3.mostrar_dado()
    print('*'*30)
    print('Informações do carro 1:')
    print(carro1.__str__())
    print('Info. Completa carro 3:\n', carro3.info_completa())
    print('*'*30)
    print(carro1.info_completa())
    print(carro2.info_completa())
    print(carro3.info_completa())