import re
import json

# Abrir o arquivo XML
with open("minidicionario.xml", "r", encoding="utf-8") as file:
    texto = file.read()
result = open('resultado.xml','w', encoding='utf-8')

# Remoção de palavras topo de página, numeros de página, letras referentes aos termos à direita/
texto = re.sub(r'(.+top="26".+\n|.+>\d\d.+\n|<text.+left="4..".+width="[67891]0?".+\n|.+>[A-Z]<.+\n)', '', texto)
texto = re.sub(r'<\/?(page|fontspec|image|text).*?>', '', texto)# Remover informação desnecessária
texto = re.sub(r'<b>(.+)</b>', r'@\1#', texto)# Substituir termos por símbolos de início e fim destes
texto = re.sub(r'#\n@|-\n', r'', texto)# Unir parte do mesmo termo e retirar traços de continuação da palavra
texto = re.sub(r'\n| {2,}|\t', r'', texto)# Remover parágrafos, vários espaços seguidos e \t
result.write(texto)
#Resolver casos específicos em que o traço não estava em bold como os termos
texto = re.sub(r'# @', r'', texto)
texto = re.sub(r'# –', r'–#', texto)
texto += '@'# Terminar o texto com @ para que a procura na lista desc funcione

termos = re.findall(r'@(.+?)\s*–?\s*#', texto)# Criar lista de termos
eng = re.findall(r'#(.+?)@', texto)# Criar lista de definições
index_port = termos.index('1ª / 2ª/ 3ª / 4ª / Bulha')

# Criar dicionário
dicionario = [{'termo': eng[i].strip(), 'categoria': ['N/A'], 'descrição': 'N/A', 'tradução inglês': termos[i].strip()} for i in range(index_port)]

# Separar casos com a mesma tradução
for item in dicionario[1:]:
    if '/' in item['termo']:
        item['termo'] = item['termo'].split('/')
        for i in item['termo']:
            novo_termo = {'termo': i.strip(), 'categoria': ['N/A'], 'descrição': 'N/A', 'tradução inglês': item['tradução inglês']}
            dicionario.insert(dicionario.index(item), novo_termo)
        dicionario.remove(item)
    
with open('dicionario_mini.json', 'w', encoding='utf-8') as ficheiro_json:
    json.dump(dicionario, ficheiro_json, indent= 6, ensure_ascii= False)