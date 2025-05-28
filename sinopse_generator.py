import random

# Listas de temas, locais e títulos
temas = [
    "fé", "vingança", "perdão", "ambição", "conversão religiosa", "mundo gospel"
]
locais = [
    "sertão nordestino", "subúrbio carioca", "bairro evangélico de São Paulo",
    "cidade fictícia envolta em mistério"
]
titulos = [
    "A Promessa", "Entre a Cruz e o Pecado", "Caminhos de Ester", "Flor de Fé",
    "Terra de Milagres"
]

def gerar_sinopse():
    """
    Gera uma sinopse de novela aleatória com título, tema e local.
    Retorna um dicionário com as chaves: 'título', 'tema', 'local' e 'sinopse'.
    """
    titulo = random.choice(titulos)
    tema = random.choice(temas)
    local = random.choice(locais)

    trama = f"Em {local}, uma história marcada por {tema} transforma vidas. " \
            f"{titulo} acompanha personagens em conflito entre fé e destino, com segredos que mudarão tudo."

    return {
        "título": titulo,
        "tema": tema,
        "local": local,
        "sinopse": trama
    }

def gerar_varias_sinopses(qtd=1):
    """
    Gera uma lista com várias sinopses de novelas.
    Parâmetro:
    - qtd: número de sinopses a serem geradas (padrão = 1)
    
    Retorna uma lista de dicionários com sinopses.
    """
    return [gerar_sinopse() for _ in range(qtd)]
