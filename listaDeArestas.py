class GrafoListaArestas:
    def __init__(self):
        self.vertices = []
        self.arestas = []

    # adiciona e remove vértices
    def inserir_vertice(self, v):
        if v in self.vertices:
            print(f"O vértice '{v}' já existe.")
            return
        self.vertices.append(v)
        print(f"Vértice '{v}' adicionado com sucesso.")

    def remover_vertice(self, v):
        if v not in self.vertices:
            print(f"O vértice '{v}' não foi encontrado.")
            return
        self.vertices.remove(v)
        
        self.arestas = [a for a in self.arestas if v not in a]
        print(f"Vértice '{v}' e suas arestas foram removidos.")

    # adiciona e remove arestas
    def inserir_aresta(self, v1, v2):
        if v1 not in self.vertices or v2 not in self.vertices:
            print("Um ou ambos os vértices não existem.")
            return
        if (v1, v2) in self.arestas or (v2, v1) in self.arestas:
            print(f"Aresta entre '{v1}' e '{v2}' já existe.")
            return
        self.arestas.append((v1, v2))
        print(f"Aresta entre '{v1}' e '{v2}' adicionada.")

    def remover_aresta(self, v1, v2):
        if (v1, v2) in self.arestas:
            self.arestas.remove((v1, v2))
        elif (v2, v1) in self.arestas:
            self.arestas.remove((v2, v1))
        else:
            print(f"Aresta entre '{v1}' e '{v2}' não existe.")
            return
        print(f"Aresta entre '{v1}' e '{v2}' removida.")

    # exibe o grafo e informações sobre os vértices
    def exibir(self):
        print("\nLista de Arestas:")
        for a in self.arestas:
            print(f"{a[0]} -- {a[1]}")
        print("Vértices:", self.vertices)

    def grau_vertices(self):
        print("\nGrau de cada vértice:")
        for v in self.vertices:
            grau = sum(1 for a in self.arestas if v in a)
            print(f"{v}: {grau}")

    # verifica se há uma ligação entre dois vértices
    def existe_aresta(self, v1, v2):
        return (v1, v2) in self.arestas or (v2, v1) in self.arestas

    # lista os vizinhos de um vértice
    def vizinhos(self, v):
        if v not in self.vertices:
            print(f"O vértice '{v}' não existe.")
            return
        vizinhos = []
        for a in self.arestas:
            if a[0] == v:
                vizinhos.append(a[1])
            elif a[1] == v:
                vizinhos.append(a[0])
        print(f"Vizinhos de '{v}': {vizinhos}")

    # verifica se o percurso informado é possível
    def percurso_possivel(self, caminho):
        for i in range(len(caminho) - 1):
            if not self.existe_aresta(caminho[i], caminho[i + 1]):
                print(f"Percurso impossível: não há ligação entre {caminho[i]} e {caminho[i + 1]}")
                return False
        print(f"Percurso {caminho} é possível!")
        return True


g = GrafoListaArestas()

g.inserir_vertice("A")
g.inserir_vertice("B")
g.inserir_vertice("C")
g.inserir_vertice("D")

g.inserir_aresta("A", "B")
g.inserir_aresta("A", "C")
g.inserir_aresta("B", "D")

g.exibir()
g.grau_vertices()
g.vizinhos("A")

print("\nExiste aresta A - D?", g.existe_aresta("A", "D"))
print("Existe aresta B - D?", g.existe_aresta("B", "D"))

g.percurso_possivel(["A", "B", "D"])
g.percurso_possivel(["A", "D"])