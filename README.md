# Novela

Este projeto tem como objetivo gerar sinopses aleatórias de novelas utilizando títulos, temas e locais pré-definidos. O script `sinopse_generator.py` seleciona esses elementos de forma aleatória e cria uma breve sinopse em português.

## Uso básico

1. Certifique-se de ter o Python 3 instalado.
2. Execute `python sinopse_generator.py` para gerar uma sinopse diretamente no terminal.
3. Caso prefira, importe a função `gerar_sinopse` em outros scripts Python.

Para rodar os testes unitários:

```bash
python -m unittest test_sinopse_generator.py
```

## Desenvolvimento futuro

- Expandir as listas de títulos, temas e locais para aumentar a variedade das sinopses.
- Permitir a customização de elementos pelo usuário.
- Explorar a criação de uma interface gráfica ou página web para facilitar o uso.
