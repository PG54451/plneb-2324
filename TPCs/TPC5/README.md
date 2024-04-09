# Tradução e Anotação de Texto em Python

## Introdução
Este projeto tem como objetivo realizar a tradução e anotação de um arquivo de texto utilizando Python. Para isso, utiliza-se a biblioteca `deep_translator` para traduzir termos do português para o inglês e, em seguida, anotar esses termos no texto utilizando tags HTML.

## Funcionalidades
- Tradução de termos do português para o inglês.
- Anotação de termos traduzidos em um arquivo de texto usando HTML.

## Uso
1. Execute o script Python `traducao.py` para gerar o novo json caso não esteja presente.
2. Execute o script Python `etiquetador.py` para gerar a página HTML com as etiquetas.

## Estrutura de Arquivos
- `traducao.py`: Script principal para tradução de conceitos.
- `etiquetador.py`: Script principal para etiquetar conceitos no ficheiro HTML. 
- `conceitos.json`: Arquivo JSON contendo termos em português e suas descrições.
- `conceitos_v2.json`: Arquivo JSON gerado com os termos traduzidos.
- `LIVRO-Doenças-do-Aparelho-Digestivo.txt`: Arquivo de texto a ser anotado.
- `livro.html`: Arquivo HTML com o texto anotado.

## Explicação do Código
O código é dividido em duas partes principais:

1. **Tradução de Termos:**
   - Cada termo em português e sua descrição são lidos do arquivo JSON `conceitos.json`.
   - Utilizando a API do Google Translate, os termos são traduzidos para o inglês.
   - Os termos traduzidos, juntamente com suas descrições, são armazenados em um novo arquivo JSON chamado `conceitos_v2.json`.

2. **Anotação do Texto:**
   - O texto a ser anotado é lido de um arquivo de texto.
   - Os termos traduzidos, juntamente com suas descrições, são carregados do arquivo JSON criado anteriormente.
   - Durante a anotação, uma lista de exclusão é criada contendo algumas palavras comuns que devem ser ignoradas.
   - Cada palavra encontrada no texto é verificada para determinar se está presente nos termos traduzidos.
   - Se estiver presente, a palavra é anotada com sua respectiva tradução e descrição em HTML.
   - Após a anotação de todas as palavras no texto, o texto anotado é escrito em um arquivo HTML chamado `livro.html`.
   - Essas iterações e verificações são realizadas utilizando expressões regulares para encontrar cada palavra no texto e substituí-la por uma etiqueta HTML correspondente, quando aplicável.