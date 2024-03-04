# Melhoria das Expressões Regulares e Formatação HTML/CSS

## Objetivo da Tarefa

A proposta é utilizar expressões regulares mais robustas para capturar os elementos do dicionário de forma precisa, e também empregar HTML e CSS para melhorar a visualização do arquivo HTML resultante.

## Dificuldades Encontradas

Durante a resolução desta tarefa, enfrentei algumas dificuldades:

1. **Quebras de Página e Elemento sem descrição:**
   Uma das principais dificuldades foi garantir que a formatação dos elementos do dicionário permanecesse intacta mesmo após uma nova ocorrência de quebra de página ou existência de um elemento sem descrição. 

2. **Manutenção da Coesão dos Elementos do Dicionário:**
   Outro desafio foi manter os elementos do dicionário coesos e bem organizados no arquivo HTML. Especificamente, garantir que cada termo e sua descrição fossem exibidos em "blocos" de conteúdo, independentemente de sua formatação inicial.

## Descrição da Solução

### Melhoria das Expressões Regulares

Para resolver as dificuldades encontradas, foram realizadas as seguintes ações:

1. **Identificação dos Elementos com "@"**

   Foi utilizado o identificador "@" para marcar os elementos do dicionário. Essa marcação facilita a identificação e a extração dos termos e suas descrições durante o processamento do texto.

2. **Melhoria na Marcação das Designações**

   Utilizou-se a função `re.sub()` para adicionar o caractere "@" antes de cada designação no texto. Isso foi alcançado com o padrão `"\n\n(.+)"`, que busca por dois caracteres de quebra de linha seguidos por qualquer caractere (exceto quebras de linha) e o substitui por `"\n\n@\1"`, adicionando o "@" antes do texto capturado.

3. **Ajuste de Caracteres de Quebra de Página**

   Para corrigir a presença indesejada de caracteres de quebra de página (\f), utilizou-se novamente a função `re.sub()`. O padrão `r"(@[^\n]+)\n(\n|\f)+"` busca por uma sequência marcada com "@" seguida por caracteres que não sejam quebras de linha, seguida por uma ou mais ocorrências de uma quebra de linha seguida por uma quebra de linha ou um caractere de quebra de página (\f). Esse padrão foi substituído por `r"@\1\n"`, que mantém apenas a marcação "@" seguida pelo texto capturado e uma quebra de linha.

4. **Extração de Termos e Descrições**

   Utilizou-se a função `re.findall()` para encontrar todos os termos médicos marcados com "@" e suas respectivas descrições no texto. O padrão `r"@(.+)\n([^@]+)"` captura uma sequência marcada com "@" seguida por qualquer caractere (exceto quebras de linha) como o primeiro grupo e uma quebra de linha, seguida por qualquer caractere (exceto "@") como o segundo grupo.



