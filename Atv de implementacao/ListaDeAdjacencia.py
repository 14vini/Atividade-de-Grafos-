class GrafoListaAdj:
    def __init__(self):
        """
        Retorna um novo grafo vazio.
        Passos:
        1. Criar um dicionário vazio: {}
        2. Retornar o dicionário (representa o grafo)
        """
        self.grafo = {}

    def inserir_vertice(self, vertice):
        """
        Insere um vértice no grafo, sem arestas iniciais.
        Passos:
        1. Verificar se 'vertice' já é chave em grafo.
        2. Se não for, criar entrada grafo[vertice] = []
        3. Se já existir, não fazer nada (ou avisar)
        """
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def inserir_aresta(self, origem, destino, nao_direcionado=False):
        """
        Adiciona aresta entre origem e destino.
        Passos:
        1. Garantir que 'origem' e 'destino' existam no grafo (inserir se necessário).
        2. adicionar destino como vizinho de origem (append).
        3. Se for Nâo Direcionado, também:
             - adicionar origem como vizinho de destino
        """
        # 1. Garantir que 'origem' e 'destino' existam no grafo (inserir se necessário).
        self.inserir_vertice(origem)
        self.inserir_vertice(destino)

        # 2. adicionar destino como vizinho de origem (append).
        if destino not in self.grafo[origem]:
            self.grafo[origem].append(destino)

        # 3. Se for Não Direcionado, também:
        #      - adicionar origem como vizinho de destino
        if nao_direcionado:
            if origem not in self.grafo[destino]:
                self.grafo[destino].append(origem)

    def vizinhos(self, vertice):
        """
        Retorna a lista de vizinhos de 'vertice'.
        Passos:
        1. Se 'vertice' estiver em grafo, retornar grafo[vertice] (lista).
        2. Se não existir, retornar lista vazia ou sinalizar erro.
        """
        # 1. Se 'vertice' estiver em grafo, retornar grafo[vertice] (lista).
        if vertice in self.grafo:
            return self.grafo[vertice]
        
        # 2. Se não existir, retornar lista vazia.
        return []

    def listar_vizinhos(self, vertice):
        """
        Função semântica: imprimir/retornar os vizinhos de 'vertice'.
        Passos:
        1. Obter lista = vizinhos(grafo, vertice)
        2. Retornar/imprimir essa lista (ou informar que o vértice não existe)
        """
        # 1. Obter lista = vizinhos(grafo, vertice)
        lista_vizinhos = self.vizinhos(vertice)

        # 2. Retornar/imprimir essa lista (ou informar que o vértice não existe)
        if vertice in self.grafo:
            print(f"Vizinhos de '{vertice}': {lista_vizinhos}")
        else:
            print(f"O vértice '{vertice}' não existe no grafo.")
        
        return lista_vizinhos

    def exibir_grafo(self):
        """
        Exibe o grafo em forma legível (lista de adjacência).
        Passos:
        1. Para cada vertice em ordem
             - imprimir: vertice -> vizinhos
        """
        if not self.grafo:
            print("O grafo está vazio.")
            return
        
        print("\nLista de Adjacência:")
        # 1. Para cada vertice em ordem - imprimir: vertice -> vizinhos
        for v, vizinhos in self.grafo.items():
            print(f"{v} -> {vizinhos}")

    def remover_aresta(self, origem, destino, nao_direcionado=False):
        """
        Remove a aresta entre origem e destino.
        Passos:
        1. Verificar se 'origem' existe; se não, terminar.
        2. Se destino estiver em grafo[origem], remover essa ocorrência.
        3. Se for não direcionado, também:
             - verificar se 'destino' existe e remover 'origem' de grafo[destino] se presente.
        """
        # 1. Verificar se 'origem' existe; se não, terminar.
        if origem not in self.grafo:
            return

        # 2. Se destino estiver em grafo[origem], remover essa ocorrência.
        if destino in self.grafo[origem]:
            self.grafo[origem].remove(destino)

        # 3. Se for não direcionado, também:
        #      - verificar se 'destino' existe e remover 'origem' de grafo[destino] se presente.
        if nao_direcionado and destino in self.grafo and origem in self.grafo[destino]:
            self.grafo[destino].remove(origem)

    def remover_vertice(self, vertice, nao_direcionado=True):
        """
        Remove um vértice e todas as arestas que o tocam.
        Passos:
        1. Verificar se 'vertice' existe em grafo; se não, terminar.
        2. Para cada outro vertice no grafo:
             - se 'vertice' estiver na lista de vizinhos, remover essa aresta.
        3. Remover o vertice do grafo
        4. Opcional: retornar confirmação/erro.
        """
        # 1. Verificar se 'vertice' existe em grafo; se não, terminar.
        if vertice not in self.grafo:
            return

        # 2. Para cada outro vertice no grafo:
        #      - se 'vertice' estiver na lista de vizinhos, remover essa aresta.
        for chave in self.grafo.keys():
            if vertice in self.grafo[chave] and chave != vertice:
                self.grafo[chave].remove(vertice)

        # 3. Remover o vertice do grafo
        del self.grafo[vertice]

    def existe_aresta(self, origem, destino):
        """
        Verifica se existe aresta direta origem -> destino.
        Passos:
        1. Verificar se 'origem' é chave no grafo.
        2. Retornar True se 'destino' estiver em grafo[origem], caso contrário False.
        """
        # 1. Verificar se 'origem' é chave no grafo.
        # 2. Retornar True se 'destino' estiver em grafo[origem], caso contrário False.
        return origem in self.grafo and destino in self.grafo[origem]

    def grau_vertices(self):
        """
        Calcula e retorna o grau (out, in, total) de cada vértice.
        Passos:
        1. Inicializar um dict de graus vazia
        2. Para cada vertice, colocar no dict uma estrutura com in, out e total zerado
        3. Para cada u em grafo:
             - out_degree[u] = tamanho de vizinhos
             - para cada v em grafo:
               - verificar se u está na lista de vizinho de v,
               - caso esteja, adicionar +1 para o grau de entrada de u
        4. Calcular o grau total somando entrada + saida
        5. Retornar uma estrutura contendo out,in,total por vértice (ex: dict de tuplas).
        """
        graus = {}
        
        # 1. e 2. Inicializar dict e para cada vertice, colocar estrutura com in, out e total zerado
        for v in self.grafo:
            graus[v] = {"entrada": 0, "saida": len(self.grafo[v]), "total": 0}

        # 3. Calcular grau de entrada (in_degree)
        for u in self.grafo:
            for v_vizinho in self.grafo[u]:
                if v_vizinho in graus:
                    graus[v_vizinho]["entrada"] += 1

        # 4. Calcular o grau total somando entrada + saida
        for v in graus:
            graus[v]["total"] = graus[v]["entrada"] + graus[v]["saida"]
            
        # 5. Retornar a estrutura
        return graus

    def percurso_valido(self, caminho):
        """
        Verifica se uma sequência específica de vértices (caminho) é válida:
        i.e., se existem arestas consecutivas entre os nós do caminho.
        Passos:
        1. Se caminho tiver tamanho < 2, retornar True (trivial).
        2. Para i de 0 até len(caminho)-2:
             - origem = caminho[i], destino = caminho[i+1]
             - se não existe_aresta(grafo, origem, destino): retornar False
        3. Se todas as arestas existirem, retornar True.
        """
        # 1. Se caminho tiver tamanho < 2, retornar True (trivial).
        if len(caminho) < 2:
            return True

        # 2. Para i de 0 até len(caminho)-2:
        for i in range(len(caminho) - 1):
            origem, destino = caminho[i], caminho[i + 1]
            
            # - se não existe_aresta(grafo, origem, destino): retornar False
            if not self.existe_aresta(origem, destino):
                return False
        
        # 3. Se todas as arestas existirem, retornar True.
        return True


