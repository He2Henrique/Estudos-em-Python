import time


class cronometro:
    # init geralmeente e usado para definir atributos iniciais de uma instancia.
    def __init__(self):
        self.ini = 0
        self.end = 0

    def inicio(self):
        self.ini = time.time()

    def fim(self):
        self.end = time.time()
        tempo_total = self.end - self.ini
        print(f"Tempo de execução: {tempo_total} segundos")


def aprendendo_classes():
    class Retangulo:
        # init geralmeente e usado para definir atributos iniciais de uma instancia, pense que aqui e onde voce vai configurar a classe..
        def __init__(self, altura, largura):
            self.altura = altura
            self.largura = largura

        def calcular_area(self):
            return self.altura * self.largura

        def calcular_perimetro(self):
            return 2 * (self.altura + self.largura)

    # Criando uma instância da classe Retangulo
    retangulo = Retangulo(5, 10)

    # Usando os métodos da classe
    area = retangulo.calcular_area()
    perimetro = retangulo.calcular_perimetro()

    print("Área do retângulo:", area)
    print("Perímetro do retângulo:", perimetro)

    # apresenta itens de uma lista
