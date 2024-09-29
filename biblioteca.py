
import math
import re
import time


class cronometro:
    # init geralmeente e usado para definir atributos iniciais de uma instancia, pense que aqui e onde voce vai configurar a classe..
    def __init__(self):
        self.ini = 0
        self.end = 0

    def inicio(self):
        self.ini = time.time()

    def fim(self):
        self.end = time.time()
        tempo_total = self.end - self.ini
        print(f"Tempo de execução: {tempo_total} segundos")


def select_iten(lista, title="chose an element of list: "):
    print(title)
    for i, e in enumerate(lista):
        print(f"{i+1}- {e}")

    while True:
        chs = input(title)
        try:
            chs = int(chs)
            if chs <= 0:
                raise IndexError
            iten = lista[chs-1]
            break
        except ValueError:
            print("valor digitado nao é um numero")
        except IndexError:
            print("fora do index")

    return iten


def find_num():

    for i in range(48, 58):
        crc = chr(i)
        print(crc)

    # aqui o e printado o numero da tabela ascii


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # o desafio se trata diser se duas strings sao um anagrama ou nao
        if len(s) != len(t):  # logo de primeira se nao for do mesmo tamanho ja pode dizer que nao funciona
            return False

        # cria uma lista de 26 zeros, o que siguinifica que ele ta pegando a diferença entre a ate z o as letras do alfabet..
        freq = [0] * 26

        for i in range(len(s)):  # define de 0 ate 7, entao nao precisa definir o ponto de ininico no for, se for passado qualquer valor ele vai de 0 ate o valor
            # aqui vai pegar a posicao da letra no alfabeto e marcar com posivo nos dizendo que a letra esta presente na string
            freq[ord(s[i]) - ord('a')] += 1
            # no caso como aqui e um desafio de saber se e um anagrama ou nao ele vai pegar a outra string e marca com negativo para que os dados se anulem indicando que a string tem as mesmas letras so que em ordens deiferentes
            freq[ord(t[i]) - ord('a')] -= 1

        for i in range(len(freq)):
            if freq[i] != 0:
                return False

        return True


def is_letter(char):
    return char.isalpha()


def looks_like(str1, str2):
    freq = [0] * 27  # Henrique mandou atulizar essa bagaça pra ter ç

    var = 0
    for i in range(len(str1)):
        if is_letter(str1[i]):
            freq[ord(str1[i]) - ord('a')] += 1
        elif ord(str1[i]) == ord(' '):
            freq[26] += 1

    for i in range(len(str2)):
        if is_letter(str2[i]):
            freq[ord(str2[i]) - ord('a')] -= 1
        elif ord(str2[i]) == ord(' '):
            freq[26] -= 1

    for i in range(len(freq)):
        p_freq = freq[i] ** 2
        p_freq = math.sqrt(p_freq)

        var += p_freq

    var = var/2

    similarity = (len(str1) - var) / len(str1)
    similarity *= 100
    return similarity

# provavelment um test


def listas_bi():
    list1 = [['nome', 'sexo', 'idade']]

    for i in range(4):
        list2 = ['cavalo', 'farm', 'job']
        list1.append(list2)

    print(list1)


def editando_strings(lista_strings, desejado):

    # Convertendo a string em uma lista de caracteres para modificar individualmente
    segunda_string = list(lista_strings[1])

    # removendo apenas o que eu quero
    segunda_string.remove(desejado)

    # Substituindo a string modificada de volta na lista original
    lista_strings[1] = ''.join(segunda_string)

    print(lista_strings)


def tipo_da_string():
    var = 'com2 de pix'

    print(var.isalnum())
    print(var.isalpha())
    print(var.isdecimal())
    print(var.isdigit())
    print(var.isascii())
    print(var.isspace())
    var = var.split('/')
    print(var)


def encontrando_complemento_em_listas(nums, target):
    numMap = {}
    n = len(nums)
    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return numMap[complement], i
        numMap[nums[i]] = i

    return []


# Usando classes e self
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


def interface(lista):
    for i, e in enumerate(lista):
        print(f" {i + 1} - {e}")


# comparando tamplates
def comparar_formato(string, formato):
    if len(string) != len(formato):
        return False

    for char, pattern in zip(string, formato):
        if pattern == 'n' and not char.isdigit():
            return False
        if pattern == 'l' and not char.isalpha():
            return False
        if pattern == '.' and char != '.':
            return False

    return True


def identificar_expressao(padrao, texto):
    padrao = re.compile(padrao)
    valores = padrao.findall(texto)
    return valores


def frases(lista):
    arm = []  # variavel de armazenamento
    lista_strings = []

    for i in lista:
        if i.isalpha():
            arm.append(i)
        elif arm:
            lista_strings.append(' '.join(arm))
            arm.clear()
    return lista_strings


def tratamento_de_erro():
    while True:  # alem de ser de simular um do while
        nota = input(f"digite nota: ")
        try:
            nota = float(nota)
            if nota < 0 or nota > 10:
                raise ValueError
            break
        except ValueError:
            print("nota invalida tente novamente")
