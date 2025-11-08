class GrafoListaAdj:
    def __init__(self):
        self.grafo = {}

    # Inserir e remover vértices
    def inserir_vertice(self, v):
        if v in self.grafo:
            print(f"O vértice '{v}' já existe.")
            return
        self.grafo[v] = []
        print(f"Vértice '{v}' adicionado com sucesso.")

    def remover_vertice(self, v):
        if v not in self.grafo:
            print(f"O vértice '{v}' não existe.")
            return

        for chave in list(self.grafo.keys()):
            if v in self.grafo[chave]:
                self.grafo[chave].remove(v)

        del self.grafo[v]
        print(f"Vértice '{v}' e suas arestas foram removidos.")

    # Inserir e remover arestas
    def inserir_aresta(self, origem, destino, nao_direcionado=False):
        if origem not in self.grafo or destino not in self.grafo:
            print("Um ou ambos os vértices não existem.")
            return

        if destino not in self.grafo[origem]:
            self.grafo[origem].append(destino)
            print(f"Aresta {origem} -> {destino} criada.")
        else:
            print(f"Aresta {origem} -> {destino} já existe.")

        if nao_direcionado and origem not in self.grafo[destino]:
            self.grafo[destino].append(origem)
            print(f"Aresta {destino} -> {origem} criada (não direcionado).")

    def remover_aresta(self, origem, destino, nao_direcionado=False):
        if origem not in self.grafo:
            print(f"Origem '{origem}' não existe.")
            return

        if destino in self.grafo[origem]:
            self.grafo[origem].remove(destino)
            print(f"Aresta {origem} -> {destino} removida.")
        else:
            print(f"Aresta {origem} -> {destino} não existe.")

        if nao_direcionado and destino in self.grafo and origem in self.grafo[destino]:
            self.grafo[destino].remove(origem)
            print(f"Aresta {destino} -> {origem} removida (não direcionado).")

    # Exibir o grafo
    def exibir(self):
        if not self.grafo:
            print("O grafo está vazio.")
            return
        print("\nLista de Adjacência:")
        for v, vizinhos in self.grafo.items():
            print(f"{v} -> {vizinhos}")

    # Listar vizinhos
    def vizinhos(self, v):
        if v not in self.grafo:
            print(f"O vértice '{v}' não existe.")
            return
        print(f"Vizinhos de '{v}': {self.grafo[v]}")

    # Verificar se uma aresta existe
    def existe_aresta(self, origem, destino):
        return origem in self.grafo and destino in self.grafo[origem]

    # Calcular graus dos vértices
    def grau_vertices(self):
        print("\nGrau de cada vértice:")
        graus = {}
        for v in self.grafo:
            graus[v] = {"entrada": 0, "saida": len(self.grafo[v]), "total": 0}

        for u in self.grafo:
            for v in self.grafo[u]:
                if v in graus:
                    graus[v]["entrada"] += 1

        for v in graus:
            graus[v]["total"] = graus[v]["entrada"] + graus[v]["saida"]
            print(f"{v}: entrada={graus[v]['entrada']}, saída={graus[v]['saida']}, total={graus[v]['total']}")

    # Verificar se um percurso é possível
    def percurso_possivel(self, caminho):
        if len(caminho) < 2:
            print("O percurso precisa ter pelo menos dois vértices.")
            return False

        for i in range(len(caminho) - 1):
            o, d = caminho[i], caminho[i + 1]
            if not self.existe_aresta(o, d):
                print(f"Percurso impossível: não há ligação entre {o} e {d}")
                return False
        print(f"Percurso {caminho} é possível!")
        return True


# Exemplo de uso

g = GrafoListaAdj()

g.inserir_vertice("A")
g.inserir_vertice("B")
g.inserir_vertice("C")
g.inserir_vertice("D")

g.inserir_aresta("A", "B", nao_direcionado=True)
g.inserir_aresta("A", "C")
g.inserir_aresta("B", "D", nao_direcionado=True)

g.exibir()
g.vizinhos("A")
g.grau_vertices()

print("\nExiste aresta A -> D?", g.existe_aresta("A", "D"))
print("Existe aresta B -> D?", g.existe_aresta("B", "D"))

g.percurso_possivel(["A", "B", "D"])
g.percurso_possivel(["A", "D"])