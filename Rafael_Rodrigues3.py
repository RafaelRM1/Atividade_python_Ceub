class Carro(object):
    def __init__(self,modelo,ano_modelo,cor):
        self.modelo = modelo
        self.ano_modelo = ano_modelo
        self.cor = cor
    def get_modelo(self):
        return self.modelo
    def set_modelo(self, n_modelo):
        if isinstance(n_modelo, str):
            self.modelo = n_modelo
        else:
            print(f'Erro: Tipo inválido')
    def get_ano_modelo(self):
        return self.ano_modelo
    def set_ano_modelo(self,n_ano_modelo):
        if isinstance(n_ano_modelo,str):
            self.ano_modelo = n_ano_modelo
        else:
            print(f'Erro: Valor inválido')
    def get_cor(self):
        return self.cor
    def set_cor(self,n_cor):
        if isinstance(n_cor,str):
            self.cor = n_cor
        else:
            print(f'Erro: Tipo inválido')
    def __str__(self):
        s = f'Modelo:{self.modelo}\nAno do modelo:{self.ano_modelo}\nCor:{self.cor}'
        return s

class Toyota(Carro):
    def __init__(self,modelo,ano_modelo,cor,ano_compra):
        self.modelo = modelo
        self.ano_modelo = ano_modelo
        self.cor = cor
        super().__init__(modelo,ano_modelo,cor)
        self.ano_compra = ano_compra
    def __str__(self):
        s = f'Modelo:{self.modelo}\nAno do modelo:{self.ano_modelo}\nCor:{self.cor}'
        return s
    def get_ano_compra(self):
        return self.ano_compra
    def set_ano_compra(self,n_ano_compra):
        if isinstance(n_ano_compra,str):
            self.ano_compra = n_ano_compra
        else:
            print(f'Erro: Valor invalido')

if __name__ == '__main__':
    carro1 = Carro('Hillux',2018,'Branca')
    print(carro1)
    print('=' * 30)
    print(carro1.__str__())
    print('='*30)
    c1_nmodelo = input(f'Digite o novo modelo do carro:')
    carro1.set_modelo(c1_nmodelo)
    c1_nano = input(f'Digite o ano de fabricação do {c1_nmodelo}:')
    carro1.set_ano_modelo(c1_nano)
    c1_ncor = input(f'Digite a cor do {c1_nmodelo}:')
    carro1.set_cor(c1_ncor)
    print(f'\nNovo modelo :{carro1.get_modelo()}')
    print(f'Ano de fabricação do {carro1.get_modelo()}:{carro1.get_ano_modelo()}')
    print(f'Cor do {carro1.get_modelo()}:{carro1.get_cor()}')
    print('=' * 30)
    print(carro1.get_modelo())
    print(carro1.get_ano_modelo())
    print(carro1.get_cor())
    print('=' * 30)
    carro2 = Toyota('Yaris',2020,'Vermelho',2021)
    print(carro2.__str__())
    print('=' * 30)
    c2_anoc = input(f'Digite o ano que o {carro2.get_modelo()} foi comprado:')
    carro2.set_ano_compra(c2_anoc)
    print('=' * 30)
    print(f'Modelo do Toyota:{carro2.get_modelo()}')
    print(f'Ano de fabricação do {carro2.get_modelo()}:{carro2.get_ano_modelo()}')
    print(f'Cor do {carro2.get_modelo()}:{carro2.get_cor()}')
    print(f'Ano de compra do {carro2.get_modelo()}:{carro2.get_ano_compra()}')
    print('=' * 30)



