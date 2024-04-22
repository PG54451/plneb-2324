# TPC7 - Desenvolvimento Web com Flask

Este é o meu TPC7 de Desenvolvimento Web com Flask. Neste projeto, desenvolvi uma aplicação web para um dicionário de conceitos médicos. A aplicação permite visualizar uma lista de conceitos médicos em uma DataTable, além de realizar pesquisas sensíveis a maiúsculas e minúsculas nesses conceitos.

## Como Executar

1. Certifique-se de ter o Python e o Flask instalados em seu ambiente de desenvolvimento.
2. Clone ou faça o download deste repositório para o seu computador.
3. Navegue até o diretório do projeto.
4. Execute a file ou o seguinte comando no terminal para iniciar o servidor Flask:

```
python app.py
```

5. Abra um navegador da web e acesse `http://localhost:4002` para visualizar a aplicação.

## Alterações na Lógica do Código

Aqui estão algumas das principais alterações na lógica do código em relação à versão anterior:

### Implementação da DataTable

- Foi adicionada uma DataTable para exibir a lista de conceitos médicos.
- Utilizei a biblioteca DataTables.js para criar uma tabela interativa e responsiva.
- Os dados da DataTable são passados para o template HTML usando a função `render_template()` do Flask.
    * aceita um argumento, que é o nome do parâmetro desejado. Se o parâmetro existir na URL, o método retorna o valor associado a ele. Se o parâmetro não existir, ele retorna `None` por padrão, a menos que um valor padrão seja fornecido como segundo argumento.

### Motor de Pesquisa

- Implementei um motor de pesquisa sensível a maiúsculas e minúsculas.
- Adicionei uma rota `/search` que lida com as pesquisas dos usuários.
- A palavra-chave da pesquisa é obtida a partir dos parâmetros da URL usando `request.args.get()`.
- Percorro todos os conceitos disponíveis e retorno os que correspondem à palavra pesquisada.

## Como Utilizar

### Acesso à Página Principal
1. Ao acessar a aplicação, você será redirecionado para a página inicial.
2. Na página inicial, encontrará o botão "Pesquisar" para acessar a página de pesquisa e o DataTable para visualizar todos os conceitos disponíveis.

### Pesquisa por Conceitos Específicos
1. Para encontrar um conceito específico, clique no botão "Pesquisar".
2. Insira a palavra-chave na barra de pesquisa.
3. Pressione Enter para iniciar a pesquisa.
4. Os resultados da pesquisa serão exibidos na página seguinte.

### Visualização dos Conceitos
1. Na página do DataTable, você pode visualizar todos os conceitos disponíveis.
2. Navegue pela tabela para encontrar informações específicas.