def criar_grafo():
    """
    Retorna um novo grafo vazio.
    Passos:
    1. Criar um dicionário vazio: {}
    2. Retornar o dicionário (representa o grafo)
    """
    return GrafoListaAdj()

def main():
    """
    Crie um menu onde seja possível escolher qual ação deseja realizar
    ex:
         1 - Mostrar o Grafo
         2 - inserir vertice
         3 - inserir aresta
         4 - remover vértice.
         ....
    """
    g = criar_grafo()
    
    g.inserir_vertice("A")
    g.inserir_vertice("B")
    g.inserir_vertice("C")
    g.inserir_vertice("D")
    
    g.inserir_aresta("A", "B", nao_direcionado=True)
    g.inserir_aresta("A", "C")
    g.inserir_aresta("B", "D", nao_direcionado=True)
    g.inserir_aresta("D", "C")
    
    g.exibir_grafo()
    g.listar_vizinhos("A")
    
    graus = g.grau_vertices()
    print("\nGraus Calculados:")
    for v, info in graus.items():
         print(f"  {v}: Entrada={info['entrada']}, Saída={info['saida']}, Total={info['total']}")
         
    print(f"\nPercurso ['A', 'B', 'D'] é válido? {g.percurso_valido(['A', 'B', 'D'])}")
    print(f"Percurso ['D', 'C', 'B'] é válido? {g.percurso_valido(['D', 'C', 'B'])}")
    
    g.remover_aresta("A", "B", nao_direcionado=True)
    g.remover_vertice("C")
    g.exibir_grafo()


if __name__ == "__main__":
    main()