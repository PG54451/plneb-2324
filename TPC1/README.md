# Dificuldade na Resolução do Exercício

Durante a resolução do exercício, a principal dificuldade encontrada foi entender o uso correto das funções `sort()` e `sorted()` em Python, especialmente em relação à concatenação dos elementos de uma lista ordenada em uma única string.

## Descrição do Problema

O problema consistia em encontrar anagramas em um texto fornecido, onde as palavras são consideradas anagramas se possuírem exatamente as mesmas letras, independentemente da ordem das letras.

## Solução

A solução para encontrar anagramas envolveu a ordenação alfabética das letras de cada palavra e, em seguida, a concatenação dessas letras ordenadas em uma única string. Isso permitiu agrupar palavras anagramas sob as mesmas chaves em um dicionário. Além disso, foi necessário garantir que após o primeiro loop o dicionário só contenha elementos que possuam algum anagrama.

## Dificuldades Encontradas

A dificuldade surgiu da confusão inicial no uso das funções `sort()` e `sorted()`. Ambas as funções são usadas para ordenar elementos, mas com diferenças significativas:
- `sorted()` é uma função que retorna uma nova lista ordenada, enquanto mantém a lista original inalterada.
- `sort()` é um método que ordena a lista original in-place, ou seja, altera a lista original e não retorna nada.

Inicialmente, houve confusão sobre qual função usar para ordenar os caracteres de um token e concatená-los em uma única string. Isso levou a uma investigação sobre a diferença entre as duas funções e a forma correta de aplicá-las no contexto do problema.

Outra dificuldade enfrentada foi garantir que o dicionário de anagramas só contivesse palavras que possuíssem pelo menos um anagrama. Isso exigiu um processo adicional de verificação após a criação do dicionário, removendo as entradas que continham apenas uma palavra. 

## Resolução das Dificuldades

Após pesquisa e experimentação, ficou claro que a função `sorted()` era a escolha correta para criar uma nova lista ordenada de caracteres a partir de um token. Em seguida, foi possível utilizar o método `join()` para concatenar os caracteres ordenados em uma única string.

## Conclusão

Apesar da confusão inicial no uso das funções `sort()` e `sorted()`, a compreensão das diferenças entre elas e a forma correta de aplicá-las foram fundamentais para a resolução bem-sucedida do exercício. Isso destacou a importância de compreender os detalhes sutis das funções em Python para resolver eficientemente problemas de programação.

