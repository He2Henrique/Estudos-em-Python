
# para evitar mostrar uma lista vazia fiz uma função que verifica de ha alguma coisa na lista antes de executar quaquer função que necessite da lista.
def ha_itens(lista, funcao, *parametros):
    if not lista:
        print("Não há itens!")
        return
    return funcao(lista, *parametros)


# um listar simples que vai apenas mostra e enumerar os conteudos da lista
def listar(lista, title="----------elementos:"):
    print("-"*30 + "\n" + title)
    for i, e in enumerate(lista):
        print(f"{i+1}- {e}")


# e uma função que permite o usuario escolher um dos elementos para ser retornado como valor
def select_iten(lista, title1="elementos ", title2="-> "):

    listar(lista, title1)

    while True:  # utilizei um tratamento de erro para evitar entradas indesejadas
        chs = input(title2)
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
