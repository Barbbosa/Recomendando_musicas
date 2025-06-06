# Esta é a nossa biblioteca de músicas.
# É uma **lista** de **dicionários**, onde cada dicionário representa uma música completa.
# Cada música possui informações como 'artista', 'titulo', 'duracao' (em minutos)
# e 'pontuacao' (uma nota de avaliação).
musicas = [
    {"artista": "The Weeknd", "titulo": "Blinding Lights", "duracao": 3.20, "pontuacao": 9.5},
    {"artista": "The Weeknd", "titulo": "Save Your Tears", "duracao": 3.35, "pontuacao": 9.0},
    {"artista": "The Weeknd", "titulo": "Starboy", "duracao": 3.50, "pontuacao": 9.2},
    {"artista": "Drake", "titulo": "God's Plan", "duracao": 3.18, "pontuacao": 9.0},
    {"artista": "Kendrick Lamar", "titulo": "HUMBLE.", "duracao": 2.57, "pontuacao": 9.4},
    {"artista": "The Weeknd", "titulo": "The Hills", "duracao": 4.00, "pontuacao": 8.5},
    {"artista": "The Weeknd", "titulo": "In Your Eyes", "duracao": 3.58, "pontuacao": 8.7},
    {"artista": "The Weeknd", "titulo": "Heartless", "duracao": 3.20, "pontuacao": 8.6},
    {"artista": "The Weeknd", "titulo": "After Hours", "duracao": 6.00, "pontuacao": 8.9},
    {"artista": "The Weeknd", "titulo": "Pray For Me", "duracao": 3.38, "pontuacao": 8.4},
    {"artista": "The Weeknd", "titulo": "Earned It", "duracao": 4.10, "pontuacao": 8.3},
    {"artista": "Drake", "titulo": "Hotline Bling", "duracao": 3.50, "pontuacao": 8.8},
    {"artista": "Drake", "titulo": "In My Feelings", "duracao": 3.37, "pontuacao": 8.9},
    {"artista": "Drake", "titulo": "One Dance", "duracao": 2.54, "pontuacao": 9.2},
    {"artista": "Drake", "titulo": "Started From the Bottom", "duracao": 3.19, "pontuacao": 8.7},
    {"artista": "Drake", "titulo": "Take Care", "duracao": 4.37, "pontuacao": 9.3},
    {"artista": "Drake", "titulo": "Marvins Room", "duracao": 5.20, "pontuacao": 8.5},
    {"artista": "Drake", "titulo": "Nice For What", "duracao": 3.31, "pontuacao": 8.6},
    {"artista": "Drake", "titulo": "Nonstop", "duracao": 3.59, "pontuacao": 8.8},
    {"artista": "Drake", "titulo": "Laugh Now Cry Later", "duracao": 6.21, "pontuacao": 8.7},
    {"artista": "Kendrick Lamar", "titulo": "DNA.", "duracao": 3.05, "pontuacao": 9.3},
    {"artista": "Kendrick Lamar", "titulo": "Alright", "duracao": 3.39, "pontuacao": 9.2},
    {"artista": "Kendrick Lamar", "titulo": "King Kunta", "duracao": 3.54, "pontuacao": 9.1},
    {"artista": "Kendrick Lamar", "titulo": "Money Trees", "duracao": 6.25, "pontuacao": 9.0},
    {"artista": "Kendrick Lamar", "titulo": "Swimming Pools (Drank)", "duracao": 3.40, "pontuacao": 8.9},
    {"artista": "Kendrick Lamar", "titulo": "Bitch, Don't Kill My Vibe", "duracao": 5.10, "pontuacao": 8.8},
    {"artista": "Kendrick Lamar", "titulo": "The Art of Peer Pressure", "duracao": 5.48, "pontuacao": 8.7},
    {"artista": "Kendrick Lamar", "titulo": "Loyalty.", "duracao": 3.47, "pontuacao": 8.9},
    {"artista": "Kendrick Lamar", "titulo": "Pride", "duracao": 4.31, "pontuacao": 8.6},
    {"artista": "Kendrick Lamar", "titulo": "Feel", "duracao": 3.34, "pontuacao": 8.5},
    {"artista": "Kendrick Lamar", "titulo": "Element", "duracao": 3.28, "pontuacao": 8.7},
    {"artista": "Kendrick Lamar", "titulo": "XXX.", "duracao": 4.14, "pontuacao": 8.8}
]


