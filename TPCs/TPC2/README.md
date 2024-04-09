# Minha Resolução do TPC2 - Exercícios com Expressões Regulares em Python

Durante a realização dos exercícios, explorei diversos métodos oferecidos pela biblioteca padrão do Python para trabalhar com expressões regulares. Além disso, utilizei flags, que são comumente utilizadas para modificar o comportamento das operações de correspondência. Essas flags permitem ajustar a forma como as expressões regulares são interpretadas ou processadas, adicionando funcionalidades adicionais ou alterando a forma como certos padrões são tratados.

## Métodos Utilizados:

- **findall:** Este método retorna todas as ocorrências de um padrão em uma string.
- **sub:** Este método substitui todas as ocorrências de um padrão em uma string por outro texto.
- **split:** Este método divide uma string em substrings com base em um padrão e retorna uma lista das substrings resultantes.
- **IGNORECASE:** Esta flag é utilizada para tornar a expressão regular insensível a maiúsculas e minúsculas.

## Dificuldades Encontradas:

Um dos exercícios que apresentou maior dificuldade foi o Exercício 10. Nele, precisei percorrer uma lista, ao invés de uma string, de códigos postais para criar pares separados por hífen para cada elemento da lista.

Ao manipular listas, tinha como comum a utilização do método `append`. No contexto do Exercício 10, optei pelo uso do método `extend` após não chegar a solução desejada com o método mais familiar. 

Utilizando `append`, cada par de códigos postais divididos foi adicionado como um elemento individual à lista de pares. Isso resultaria em uma estrutura de lista aninhada, onde cada par seria uma lista dentro de outra lista. Por outro lado, utilizando `extend`, cada par de códigos postais seria adicionado como elementos individuais à lista de pares, mantendo a estrutura plana da lista.

Portanto, preferi o uso do método `extend`, pois ele permite adicionar múltiplos elementos de uma lista a outra lista, mantendo a estrutura correta para representar os pares de códigos postais. Isso facilita a manipulação e processamento dos dados, garantindo a precisão e clareza dos resultados.
