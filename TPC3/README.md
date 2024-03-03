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

2. **Uso do Grupo de Captura Lookahead positivo**

   O grupo de captura lookahead foi utilizado para garantir que a busca pelos elementos do dicionário fosse precisa e não incluísse mais texto do que o desejado. O padrão final `(?=\n\n|$)` no grupo lookahead, exemplo presente ao fim de uma das regex utilizadas no código, garante que a busca alcance apenas o próximo elemento do dicionário, evitando quebras de página indesejadas.

3. **Garantindo a Existência de Título sem Descrição**

   Para garantir que um elemento com título, mas sem descrição, não desformatasse a exibição, foi adicionada uma verificação no loop for que percorre os termos e suas descrições. Se uma descrição não começar com uma tag HTML, ela é encapsulada em um parágrafo para garantir a coesão visual dos elementos do dicionário no arquivo HTML final. Essa verificação foi realizada no loop for devido à dificuldade em aumentar a eficácia das expressões regulares para lidar com esse problema.


