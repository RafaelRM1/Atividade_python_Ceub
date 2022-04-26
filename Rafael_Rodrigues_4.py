class Animal(object):
    def __init__(self,especie_raca,cor,alimento,mov):
        self.especie_raca = especie_raca
        self.cor = cor
        self.alimento = alimento
        self.mov = mov

    def get_especie_raca(self):
        return self.especie_raca

    def set_especie_raca(self,n_especie_raca):
        if isinstance(n_especie_raca,str):
            self.especie_raca = n_especie_raca
        else:
            print(f'Erro: Tipo invalido')

    def get_cor(self):
        return self.cor

    def set_cor(self,n_cor):
        if isinstance(n_cor,str):
            self.cor = n_cor
        else:
            print(f'Erro: Cor invalida')

    def get_alimento(self):
        return self.alimento

    def set_alimento(self,n_alimento):
        if isinstance(n_alimento,str):
            self.alimento = n_alimento
        else:
            print(f'Erro: Tipo invalido')

    def get_mov(self):
        return self.mov

    def set_mov(self,n_mov):
        if isinstance(n_mov,str):
            self.mov = n_mov
        else:
            print(f'Erro: Tipo invalido')


class Cachorro(Animal):

    def __init__(self,especie_raca,cor,alimento,mov,qtd_patas):
        self.especie_raca = especie_raca
        self.cor = cor
        self.alimento = alimento
        self.mov = mov
        super().__init__(especie_raca,cor,alimento,mov)
        self.qtd_patas = qtd_patas

    def get_qtd_patas(self):
        return self.qtd_patas

    def set_qtd_patas(self,n_qtd_patas):
        if isinstance(n_qtd_patas,str):
            self.qtd_patas = n_qtd_patas
        else:
            print(f'Erro: Tipo invalido')

    def __str__(self):
        s = f'Raça do cachorro:{self.especie_raca}\nCor:{self.cor}\nAlimentação:{self.alimento}\nMovimentação:{self.mov}\nQuantidade de patas:{self.qtd_patas}'
        return s


class Cobra(Animal):

    def __init__(self,especie_raca,cor,alimento,mov,veneno):
        self.especie_raca = especie_raca
        self.cor = cor
        self.alimento = alimento
        self.mov = mov
        super().__init__(especie_raca,cor,alimento,mov)
        self.veneno = veneno

    def get_veneno(self):
        return self.veneno

    def set_veneno(self,n_veneno):
        if isinstance(n_veneno,str):
            self.veneno = n_veneno
        else:
            print(f'Erro: Tipo invalido')

    def __str__(self):
        s = f'Especie da cobra:{self.especie_raca}\nCor:{self.cor}\nAlimentação:{self.alimento}\nMovimentação:{self.mov}\nVenosa:{self.veneno}'
        return s


if __name__ == '__main__':
    cachorro1 = Cachorro('Bulldogue','Preto','Ração','Devagar',4)
    print(cachorro1)
    print('=' * 30)
    c1_nraca = input(f'Qual é a raça do cachorro ?')
    cachorro1.set_especie_raca(c1_nraca)
    c1_ncor = input(f'Qual a cor do cachorro ?')
    cachorro1.set_cor(c1_ncor)
    c1_nali = input(f'Qual a alimentação do cachorro?')
    cachorro1.set_alimento(c1_nali)
    c1_nmov = input(f'Como o cachorro se movimenta?(rapido,moderado ou devagar)')
    cachorro1.set_mov(c1_nmov)
    c1_nqtd_patas = input(f'Quantas patas tem seu cachorro?')
    cachorro1.set_qtd_patas(c1_nqtd_patas)
    print('=' * 30)
    print(cachorro1)
    cobra1 = Cobra('Sucuri','Preta','Ovo','Moderado','Sim')
    print('=' * 30)
    print(cobra1)
    print('=' * 30)
    s1_nespecie = input(f'Qual é a especie da cobra?')
    cobra1.set_especie_raca(s1_nespecie)
    s1_ncor = input(f'Qual a cor da cobra?')
    cobra1.set_cor(s1_ncor)
    s1_nali = input(f'O que a cobra come?')
    cobra1.set_alimento(s1_nali)
    s1_nmov = input(f'Como a cobra se movimenta?(rapido,moderado ou devagar)')
    cobra1.set_mov(s1_nmov)
    s1_nven = input(f'A cobra é venenosa?')
    cobra1.set_veneno(s1_nven)
    print('=' * 30)
    print(cobra1.__str__())
    print('=' * 30)
