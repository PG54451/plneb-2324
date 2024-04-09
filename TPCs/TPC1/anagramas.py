filename = "../../data/CIH Bilingual Medical Glossary English-Spanish.txt"

file = open(filename)
text = file.read()

# Remover pontuação
text = text.replace("."," ")
text = text.replace(","," ")
text = text.replace("-"," ")
# ...

text = text.lower()

# Dividir o texto por tokens
anagramas = {}
tokens = text.split()

# remover repetidos
tokens_unicos = list(set(tokens))

for token in tokens_unicos:
    token_ordenado = ''.join(sorted(token))
    if token_ordenado in anagramas:
        anagramas[token_ordenado].append(token)
    else:
        anagramas[token_ordenado] = [token]


for chave, valor in anagramas.items():
    if len(valor) > 1:
        anagramas[chave] = valor
