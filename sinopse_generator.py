# -*- coding: utf-8 -*-
import random

temas = [
    "fé", "vingança", "perdão", "ambição", "segredos de família", "amor proibido",
    "conversão religiosa", "mundo gospel", "sucesso e queda", "dupla identidade"
]

locais = [
    "sertão nordestino", "subúrbio do Rio de Janeiro", "bairro evangélico de São Paulo",
    "cidade fictícia envolta em mistérios", "vilarejo à beira-mar", "favela carioca"
]

titulos = [
    "A Promessa", "Entre a Cruz e o Pecado", "Luz do Sertão", "Terra de Milagres",
    "Caminhos de Ester", "Flor de Fé", "O Último Culto"
]

def gerar_sinopse():
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

if __name__ == "__main__":
    novela = gerar_sinopse()
    print("🎬 TÍTULO:", novela["título"])
    print("📌 TEMA:", novela["tema"])
    print("📍 LOCAL:", novela["local"])
    print("\n📝 SINOPSE:", novela["sinopse"])
