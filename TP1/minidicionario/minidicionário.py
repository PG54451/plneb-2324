import re
import json

# Abrir o arquivo XML
with open("minidicionario.xml", "r", encoding="utf-8") as file:
    texto = file.read()

# Remover tags e Marcar a separação dos dicionários
texto = re.sub(r'<page number="31"[^>]*>', r'#', texto)
texto = re.sub(r'<\/?page[^>]*>', '', texto)
texto = re.sub(r'<\/?fontspec[^>]*>', r'', texto)
texto = re.sub(r'<\/?image[^>]*>', r'', texto)
texto = re.sub(r'<\/?text[^>]*\bfont="(5|6|9|10|12)">.*', r'', texto)
texto = re.sub(r'<\/?text[^>]*>', r'', texto)

# Agrupar termos e definições
texto = re.sub(r'<\/b>\n<b>', r'', texto)
texto = re.sub(r'<b>–</b>', r'', texto)
texto = re.sub(r'<\/b>', r'£', texto)
texto = re.sub(r'<b>', r'@', texto)
texto = re.sub(r'\s?\n\s?', r'\n', texto)
texto = re.sub(r'\n', r'', texto)


# Criar listas e limpar os dados 
lista = re.split(r'#', texto)

en_pt = re.split(r'@', lista[0])
en_pt.pop(0)
en_pt = [elemento.replace("\xad", "") for elemento in en_pt]

pt_en = re.split(r'@', lista[1])
pt_en.pop(0)
pt_en = [elemento.replace("\xad", "") for elemento in pt_en]


# Criar listas e Dicionários para termos e descrições 
termo, definicao = [], []
dic_en_pt, dic_pt_en = {}, {}

for i in en_pt:
        index = i.index('£')
        termo.append(i[:index].strip())
        definicao.append(i[index+1:].strip())
        dict_en_pt = { termo: definicao for termo, definicao in zip(termo, definicao)}
        
termo.clear()
definicao.clear()

for i in pt_en:
        index = i.index('£')
        termo.append(i[:index].strip())
        definicao.append(i[index+1:].strip())
        dict_pt_en = { termo: definicao for termo, definicao in zip(termo, definicao)}

dicionario = {}
dicionario["EN_PT"] = dict_en_pt
dicionario["PT_EN"] = dict_pt_en
with open('minidicionario.json', 'w', encoding='utf-8') as ficheiro_json:
    json.dump(dicionario, ficheiro_json, indent= 6, ensure_ascii= False)