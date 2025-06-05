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
    {"artista": "Kendrick Lamar", "titulo": "HUMBLE.", "duracao": 2.57, "pontuacao": 9.4},
    {"artista": "Kendrick Lamar", "titulo": "DNA.", "duracao": 3.05, "pontuacao": 9.3},
    {"artista": "Kendrick Lamar", "titulo": "Alright", "duracao": 3.39, "pontuacao": 9.2},
    {"artista": "Kendrick Lamar", "titulo": "King Kunta", "duracao": 3.54, "pontuacao": 9.1},{"artista": "Kendrick Lamar", "titulo": "Money Trees", "duracao": 6.25, "pontuacao": 9.0},
    {"artista": "Kendrick Lamar", "titulo": "Swimming Pools (Drank)", "duracao": 3.40, "pontuacao": 8.9},
    {"artista": "Kendrick Lamar", "titulo": "Bitch, Don't Kill My Vibe", "duracao": 5.10, "pontuacao": 8.8},
    {"artista": "Kendrick Lamar", "titulo": "The Art of Peer Pressure", "duracao": 5.48, "pontuacao": 8.7},
    {"artista": "Kendrick Lamar", "titulo": "Loyalty.", "duracao": 3.47, "pontuacao": 8.9},
    {"artista": "Kendrick Lamar", "titulo": "Pride", "duracao": 4.31, "pontuacao": 8.6},
    {"artista": "Kendrick Lamar", "titulo": "Feel", "duracao": 3.34, "pontuacao": 8.5},
    {"artista": "Kendrick Lamar", "titulo": "Element", "duracao": 3.28, "pontuacao": 8.7},
    {"artista": "Kendrick Lamar", "titulo": "XXX.", "duracao": 4.14, "pontuacao": 8.8}
]

def buscar(query):
    resultado = []
    for musica in musicas:
        if query.lower() in musica['titulo'].lower() or query.lower() in musica['artista'].lower():
            resultado.append(musica)
    return resultado

def ordenar_pontuacao(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j]["pontuacao"] < lista[j+1]["pontuacao"]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def recomendar(musica_base):
    score_musica = musica_base["pontuacao"]
    artista_musica = musica_base["artista"]
    recomendacoes = []

    for musica in musicas:
        if musica["titulo"] != musica_base["titulo"]:
            diff_score = abs(musica["pontuacao"] - score_musica)
            if diff_score <= 0.5 or musica["artista"] == artista_musica:
                recomendacoes.append(musica)

    return ordenar_pontuacao(recomendacoes)

busca = input("Digite o nome de uma música ou artista: ")

resultados = buscar(busca)

print("\n Resultado da busca (Busca Sequencial):")
if resultados:
    for m in resultados:
        print(f'{m["artista"]} - {m["titulo"]} ({m["duracao"]} min), Score: {m["pontuacao"]}')
else:
    print("Nenhuma música encontrada.")

if resultados:
    print("\n Recomendado para você:")
    recomendados = recomendar(resultados[0])
    for m in recomendados:
        print(f'{m["artista"]} - {m["titulo"]} ({m["duracao"]} min), Score: {m["pontuacao"]}')
