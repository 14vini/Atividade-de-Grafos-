from typing import List, Tuple, Optional, Dict, Any

class Grafo:
    def __init__(self, direcionado:bool) -> None: #criar grafo
    # Cria e retorna uma matriz de adjacência vazia e uma lista de vértices.

    # Passos:
    # 1. Criar uma lista vazia chamada matriz (para armazenar as conexões).
    # 2. Criar uma lista vazia chamada vertices (para armazenar os nomes dos vértices).
    # 3. Retornar (matriz, vertices).
        self.direcionado = direcionado
        self.matriz = []
        self.vertices = []

    def inserir_vertice(self,  vertice:str):
        """
        Adiciona um novo vértice ao grafo.

        Passos:
        1. Verificar se o vértice já existe em 'vertices'.
        2. Caso não exista:
            - Adicionar o vértice à lista 'vertices'.
            - Aumentar o tamanho da matriz:
                a) Para cada linha existente, adicionar um valor 0 no final (nova coluna).
                b) Adicionar uma nova linha com zeros do tamanho atualizado.
        """
        if vertice in self.vertices:
            return True
        
        self.vertices.append(vertice)
        for linha in self.matriz:
            linha.append(0)

        nova_linha = []
        for i in range(len(self.vertices)):
            nova_linha.append(0)

        self.matriz.append(nova_linha)

    def inserir_aresta(self, origem, destino):
        """
        Adiciona uma aresta entre dois vértices.

        Passos:
        1. Garantir que 'origem' e 'destino' existam em 'vertices':
            - Se não existirem, chamar 'inserir_vertice' para adicioná-los.
        2. Localizar o índice da origem (i) e do destino (j).
        3. Marcar a conexão na matriz: matriz[i][j] = 1.
        4. Se nao_direcionado=True, também marcar a conexão inversa matriz[j][i] = 1.
        """
        if origem not in self.vertices:
            self.inserir_vertice(origem)
        if destino not in self.vertices:
            self.inserir_vertice(destino)
        
        i_origem = self.vertices.index(origem)
        i_destino = self.vertices.index(destino)

        self.matriz[i_origem][i_destino] = 1

        if not self.direcionado:
            self.matriz[i_destino][i_origem] = 1

    def remover_vertice(self, vertice):
        """
        Remove um vértice e todas as arestas associadas.

        Passos:
        1. Verificar se o vértice existe em 'vertices'.
        2. Caso exista:
            - Descobrir o índice correspondente (usando vertices.index(vertice)).
            - Remover a linha da matriz na posição desse índice.
            - Remover a coluna (mesmo índice) de todas as outras linhas.
            - Remover o vértice da lista 'vertices'.
        """
        i = self.vertices.index(vertice)
        del self.matriz[i]
        for linha in self.matriz:
            del linha[i]

    def remover_aresta(self,origem, destino):
        """
        Remove uma aresta entre dois vértices.

        Passos:
        1. Verificar se ambos os vértices existem.
        2. Localizar os índices (i e j).
        3. Remover a aresta: matriz[i][j] = 0.
        4. Se nao_direcionado=True, também remover a inversa: matriz[j][i] = 0.
        """
        if origem not in self.vertices or destino not in self.vertices:
            return

        i_origem = self.vertices.index(origem)
        i_destino = self.vertices.index(destino)
        self.matriz[i_origem][i_destino] = 0

        if not self.direcionado:
            self.matriz[i_destino][i_origem] = 0

    def existe_aresta(self, origem, destino) -> bool:
        """
        Verifica se existe uma aresta direta entre dois vértices.

        Passos:
        1. Verificar se ambos os vértices existem em 'vertices'.
        2. Obter os índices (i, j).
        3. Retornar True se matriz[i][j] == 1, caso contrário False.
        """
        if origem not in self.vertices or destino not in self.vertices:
            return False
        
        i_origem = self.vertices.index(origem)
        i_destino = self.vertices.index(destino)

        existe = self.matriz[i_origem][i_destino] == 1 
        return existe
        
    def vizinhos(self, vertice):
        """
        Retorna a lista de vizinhos (vértices alcançáveis a partir de 'vertice').

        Passos:
        1. Verificar se 'vertice' existe em 'vertices'.
        2. Obter o índice 'i' correspondente.
        3. Criar uma lista de vizinhos vazia
        4. Para cada item da linha matriz[i], verificar se == 1
            - Adicionar o vértice correspondente na lista de vizinhos
        5. Retornar essa lista.
        """
        if vertice not in self.vertices:
            return []
        
        vizinhos = []
        i = self.vertices.index(vertice)
        linha_vizinhos = self.matriz[i]
        
        # Percorrer a linha 'i' para encontrar as saídas
        for j, conexao in enumerate(linha_vizinhos):
            if conexao == 1:
                vizinhos.append(self.vertices[j])

        return sorted(vizinhos)

    def entradas(self, vertice): 
        if vertice not in self.vertices:
            return []
        j = self.vertices.index(vertice)
        coluna = []
        for v in self.matriz:
            coluna.append(v[j])
        return coluna

    def grau_vertices(self):
        """
        Calcula o grau de entrada, saída e total de cada vértice.

        Passos:
        1. Criar um dicionário vazio 'graus'.
        2. Para cada vértice i:
            - Se o grafo for direcionado:
                - Grau de saída: somar os valores da linha i.
                - Grau de entrada: somar os valores da coluna i.
                - Grau total = entrada + saída.
            - Se não:
                - calcular apenas o grau de saida ou entrada
        3. Armazenar no dicionário no formato:
            graus[vértice] = {"saida": x, "entrada": y, "total": z} ou graus[vértice] = x.
        4. Retornar 'graus'.
        """
        graus = {}
        if self.direcionado:
            for index_vertice in range(len(self.vertices)):
                v = self.vertices[index_vertice]
                saida = sum(self.matriz[index_vertice])
                entrada = sum(self.entradas(v))
                graus[v] = {
                    "saida": saida,
                    "entrada": entrada,
                    "total": saida + entrada,
                }
        else: #nao direcionado
            for index_vertice in range(len(self.vertices)):
                v = self.vertices[index_vertice]
                saida = sum(self.matriz[index_vertice])
                graus[v] = saida

        return graus

    def percurso_valido(self, caminho):
        """
        Verifica se um percurso (sequência de vértices) é possível no grafo.

        Passos:
        1. Percorrer a lista 'caminho' de forma sequencial (de 0 até len-2).
        2. Para cada par consecutivo (u, v):
            - Verificar se existe_aresta(matriz, vertices, u, v) é True.
            - Se alguma não existir, retornar False.
        3. Se todas existirem, retornar True.
        """
        for i in range(len(caminho)-2):
            if not self.existe_aresta(caminho[i], caminho[i+1]):
                return False
        return True

    def listar_vizinhos(self, vertice):
        """
        Exibe (ou retorna) os vizinhos de um vértice.

        Passos:
        1. Verificar se o vértice existe.
        2. Chamar a função vizinhos() para obter a lista.
        3. Exibir a lista formatada (ex: print(f"Vizinhos de {v}: {lista}")).
        """
        if vertice not in self.vertices:
            return []
        print(f"Vizinhos de {vertice}: {self.vizinhos(vertice)}")

    def exibir_grafo(self):
        """
        Exibe o grafo em formato de matriz de adjacência.

        Passos:
        1. Exibir cabeçalho com o nome dos vértices.
        2. Para cada linha i:
            - Mostrar o nome do vértice.
            - Mostrar os valores da linha (0 ou 1) separados por espaço.
        """
        print("  " + " ".join(self.vertices))
        for i in self.matriz:
            print(self.vertices[self.matriz.index(i)] +" " + " ".join([str(x) for x in i]))

    def bfs(self, inicio: str = None) -> List[str]:
        """
        Implementa a Busca em Largura (BFS) a partir de um vértice inicial.

        Passos:
        1. Inserir o vértice inicial na fila.
        2. Iniciar a lista de visitados (ou set) vazia.
        3. Enquanto a fila não estiver vazia:
            a. Retirar o primeiro vértice da fila.
            b. Marcar vértice como visitado.
            c. Obter os vizinhos do vértice.
            d. Para cada vizinho:
                i. Verificar se o vizinho já não foi visitado.
                ii. Adicionar o vizinho na Fila.
        4. Retornar Visitados.
        """
        if not self.vertices: return []
        
        # define o vértice inicial, se não for fornecido, usa o primeiro da lista
        start_node = inicio if inicio in self.vertices else self.vertices[0]
        
        fila: List[str] = [start_node]
        visitados: set[str] = {start_node}
        ordem_visitados: List[str] = [start_node]

        while fila:
            # a. Retirar o primeiro vértice da fila (FIFO)
            vertice_atual = fila.pop(0)

            # c. Obter os vizinhos do vértice (já ordenados pela função vizinhos)
            for vizinho in self.vizinhos(vertice_atual):
                # i. Verificar se o vizinho já não foi visitado
                if vizinho not in visitados:
                    # ii. Adicionar o vizinho na Fila e marcar como visitado
                    visitados.add(vizinho)
                    fila.append(vizinho)
                    ordem_visitados.append(vizinho)
        
        # 4. Retornar Visitados
        return ordem_visitados

    def menorCaminho(self, inicio: str, destino: str) -> Optional[List[str]]:
        """
        Utiliza BFS para encontrar o menor caminho (em número de arestas) entre dois vértices.

        Passos:
        1. Inserir a estrutura {vertice, caminho} na fila.
        2. Iniciar a lista de visitados vazia.
        3. Enquanto a fila não estiver vazia:
            a. Retirar o primeiro item da fila.
            b. Verificar se o vértice é o destino.
                i. Retornar o caminho.
            c. Marcar vértice como visitado.
            d. Obter os vizinhos.
            e. Para cada vizinho:
                i. Verificar se o vizinho já não foi visitado.
                ii. Adicionar estrutura com vizinho e caminho atualizado na Fila.
        4. Retornar vazio se não encontrar.
        """
        if inicio not in self.vertices or destino not in self.vertices:
            return None
        
        # a fila armazena a estrutura: {'vertice': 'V', 'caminho': ['A', 'C', 'V']}
        fila: List[Dict[str, Any]] = [{'vertice': inicio, 'caminho': [inicio]}]
        visitados: set[str] = {inicio}

        while fila:
            # a. Retirar o primeiro item da fila (FIFO)
            item_atual = fila.pop(0)
            vertice_atual = item_atual['vertice']
            caminho_atual = item_atual['caminho']

            # b. Verificar se o vértice do item retirado é o destino
            if vertice_atual == destino:
                # i. Retornar o caminho caso seja
                return caminho_atual
            
            # d. Obter os vizinhos do vértice
            for vizinho in self.vizinhos(vertice_atual):
                # i. Verificar se o vizinho já não foi visitado
                if vizinho not in visitados:
                    # O BFS garante o menor caminho. Marcar como visitado.
                    visitados.add(vizinho)
                    
                    # ii. Adicionar estrutura com vizinho e caminho atualizado na Fila
                    novo_caminho = caminho_atual + [vizinho]
                    fila.append({'vertice': vizinho, 'caminho': novo_caminho})

        # 4. Retornar vazio
        return None


