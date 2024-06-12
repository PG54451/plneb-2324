import re
import json



# Abrir ficheiros
xml=open('glossário.xml','r', encoding='utf-8')
resultado = str(xml.read())

# Alterações do XML
resultado = re.sub(r'<text.*?>[A-Z]<\/text>|<b>[A-Z]<\/b>|<text.*?>[ ]*,[ ]*<\/text>|<text.*?>[ ]+<\/text>', r'', resultado)# Remover letras referentes à ordem alfabética dos termos e tags de texto sem nada dentro
resultado = re.sub(r'<text.*?>[ ,]*\(pop\)[ ,]*<\/text>', r'(pop)', resultado)# Substituir todas as ocorrências do marcador pop com espaços e vírgulas por (pop) apenas.
resultado = re.sub(r'<text.*?>|<\/text>', r'', resultado)# Remover tags de texto mantendo a informação contida neles
resultado = re.sub(r'<page.*?>|<\/page>|<fontspec.+?>', r'', resultado)#Remover tags de página mantendo a informção contida neles e a tag fontspec

termos_ligados = re.findall(r'<b>(.+)<\/b>\n<b>(.+)<\/b>', resultado)#Procurar por termos que estejam em linhas diferentes sem um parágrafo
lista_bold =re.findall(r'<b>(.*?)<\/b>', resultado)#Procurar por todas as intâncias de termos

# Resolver os termos que foram separados em diferentes linhas
# Verificar se os termos em linhas diferentes são uma continuação ou não e uni-los se sim
for i in range(len(termos_ligados)):
    inicio = termos_ligados[i][0]
    fim = termos_ligados[i][1]
    if termos_ligados[i][0]+termos_ligados[i][1] in lista_bold:
        resultado = re.sub(f'<b>{inicio}</b>\n<b>{fim}</b>', f'<b>{inicio}{fim}</b>', resultado)
    elif termos_ligados[i][0]+' '+termos_ligados[i][1] in lista_bold:
        resultado = re.sub(f'<b>{inicio}</b>\n<b>{fim}</b>', f'<b>{inicio} {fim}</b>', resultado)

lista_bold =re.findall(r'<b>(.*?)<\/b>', resultado)# Procurar de novo com os termos ajustados

resultado = re.sub(r'<b>.*?<\/b>', r'', resultado)# Remover as tags e os termos
resultado = re.sub(r'\n', r'', resultado)# Remover parágrafos
resultado = re.sub(r' {2,}', r' ', resultado)# Substituir espaços a mais nas definições por um único espaço
resultado = re.sub(r'<\/i><i>', r' ', resultado)# Substituir tags de itálico entre duas linhas da mesma frase por um espaço
resultado = re.sub(r'<\/i>|<i>', r'', resultado)# Substituir tags de itálico restantes por vazio
lista_def = re.split(r'\(pop\)', resultado)# Dividir todas as definições pelo marcador de separação (pop)
lista_def.pop()# Remover o último separador vazio da lista de definições

dicionario= [{'termo': termo.capitalize().strip(), 'categoria': ['N/A'], 'descrição': definicao, 'tradução inglês': 'N/A'} for termo, definicao in zip(lista_bold, lista_def)]

# Guardar o dicionário em Json
with open('dicionario_glossario.json', 'w', encoding='utf-8') as ficheiro_json:
    json.dump(dicionario, ficheiro_json, indent= 6, ensure_ascii= False)