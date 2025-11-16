class GrafoListaArestas:
    def __init__(self):
        """
        Cria e retorna uma estrutura de grafo com lista de arestas e lista de vértices.

        Passos:
        1. Criar uma lista vazia chamada 'vertices'.
        2. Criar uma lista vazia chamada 'arestas', onde cada elemento será uma lista de tamanho 2 (origem, destino)
        3. Retornar vertices e arestas
        """
        self.vertices = []
        self.arestas = []

    def inserir_vertice(self, vertice):
        """
        Adiciona um novo vértice no grafo.

        Passos:
        1. Verificar se o vértice já existe em 'vertices'.
        2. Se não existir, adicionar à lista 'vertices'.
        """
        if vertice not in self.vertices:
            self.vertices.append(vertice)

    def inserir_aresta(self, origem, destino, nao_direcionado=False):
        """
        Adiciona uma aresta entre dois vértices.

        Passos:
        1. Garantir que 'origem' e 'destino' existam em 'vertices'.
            - Se não existirem, chamar 'inserir_vertice' para adicioná-los.
        2. Adicionar uma lista [origem, destino] na lista 'arestas'.
        3. Se nao_direcionado=True, adicionar também [destino, origem].
        """
        # 1. Garantir que 'origem' e 'destino' existam em 'vertices'.
        self.inserir_vertice(origem)
        self.inserir_vertice(destino)
        
        v1, v2 = sorted((origem, destino)) if nao_direcionado else (origem, destino)
        
        if (v1, v2) not in self.arestas:
            self.arestas.append((v1, v2))


    def remover_aresta(self, origem, destino, nao_direcionado=False):
        """
        Remove uma aresta entre dois vértices.

        Passos:
        1. Percorrer a lista de Arestas procurando [origem, destino]
        2. Se encontrar, remover
        3. Se nao_direcionado=True, também procurar por [destino, origem]
        """
        if (origem, destino) in self.arestas:
            self.arestas.remove((origem, destino))
            return
        
        if (destino, origem) in self.arestas:
            self.arestas.remove((destino, origem))
            return
            

    def remover_vertice(self, vertice):
        """
        Remove um vértice e todas as arestas conectadas a ele.

        Passos:
        1. Verificar se o vértice existe na lista de vertices.
        2. Caso encontrado, remover o vértice da lista 'vertices'.
        3. Percorrer a lista de 'arestas' e remover todas onde o vértice aparece
            como origem ou destino.
        """
        # 1. Verificar se o vértice existe na lista de vertices.
        if vertice not in self.vertices:
            return

        # 2. Caso encontrado, remover o vértice da lista 'vertices'.
        self.vertices.remove(vertice)
        
        # 3. Percorrer a lista de 'arestas' e remover todas onde o vértice aparece
        self.arestas = [a for a in self.arestas if vertice not in a]


    def existe_aresta(self, origem, destino):
        """
        Verifica se existe uma aresta entre origem e destino.

        Passos:
        1. Percorrer a lista de aresta procurando [origem, destino]
        2. Retornar True se encontrar
        3. Caso não encontre na lista, retornar False no final.
        """

        return (origem, destino) in self.arestas or (destino, origem) in self.arestas


    def vizinhos(self, vertice):
        """
        Retorna a lista de vizinhos (vértices alcançáveis a partir de 'vertice').

        Passos:
        1. Criar uma lista vazia chamada 'vizinhos'.
        2. Percorrer todas as arestas [origem, destino].
        3. Se origem == vertice, adicionar destino na lista de vizinhos.
        4. Retornar a lista final.
        """
        if vertice not in self.vertices:
            return []

        # 1. Criar uma lista vazia chamada 'vizinhos'.
        vizinhos_list = []
        
        # 2. Percorrer todas as arestas [origem, destino].
        for u, v in self.arestas:
            # 3. Se origem == vertice, adicionar destino na lista de vizinhos (e vice-versa para não direcionado).
            if u == vertice:
                vizinhos_list.append(v)
            elif v == vertice:
                vizinhos_list.append(u)
        
        # 4. Retornar a lista final.
        return vizinhos_list


    def grau_vertices(self):
        """
        Calcula o grau de entrada, saída e total de cada vértice.

        Passos:
        1. Criar um dicionário vazio 'graus'.
        2. Percorrer todas as arestas [origem, destino]:
            I. Se o grafo for não direcionado:
                - incrementar grau analisando apenas se origem ou destino equivale ao vértice analisado
            II. Se o grafo for direcionado
                - Se o vértice for origem Incrementar grau de saída do vértice origem
                - Se o vértice for destino incrementar grau de entrada do vértice destino.
                - Calcular o grau total (entrada + saída).
        4. Retornar o dicionário 'graus' para cada vértice.
        """
        graus = {v: {"entrada": 0, "saida": 0, "total": 0} for v in self.vertices}
        
        for u, v in self.arestas:

            if u in graus:
                graus[u]["total"] += 1
            if v in graus:
                graus[v]["total"] += 1

        for v in self.vertices:
            grau = graus[v]["total"]

            graus[v]["entrada"] = grau
            graus[v]["saida"] = grau
            
        return graus


    def percurso_valido(self, caminho):
        """
        Verifica se um percurso é possível (seguindo as arestas na ordem dada).

        Passos:
        1. Percorrer o caminho de 0 até len(caminho) - 2.
        2. Para cada par consecutivo (u, v):
            - Verificar se (u, v) existe na lista de 'arestas' (funcao existe_aresta).
            - Se alguma não existir, retornar False.
        3. Se todas existirem, retornar True.
        """
        # 1. Percorrer o caminho de 0 até len(caminho) - 2.
        for i in range(len(caminho) - 1):
            origem, destino = caminho[i], caminho[i + 1]
            
            # 2. Para cada par consecutivo (u, v):
            if not self.existe_aresta(origem, destino):
                return False
        
        # 3. Se todas existirem, retornar True.
        return True


    def listar_vizinhos(self, vertice):
        """
        Exibe os vizinhos de um vértice.

        Passos:
        1. Chamar a função vizinhos() para obter a lista.
        2. Exibir a lista formatada.
        """
        # 1. Chamar a função vizinhos() para obter a lista.
        vizinhos_list = self.vizinhos(vertice)
        
        # 2. Exibir a lista formatada.
        if vertice in self.vertices:
            print(f"Vizinhos de '{vertice}': {vizinhos_list}")
        else:
            print(f"O vértice '{vertice}' não existe.")
        
        return vizinhos_list


    def exibir_grafo(self):
        """
        Exibe todas as arestas do grafo.

        Passos:
        1. Exibir a lista de vértices.
        2. Exibir todas as arestas no formato (origem -> destino).
        """
        if not self.vertices:
            print("O grafo está vazio.")
            return

        # 1. Exibir a lista de vértices.
        print("\nVértices:", self.vertices)
        
        # 2. Exibir todas as arestas no formato (origem -> destino).
        print("Lista de Arestas:")
        for u, v in self.arestas:
            print(f"{u} -- {v}")