# Criação do grafo da Atividade 1 (não direcionado)
g = Grafo(direcionado=False)

# Inserção de arestas (V1--V2, V1--V6, V2--V3, V2--V4, V2--V6, V2--V7, V4--V5, V5--V6, V5--V8, V6--V7, V7--V8)
arestas = [
    ("V1", "V2"), ("V1", "V6"),
    ("V2", "V3"), ("V2", "V4"), ("V2", "V7"),
    ("V4", "V5"),
    ("V5", "V8"),
    ("V6", "V7")
]

 # inserindo mais arestas
g.inserir_aresta("V2", "V6")
g.inserir_aresta("V5", "V6")
g.inserir_aresta("V7", "V8")


for u, v in arestas:
    g.inserir_aresta(u, v)

print("--- Exercicio 1 ---".upper())
ordem_visitados = g.bfs("V1")
print(f"Ordem de visita BFS (a partir de V1): {ordem_visitados}")

print("\n--- exercicio 2  --".upper())

inicio = "V1"
destino = "V8"
caminho = g.menorCaminho(inicio, destino)
print(f"Menor caminho de {inicio} para {destino}: {caminho}")

inicio = "V3"
destino = "V5"
caminho = g.menorCaminho(inicio, destino)
print(f"Menor caminho de {inicio} para {destino}: {caminho}")

