import re
import json


def main():
    xml=open('glossario_ministerio_saude.xml','r', encoding='utf8')
    resultado = str(xml.read())
    
    # Remoções manuais
    # Eliminar linhas até o início das Siglas
    # Eliminar desde final de siglas até início das definições
    # Remoção da página 107 (fim de definições) até ao final do pdf

    resultado = re.sub(r'<fontspec.*?>', r'', resultado)# Remover tags de fontspec
    resultado = re.sub(r'<image.*?>', r'', resultado)# Remover tags de imagens
    resultado = re.sub(r'\s?\n', r'\n', resultado)# Remover espaços vazios
    resultado = re.sub(r'\n+', r'\n', resultado)# Remover parágrafos deixados por espaços vazios
    resultado = re.sub(r'<page.+?>\n<\/page>', r'', resultado)# Remover páginas sem conteúdo

    # Siglas - estas necessitam de uma preparação diferente, logo é necessário adicioná-las a uma variável que será 
    # posteriormente alterada, para isto usou-se o findall pois é a única função regex que devolve o resultado, mas
    # como era necessário passar por várias linhas deve-se fazer uma condição OU \n ou ., então usou-se um grupo de 
    # não captura para afirmar estes, o resultado final é uma lista de um único valor, logo escolheu-se a posição inicial deste
    siglas = re.findall(r'<page number="5".+?>(?:\n|.)*?<page number="9".+?>(?:\n|.)*?</page>', resultado)[0]
    siglas = re.sub(r'<text.+?>[0-9]</text>|<\/?page.*?>|<\/?text.*?>|<b>Siglas<\/b>', r'', siglas)# Remover numero de página e tags e o título Siglas
    siglas = re.sub(r'<b>', r'@<b>', siglas)# Marcador de início de definição
    siglas = re.sub(r'<b>|<\/b>|\n', r'', siglas)# Remoção das tags bold
    siglas = re.split(r'@', siglas)
    siglas.pop(0)# string vazia

    sigla, definicao = [], []

    # Guardar as siglas e respetivas definições num dicionário
    for i in siglas:
        index = i.index('–')
        sigla.append(i[:index-1])
        definicao.append(i[index+2:])
    siglas_dict = { sigla: definicao for sigla, definicao in zip(sigla, definicao)}
    dicionario = {'Siglas': siglas_dict}

    # Glossário
    resultado = re.sub(r'<page number="5".+?>(\n|.)*<page number="9".+?>(\n|.)*?</page>', r'', resultado)# Remoção das Siglas do código principal
    resultado = re.sub(r'<text.*?top="2..".*?>.*?<\/text>', r'', resultado)# Remover informação no topo das páginas
    resultado = re.sub(r'<\/?page.*?>',r'', resultado)# Remover tags de páginas
    resultado = re.sub(r'-<',r'<', resultado)# Remover traços de continuação de frase
    resultado = re.sub(r'<text.*?(width=".+?").*?>',r'<text \1>', resultado)# Remover tags de texto
    resultado = re.sub(r'\n+',r'\n', resultado)# Remover espaços entre diferentes linhas
    resultado = re.sub(r'<b>epidemiologia<\/b>',r'Epidemiologia', resultado)# Encontrado erro, epidemiologia em Notiﬁcação de doenças está a negrito e em minúsculas
    resultado = re.sub(r'<i>Categoria</i>\n:? ',r'<i>Categoria: </i>\n', resultado)# Encontrado erro, má formatação de categoria
    resultado = re.sub(r'<i>(<b>.+?<\/b>)<\/i>', r'\1', resultado)# Remover casos de palavras em bold e itálico
    resultado = re.sub(r'<text.+?><b>(.+?)>', r'§@<b>\1>', resultado)# Criar marcador de termos
    resultado = re.sub(r'</b></text>\n§@<b>', r'', resultado)# Unir continuação de termos em diferentes linhas
    resultado = re.sub(r'<\/?i>', r'', resultado)# Remover tags italico
    resultado = re.sub(r'(<text.+?width="(?:229|2[3-9][0-9]).+)', r'&\1', resultado)# Se tem width> 228, então é descrição, logo é uma categoria
    resultado = re.sub(r'(<text.+?>.+\n§@<b>)', r'&\1', resultado)# Se está antes de outro termo é descrição
    resultado = re.sub(r'<\/?b>', r'', resultado)# Remover tags de bold
    resultado = re.sub(r'(@.+?\n)(&+<.+?Ver.+)', r'\1#None\n\2', resultado)# Adicionar NA a termos sem categoria
    resultado = re.sub(r'(§@Zalcitabina.+>\n)(.+)', r'\1#None\n&\2', resultado)# Caso específico, último caso não se aplica às regras anteriores 
    resultado = re.sub(r'>\n<', r'>\n#<', resultado)# Adicionar marcador às categorias
    resultado = re.sub(r'#<.+Categoria: .+>', r'', resultado)# Remover a linha categorias que agora é obsuleta
    resultado = re.sub(r'<\/?text.*?>', r'', resultado)# Remover tags de texto
    resultado = re.sub(r'\n+', r'', resultado)# Remover parágrafos (tudo numa linha)
    resultado = re.split(r'§', resultado)# Separar os casos
    resultado.pop(0)# Remover a primeira instâncias que é vazia devido ao primeiro split
    
    # Criar o Dicionário Final: 
    termos,categoria, descricao = [],[],[]

    # Diferenciar as três partes das definições pelos marcadores criados
    for i in range(len(resultado)):
        termos.append(re.findall(r'@(.+?)#', resultado[i])[0])
        categoria.append(re.findall(r'#(.+?)&', resultado[i])[0])
        descricao.append(re.findall(r'&(.+)', resultado[i])[0])

    # Remover os marcadores no meio das frases
    for i in range(len(resultado)):
        categoria[i] = re.sub(r'#', r'', categoria[i])
        descricao[i] = re.sub(r'&', r'', descricao[i])

    dicionario_def = {i : {} for i in 'ABCDEFGHIJLMNOPQRSTUVWZ'}# Criar o dicionário maior que irá conter os termos
    cat_desc = [[categoria, descricao] for categoria, descricao in zip(categoria, descricao)]# Lista em que a primeira posição é a categoria e a segunda a definição
    dicionario_unidos = {termos: cat_desc for termos, cat_desc in zip(termos, cat_desc)}# Unir as listas criadas aos seus termos respetivos

    # Ciclo para adicionar corretamente os termos no glossário tomando em consideração se iniciam com sinais
    for letra in dicionario_def:
        for termo in dicionario_unidos:
            if termo[0] =='Á':
                dicionario_def['A'][termo] = dicionario_unidos[termo]
            elif termo[0] =='É':
                dicionario_def['E'][termo] = dicionario_unidos[termo]
            elif termo[0] =='Í':
                dicionario_def['I'][termo] = dicionario_unidos[termo]
            elif termo[0] =='Ó':
                dicionario_def['O'][termo] = dicionario_unidos[termo]
            elif termo[0].upper()==letra:
                dicionario_def[letra][termo] = dicionario_unidos[termo]

    # Adicionar o glossáio ao dicionario maior com as siglas
    dicionario['Glossário'] = dicionario_def

    # Guardar o dicionário em Json
    with open('json_glossario_ministerio.json', 'w', encoding='utf-8') as ficheiro_json:
        json.dump(dicionario, ficheiro_json, indent= 6, ensure_ascii= False)


main()