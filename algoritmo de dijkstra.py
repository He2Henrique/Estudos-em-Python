# algoritmo para descobrir menor caminho em valor entre dois pontos.
# deve ser usado em grafos ponderados e os valores devem ser positivos.
custos = {
    "a": 0,
    "b": float("inf"),
    "c": float("inf"),
    "d": float("inf"),
    "e": float("inf"),
    "f": float("inf")
}
grafo = {}
grafo["a"] = {}
grafo["a"]["b"] = 3
grafo["a"]["c"] = 5
grafo["b"] = {}
grafo["b"]["d"] = 2
grafo["b"]["e"] = 3
grafo["c"] = {}
grafo["c"]["d"] = 1
grafo["c"]["e"] = 6
grafo["e"] = {}
grafo["d"] = {}
grafo["d"]["f"] = 2
grafo["e"]["f"] = 3
grafo["f"] = {}

pais = {}
verificados = []


def achar_menor_custo(custos):
    menor_custo = float("inf")
    node = None
    for i in custos:
        if custos[i] < menor_custo and i not in verificados:
            menor_custo = custos[i]
            node = i
    return node


node = achar_menor_custo(custos)
while node is not None:  # node que esta sendo verificado
    custo = custos[node]  # o custo para chegar no node
    visinhos = grafo[node]  # as direções que o node aponta
    for i in visinhos.keys():  # i sao os vetores
        # o custo para chegar ate o ponto é o custo para chegar ate o node e o custo do vertor que o node aponta
        new_cost = custo + visinhos[i]
        # se o custo para chegar ate ele e menor do que o custo de outro caminho então esse e o nono caminho
        if new_cost < custos[i]:
            custos[i] = new_cost  # custo para chegar ate esse ponto
            pais[i] = node  # quem era o node anterior a esse
    verificados.append(node)
    node = achar_menor_custo(custos)

print(f"{verificados} \n  {custos} \n  {pais}")
# a parti de um ponto inicial voce pode pedir a menor distancia para qualquer ponto
