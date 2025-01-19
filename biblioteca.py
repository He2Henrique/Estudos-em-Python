
import re
import ast
import inspect
from manipulando_listas import *


def spliter(st, simbol, tipo, times=float('inf')):
    # ele recebe de entrada a string, o simbulo e o tipo de slipter e a quantidade de vezes que que queres dividir ou recortar

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


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    # o desafio se trata dizer se duas strings sao um anagrama ou nao
    if len(s) != len(t):  # logo de primeira se as strings comparadas não possuirem o mesmo tamanho então não são anagramas
        return False

    # cria uma lista de 26 zeros, o que siguinifica que ele marca a diferença entre "a" ate "z"
    freq = [0] * 26

    for i in range(len(s)):
        # seleciona o caracter na string e tranforma em seu respectivo valor na tabela ascii
        # e subtrai do valor da tabela ascii a valor de "a" para saber a posição do caracter na lista
        freq[ord(s[i]) - ord('a')] += 1
        # ao marcar a posição a segunda string tambem ira marcar a posição na lista porem com valor inverso
        # as marcações iram se anular se ambas forem iguais.
        freq[ord(t[i]) - ord('a')] -= 1

        # agora voce pode se pergutar porque não utilizar map o motivo é que o codigo ficaria muito mais ilegivel e grande.

    for i in range(len(freq)):
        if freq[i] != 0:
            return False
        # tambem seria possivel usar a função sum mas pense comigo o quanto enviavel seria isso. a função sum deve passar por todos os elementos.
        #  ja a sintaxe que atribui ao encontrar o primeiro elemento que nao seja zero siguinifica que a um caracter divergente portanto não é um anagrama.
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