# --- Funções do Sistema ---

# Esta função **busca músicas** em nossa lista principal.
# Ela verifica se o termo de busca (query) está presente no título ou no nome do artista.
def buscar_musicas(query_busca):
    """
    Busca músicas com base em uma consulta fornecida, tanto no título da música quanto no nome do artista.
    A busca não diferencia maiúsculas de minúsculas.

    Args:
        query_busca (str): O termo de busca fornecido pelo usuário.

    Returns:
        list: Uma lista de dicionários que representam as músicas que correspondem à consulta.
    """
    # Criamos uma lista vazia para armazenar as músicas que encontrarmos.
    resultados_busca = []

    # Percorremos cada 'musica' em nossa coleção 'musicas'.
    for musica in musicas:
        # Convertemos tanto a consulta quanto o título/artista para minúsculas
        # para garantir que a busca não seja sensível a maiúsculas e minúsculas.
        # Se a consulta estiver no título OU no nome do artista, adicionamos a música aos resultados.
        if query_busca.lower() in musica['titulo'].lower() or \
           query_busca.lower() in musica['artista'].lower():
            resultados_busca.append(musica)

    # Devolvemos a lista de todas as músicas que correspondem à busca.
    return resultados_busca


# Esta função **ordena uma lista de músicas** com base em sua 'pontuacao' (nota).
# Ela usa o algoritmo de **Bubble Sort** para colocar as músicas com maior pontuação primeiro.
def ordenar_por_pontuacao(lista_musicas):
    """
    Ordena uma lista de músicas em ordem decrescente com base em sua 'pontuacao'.
    Esta função usa o algoritmo Bubble Sort.

    Args:
        lista_musicas (list): Uma lista de dicionários, onde cada dicionário é uma música.

    Returns:
        list: A lista de músicas ordenada.
    """
    # Pegamos o número total de músicas na lista.
    n = len(lista_musicas)

    # O loop externo controla quantas vezes vamos "passar" pela lista.
    # A cada passagem, o maior elemento restante "flutua" para sua posição correta.
    for i in range(n):
        # O loop interno compara elementos adjacentes e os troca se estiverem na ordem errada.
        # Reduzimos o range a cada iteração, pois os últimos 'i' elementos já estarão no lugar certo.
        for j in range(0, n - i - 1):
            # Se a pontuação da música atual for menor que a da próxima música,
            # precisamos trocá-las para que a maior pontuação venha primeiro.
            if lista_musicas[j]["pontuacao"] < lista_musicas[j+1]["pontuacao"]:
                # Realiza a troca das posições dos dicionários na lista.
                lista_musicas[j], lista_musicas[j+1] = lista_musicas[j+1], lista_musicas[j]

    # Retornamos a lista de músicas agora totalmente ordenada por pontuação.
    return lista_musicas