def criar_grafo():
    """
    Cria e retorna uma estrutura de grafo com lista de arestas e lista de vértices.

    Passos:
    1. Criar uma lista vazia chamada 'vertices'.
    2. Criar uma lista vazia chamada 'arestas', onde cada elemento será uma lista de tamanho 2 (origem, destino)
    3. Retornar vertices e arestas
    """
    return GrafoListaArestas()


def main():
    g = criar_grafo()
    
    print("Implementação (Grafo Não Direcionado)")
    
    g.inserir_vertice("A")
    g.inserir_vertice("B")
    g.inserir_vertice("C")
    g.inserir_vertice("D")
    

    g.inserir_aresta("A", "B")
    g.inserir_aresta("A", "C")
    g.inserir_aresta("B", "D")
    
    g.exibir_grafo()
    
    g.listar_vizinhos("A")
    
    graus = g.grau_vertices()
    print("\nGraus (Grafo Não Direcionado):")
    for v, info in graus.items():

         print(f"  {v}: Grau Total={info['total']}") 
         
    print(f"\nExiste aresta A - D? {g.existe_aresta('A', 'D')}")
    print(f"Percurso ['A', 'B', 'D'] é válido? {g.percurso_valido(['A', 'B', 'D'])}")
    print(f"Percurso ['A', 'D'] é válido? {g.percurso_valido(['A', 'D'])}")
    
    print("\n--- Remoção ---")
    g.remover_aresta("A", "B")
    g.remover_vertice("D")
    g.exibir_grafo()


if __name__ == "__main__":
    main()