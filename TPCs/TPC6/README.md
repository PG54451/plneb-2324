# TPC6 - Criação de Página Web para Dicionário Médico

## Introdução
Este projeto tem como objetivo criar uma página web para um dicionário médico desenvolvido em Python utilizando o framework Flask. A aplicação permite aos usuários pesquisar conceitos médicos e visualizar suas descrições.

## Funcionalidades
- A aplicação permite aos usuários pesquisar conceitos médicos.
- Os usuários podem visualizar as descrições dos conceitos médicos encontrados e suas respetivas traduções para inglês.

## Uso
1. Execute o arquivo `app.py` 
2. Acesse a aplicação em seu navegador usando o endereço fornecido no terminal.

## Estrutura do Projeto
- **app.py**: Contém o código principal da aplicação Flask, incluindo as rotas e a lógica de manipulação de dados.
- **templates/**: Pasta contendo os arquivos HTML que compõem as páginas da aplicação.
- **static/css/style.css**: Arquivo CSS com estilos personalizados para a aplicação.

## Arquivos HTML
- **base.html**: Modelo base para outras páginas HTML, define a estrutura básica, como cabeçalho e navbar.
- **index.html**: Página que exibe uma lista de conceitos médicos disponíveis para pesquisa.
- **conceito.html**: Página que exibe os detalhes de um conceito médico específico.

## Arquivos CSS
- **style.css**: Contém os estilos personalizados para a aplicação, definindo a aparência geral das páginas.

## Arquivos de Dados
- **TPC6/conceitos_v2.json**: Arquivo JSON contendo os conceitos médicos, suas descrições e a tradução.

## Funcionalidades Implementadas
- Uso de compreensões de listas e dicionários para carregar e manipular os dados dos conceitos médicos a partir do arquivo JSON.
- Uso de argumentos posicionais e palavras-chave (`*args` e `**kwargs`) para lidar com a passagem de argumentos dinâmicos entre funções.

### Função `carregar_conceitos()`

1. **Abertura do Arquivo JSON:** A função abre o arquivo JSON `conceitos_v2.json` que contém os conceitos médicos e suas descrições.

2. **Carregamento dos Dados:** Utilizando a função `json.load()`, os dados do arquivo JSON são carregados para a variável `dados_json`.

3. **Compreensão de Dicionário:** Utilizando uma compreensão de dicionário, os conceitos são formatados em um novo formato. Cada conceito é representado como um dicionário contendo a chave `'conceito_pt'` para o nome do conceito em português e todas as outras chaves e valores do dicionário original.

4. **Retorno dos Conceitos:** A função retorna a lista de conceitos no novo formato.

### Rota Principal (`/`)

1. **Carregamento dos Conceitos:** A rota principal carrega os conceitos médicos chamando a função `carregar_conceitos()`.

2. **Obtenção da Pesquisa:** A rota verifica se há uma pesquisa na query string da URL. Isso é feito utilizando `request.args.get('pesquisa')`.

3. **Filtragem dos Conceitos:** Se houver uma pesquisa, a lista de conceitos é filtrada para incluir apenas os conceitos que contenham a pesquisa no nome. Isso é feito usando uma compreensão de lista.

4. **Renderização do Template HTML:** A lista filtrada de conceitos é passada para o template HTML `index.html` usando a função `render_template()`.

### Rota para um Conceito Específico (`/conceito/<string:nome>`)

1. **Carregamento dos Conceitos:** A rota carrega os conceitos médicos chamando a função `carregar_conceitos()`.

2. **Busca pelo Conceito:** Utilizando a função `next()`, a rota encontra o conceito específico com o nome passado na URL.

3. **Verificação do Conceito:** Se o conceito for encontrado, ele é renderizado no template HTML `conceito.html` usando a função `render_template()`. Caso contrário, o usuário é redirecionado de volta para a página inicial usando `redirect(url_for('index'))`.

### Passo a Passo da Execução da Aplicação

1. **Verificação do Nome do Módulo:** A condição `if __name__ == '__main__':` verifica se o script está sendo executado diretamente (não importado como um módulo).

2. **Inicialização do Servidor Flask:** Se o script estiver sendo executado diretamente, a aplicação Flask é iniciada com a opção `debug=True`, permitindo recarregamento automático do servidor e exibição de mensagens de erro detalhadas.

