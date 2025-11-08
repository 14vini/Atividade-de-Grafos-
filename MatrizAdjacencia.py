class Grafo:
    def __init__(self):
        self.vertices = []
        self.arestas = []

    # inserir e remover vértices
    def inserir_vertice(self, v):
        if v not in self.vertices:
            self.vertices.append(v)
            print(f"Vértice {v} inserido.")
        else:
            print(f"Vértice {v} já existe.")

    def remover_vertice(self, v):
        if v in self.vertices:
            self.vertices.remove(v)
            # Remove todas as arestas ligadas a esse vértice
            self.arestas = [a for a in self.arestas if v not in a]
            print(f"Vértice {v} e suas arestas removidos.")
        else:
            print(f"Vértice {v} não existe.")

    #inserir e remover arestas
    def inserir_aresta(self, u, v):
        if u in self.vertices and v in self.vertices:
            if (u, v) not in self.arestas and (v, u) not in self.arestas:
                self.arestas.append((u, v))
                print(f"Aresta ({u}, {v}) inserida.")
            else:
                print("Aresta já existe.")
        else:
            print("Um ou ambos os vértices não existem.")

    def remover_aresta(self, u, v):
        if (u, v) in self.arestas:
            self.arestas.remove((u, v))
            print(f"Aresta ({u}, {v}) removida.")
        elif (v, u) in self.arestas:
            self.arestas.remove((v, u))
            print(f"Aresta ({v}, {u}) removida.")
        else:
            print("Aresta não existe.")

    # exibir e calcular grau
    def grau_vertice(self, v):
        if v not in self.vertices:
            print(f"Vértice {v} não encontrado.")
            return
        grau = sum(1 for (a, b) in self.arestas if a == v or b == v) 
        print(f"Grau do vértice {v}: {grau}")
        return grau

    # verificar existência de aresta
    def existe_aresta(self, u, v):
        existe = (u, v) in self.arestas or (v, u) in self.arestas
        print(f"Existe aresta entre {u} e {v}? {'Sim' if existe else 'Não'}")
        return existe

    # exibir vizinhos de um vértice
    def vizinhos(self, v):
        if v not in self.vertices:
            print(f"Vértice {v} não encontrado.")
            return []
        vizinhos = []
        for (a, b) in self.arestas:
            if a == v:
                vizinhos.append(b)
            elif b == v:
                vizinhos.append(a)
        print(f"Vizinhos de {v}: {vizinhos}")
        return vizinhos
    
    # Verificar se um determinado percurso é possíve
    def percurso_possivel(self, caminho):
        for i in range(len(caminho) - 1): 
            if not self.existe_aresta(caminho[i], caminho[i+1]): 
                print("Percurso impossível.")
                return False
        print("Percurso possível!")
        return True


grafo = Grafo()


grafo.inserir_vertice(1)
grafo.inserir_vertice(2)
grafo.inserir_vertice(3)
grafo.inserir_vertice(4)

grafo.inserir_aresta(1, 2)
grafo.inserir_aresta(2, 3)
grafo.inserir_aresta(3, 4)

grafo.grau_vertice(2)
grafo.vizinhos(3)
grafo.existe_aresta(1, 3)
grafo.percurso_possivel([1, 2, 3, 4])
