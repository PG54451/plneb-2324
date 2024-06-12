import re
import json


def main():
    xml=open('glossario_ministerio_saude.xml','r', encoding='utf8')
    resultado = str(xml.read())
    result = open('resultado.xml','w', encoding='utf-8')


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
    siglas = re.sub(r'ﬁ ',r'fi', siglas)#remover caracter único
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
    dicionario = [{'termo': sigla, 'categoria': ['N/A'], 'descrição': definicao, 'tradução inglês': 'N/A'} for sigla, definicao in zip(sigla, definicao)]


    # Termos, Doenças Crônicas e Degenerativas e Doenças Infecciosas e Parasitárias não têm casos
    termos = ['Acidentes e Violência','Administração e Planejamento em Saúde','Alimentação e Nutrição','Ambiente e Saúde','Atenção à Saúde','Ciência e Tecnologia em Saúde','Ciências Sociais em Saúde','Comunicação em Saúde','Demografia','Direito Sanitário','Doenças','Doenças Crônicas e Degenerativas','Doenças Infecciosas e Parasitárias','Drogas de Uso Terapêutico e Social','Economia de Saúde','Economia da Saúde','Ciências Sociais e Saúde','Epidemiologia','Eqüidade em Saúde e Social','Ética e Bioética','História da Saúde Pública','Medicamentos, Vacinas e Insumos','None','Políticas Públicas e Saúde','Promoção e Educação em Saúde','Recursos Humanos em Saúde Pública','Saúde Animal','Vigilância em Saúde']

    # Glossário
    resultado = re.sub(r'<page number="5".+?>(\n|.)*<page number="9".+?>(\n|.)*?</page>', r'', resultado)# Remoção das Siglas do código principal
    resultado = re.sub(r'<text.*?top="2..".*?>.*?<\/text>', r'', resultado)# Remover informação no topo das páginas
    resultado = re.sub(r'ﬁ ',r'fi', resultado)#remover caracter único
    resultado = re.sub(r'<\/?page.*?>',r'', resultado)# Remover tags de páginas
    resultado = re.sub(r'-<',r'<', resultado)# Remover traços de continuação de frase
    resultado = re.sub(r'<text.*?(width=".+?").*?>',r'<text \1>', resultado)# Remover tags de texto
    resultado = re.sub(r'\n+',r'\n', resultado)# Remover espaços entre diferentes linhas
    resultado = re.sub(r'<b>epidemiologia<\/b>',r'Epidemiologia', resultado)# Encontrado erro, epidemiologia em Notiﬁcação de doenças está a negrito e em minúsculas
    resultado = re.sub(r'<i>Categoria</i>(.+)\n(.+)>:? ',r'<i>Categoria: </i>\1\n\2>', resultado)# Encontrado erro, má formatação de categoria
    resultado = re.sub(r'<i>(<b>.+?<\/b>)<\/i>', r'\1', resultado)# Remover casos de palavras em bold e itálico
    resultado = re.sub(r'<text.+?><b>(.+?)>', r'§@<b>\1>', resultado)# Criar marcador de termos
    resultado = re.sub(r'</b></text>\n§@<b>', r'', resultado)# Unir continuação de termos em diferentes linhas
    resultado = re.sub(r'<i>(Categoria: ?)</i>', r'\1', resultado)# Remover tags italico Categoria
    #resultado = re.sub(r'<\/?i>', r'', resultado)
    #print(re.findall(r'<text.+?><i>(.+)</i></text>', resultado))  
    resultado = re.sub(r'(<text.+?width="(?:229|2[3-9][0-9]).+)', r'&\1', resultado)# Se tem width> 228, então é descrição, logo não é uma categoria
    resultado = re.sub(r'(<text.+?>.+\n§@<b>)', r'&\1', resultado)# Se está antes de outro termo é descrição
    resultado = re.sub(r'<\/?b>', r'', resultado)# Remover tags de bold
    resultado = re.sub(r'(@.+?\n)(&+<.+?Ver.+)', r'\1#None\n\2', resultado)# Adicionar NA a termos sem categoria
    resultado = re.sub(r'(§@Zalcitabina.+>\n)(.+)', r'\1#None\n&\2', resultado)# Caso específico, último caso não se aplica às regras anteriores 
    resultado = re.sub(r'>\n<', r'>\n#<', resultado)# Adicionar marcador às categorias
    resultado = re.sub(r'#<.+Categoria: .+>', r'', resultado)# Remover a linha categorias que agora é obsuleta
    resultado = re.sub(r'<\/?text.*?>', r'', resultado)# Remover tags de texto
    resultado = re.sub(r'#<i>(.+)</i>', r'&\1', resultado)# Remover # em casos de &
    
    #Casos específicos em que termos ficaram na mesma linha
    resultado = re.sub(r'(#.+?)\n#(Saúde.*)', r'\1\2', resultado)
    resultado = re.sub(r'(#Saúde Animal). (Vigilância em Saúde)', r'\1\n#\2', resultado)
    resultado = re.sub(r'(#Acidentes e Violência) (Atenção à Saúde)', r'\1\n#\2', resultado)
    
    #Casos em que a categoria está dividida em várias linhas
    lista_termos = [i for i in re.findall(r'#(.+)', resultado) if i not in termos and i!= ' ']
    for i in range(1, len(lista_termos)):
        term1 = lista_termos[i-1]
        term2 = lista_termos[i]
        termf = lista_termos[i-1]+lista_termos[i]
        if termf.strip() in termos:
            resultado = re.sub(fr'#{term1}\n#{term2}', fr'#{termf.strip()}', resultado)
    
    #Casos em que a descrição está com o símbolo de categoria
    lista_def = [i for i in re.findall(r'#(.+)', resultado) if i.strip() not in termos and i!=' ']
    for i in lista_def:
        resultado = resultado.replace(f'#{i}', f'&{i}')

    resultado = re.sub(r'# *\n', r'', resultado)
    resultado = re.sub(r'\n+', r'', resultado)# Remover parágrafos (tudo numa linha)
    resultado = re.split(r'§', resultado)# Separar os casos
    resultado.pop(0)# Remover a primeira instâncias que é vazia devido ao primeiro split
    #result.write(resultado)
    # Criar o Dicionário Final: 
    termos,categoria, descricao = [],[],[]

    # Diferenciar as três partes das definições pelos marcadores criados
    for i in range(len(resultado)):
        termos.append(re.findall(r'@(.+?)#', resultado[i])[0])
        categoria.append(re.findall(r'#(.+?)&', resultado[i])[0])
        descricao.append(re.findall(r'&(.+)', resultado[i])[0])
    # Remover os marcadores no meio das frases
    for i in range(len(resultado)):
        categoria[i] = categoria[i].strip()
        categoria[i] = re.sub(r'\s*#\s*', r'!', categoria[i])
        categoria[i] = categoria[i].split('!')# Dividir todas as categorias
        descricao[i] = re.sub(r'&', r'', descricao[i])

    #Criação do dicionário final
    dicionario_termos = [{'termo': termo, 'categoria': categoria, 'descrição': descricao, 'tradução inglês': 'N/A'} for termo, descricao, categoria in zip(termos, descricao, categoria)]
    for item in dicionario_termos:
        dicionario.append(item)

    # Guardar o dicionário em Json
    with open('dicionario_glossario_ministerio.json', 'w', encoding='utf-8') as ficheiro_json:
        json.dump(dicionario, ficheiro_json, indent= 6, ensure_ascii= False)


main()