
import re
import ast
import inspect
from manipulando_listas import *


def spliter(st, simbol, tipo, times=float('inf')):
    # ele recebe de entrad a string o simbulo e o tipo de slipter e a quantidade de vezes que que queres dividir ou recortar

    if tipo == "divide":
        return st.split(simbol, times)

    elif tipo == "select":
        idx2 = -1
        lista = []
        qt = 0
        while qt < times:
            # Começa a procurar do próximo caractere
            idx1 = st.find(simbol, idx2 + 1)
            # Começa a procurar do próximo caractere
            idx2 = st.find(simbol, idx1 + 1)
            if idx1 != -1 and idx2 != -1:
                # evitar que o caractere seja incluido na lista
                idx1 = idx1+len(simbol)
                lista.append(st[idx1:idx2])

            if idx1 == -1 or idx2 == -1:
                break
            qt += 1
        return lista


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


def editando_strings(lista_strings, desejado):

    # Convertendo a string em uma lista de caracteres para modificar individualmente
    segunda_string = list(lista_strings[1])

    # removendo apenas o que eu quero
    segunda_string.remove(desejado)

    # Substituindo a string modificada de volta na lista original
    lista_strings[1] = ''.join(segunda_string)

    print(lista_strings)

# entender em que tipo de dado a varival se encaixa


def tipo_da_string(var):

    print(var.isalnum())
    print(var.isalpha())
    print(var.isdecimal())
    print(var.isdigit())
    print(var.isascii())
    print(var.isspace())


def encontrando_complemento_em_listas(nums, target):
    numMap = {}
    n = len(nums)
    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return numMap[complement], i
        numMap[nums[i]] = i

    return []


# comparando tamplates
def comparar_formato(string, formato):
    if len(string) != len(formato):
        return False

    for char, pattern in zip(string, formato):
        # se  o caractere for igual ao padrão, continua

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


def tratamento_de_erro():  # apenas um exemplo de tratamento de erro
    while True:
        nota = input(f"digite nota: ")
        try:  # aqui e simulado
            nota = float(nota)
            if nota < 0 or nota > 10:
                raise ValueError
            break
        except ValueError:
            print("nota invalida tente novamente")


def pegar_globais():
    # Obtém o frame chamador (o ambiente de execução do script que está chamando a função)
    frame_chamador = inspect.currentframe().f_back

    # Pega o dicionário de variáveis globais do chamador
    globais = frame_chamador.f_globals

    return globais


def exe_oneof(lista):
    try:
        iten = select_iten(lista, "listas de funções:")

        _global = pegar_globais()
        funcao_exe = _global.get(iten)

        if callable(funcao_exe):  # verifica se é possivel executar
            funcao_exe()
        else:
            print(f"A função '{iten}' não foi encontrada.")
    except TypeError:
        print("verififique se passou um segundo parametro globals, deve passar uma variavel que contenha as globals()")


def listar_funcoes(arquivo):
    with open(arquivo, "r", encoding="utf-8") as file:
        codigo_fonte = file.read()  # retorna o conteudo escrito

    # Analisar a árvore sintática do código-fonte
    arvore = ast.parse(codigo_fonte)

    # Iterar pelos nós da árvore e verificar se são funções
    funcoes = [n.name for n in ast.walk(
        arvore) if isinstance(n, ast.FunctionDef)]

    return funcoes


nome_do_arquivo = "biblioteca.py"
funcoes = listar_funcoes(nome_do_arquivo)
print(funcoes)
exe_oneof(funcoes)