# Esta função **recomenda músicas** com base em uma música "base" fornecida.
# As recomendações são geradas se a pontuação for próxima ou se for do mesmo artista.
def recomendar_musicas(musica_base_recomendacao):
    """
    Recomenda músicas com base em uma música "base" fornecida.
    As recomendações são feitas se:
    - A pontuação da música estiver dentro de 0.5 pontos (inclusive) da pontuação da música base, OU
    - A música for do mesmo artista que a música base.

    As recomendações são então ordenadas por pontuação em ordem decrescente.

    Args:
        musica_base_recomendacao (dict): O dicionário da música para basear as recomendações.

    Returns:
        list: Uma lista ordenada de músicas recomendadas.
    """
    # Pegamos a pontuação e o artista da música que será a base para as recomendações.
    score_base = musica_base_recomendacao["pontuacao"]
    artista_base = musica_base_recomendacao["artista"]

    # Criamos uma lista vazia para guardar as recomendações.
    lista_recomendacoes = []

    # Percorremos todas as músicas em nossa biblioteca para encontrar recomendações.
    for musica in musicas:
        # Evitamos recomendar a própria música base.
        # Verificamos se o título OU o artista são diferentes para garantir que não seja a mesma música.
        if musica["titulo"] != musica_base_recomendacao["titulo"] or \
           musica["artista"] != musica_base_recomendacao["artista"]:

            # Calculamos a diferença absoluta entre as pontuações.
            diferenca_score = abs(musica["pontuacao"] - score_base)

            # Se a diferença de pontuação for pequena (até 0.5) OU se o artista for o mesmo,
            # consideramos a música uma boa recomendação.
            if diferenca_score <= 0.5 or musica["artista"] == artista_base:
                lista_recomendacoes.append(musica)

    # Antes de retornar, ordenamos as recomendações pela pontuação, das maiores para as menores.
    return ordenar_por_pontuacao(lista_recomendacoes)


# --- Execução Principal do Programa ---
# Este é o ponto de partida do nosso script.

# Pedimos ao usuário para digitar o nome de uma música ou artista.
busca_usuario = input("Por favor, digite o nome de uma música ou um artista para buscar: ")

# Chamamos a função de busca para encontrar músicas que correspondam à entrada do usuário.
resultados_busca = buscar_musicas(busca_usuario)


# --- Exibição dos Resultados da Busca ---

# Imprimimos um cabeçalho claro para os resultados.
print("\n" + "="*30) # Linha decorativa
print("   *** Resultados da Busca ***")
print("="*30 + "\n")

# Verificamos se encontramos alguma música.
if resultados_busca:
    # Se sim, percorremos cada música encontrada e a exibimos de forma formatada.
    for musica_encontrada in resultados_busca:
        print(f"  Artista: {musica_encontrada['artista']}")
        print(f"  Título: {musica_encontrada['titulo']}")
        print(f"  Duração: {musica_encontrada['duracao']:.2f} min") # Formatado para 2 casas decimais
        print(f"  Pontuação: {musica_encontrada['pontuacao']:.1f}") # Formatado para 1 casa decimal
        print("-" * 25) # Separador entre as músicas
else:
    # Se não houver resultados, informamos o usuário.
    print("  Nenhuma música encontrada que corresponda aos seus critérios de busca.")


# --- Exibição das Recomendações ---

# Só exibimos recomendações se a busca inicial tiver encontrado pelo menos uma música.
if resultados_busca:
    print("\n" + "="*30) # Linha decorativa
    print("   *** Recomendado para Você ***")
    print("="*30 + "\n")

    # Usamos a primeira música dos resultados da busca como base para gerar recomendações.
    recomendacoes_para_usuario = recomendar_musicas(resultados_busca[0])

    # Verificamos se o sistema conseguiu gerar alguma recomendação.
    if recomendacoes_para_usuario:
        # Se sim, exibimos cada música recomendada de forma formatada.
        for musica_recomendada in recomendacoes_para_usuario:
            print(f"  Artista: {musica_recomendada['artista']}")
            print(f"  Título: {musica_recomendada['titulo']}")
            print(f"  Duração: {musica_recomendada['duracao']:.2f} min")
            print(f"  Pontuação: {musica_recomendada['pontuacao']:.1f}")
            print("-" * 25) # Separador entre as músicas
    else:
        # Se nenhuma recomendação foi encontrada com base na música selecionada, informamos o usuário.
        print("  Nenhuma recomendação pôde ser gerada com base na sua busca inicial.")

print("\n" + "="*30) # Linha final
print("       *** Fim do Programa ***")
print("="*30)
        
