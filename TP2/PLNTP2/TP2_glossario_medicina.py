import re
import json

# Abrir o arquivo XML
with open("medicina.xml", "r", encoding="utf-8") as file:
    texto = file.read()
result = open('resultado.xml','w', encoding='utf-8')

categorias = ['Patoloxías','Etiopatoxenia','Probas complementarias','Terapéutica','Medicina preventiva','Farmacoloxía','Anatomía','Anatomía patolóxica','Semioloxía','Fisioloxía','Epidemioloxía','Histoloxía','Bioquímica','Xenética','Organización sanitaria','Instrumental','Termos xerais']
categorias_port = ['Patologias','Etiopatogenia','Testes complementares','Terapêutica','Medicina preventiva','Farmacologia','Anatomia','Anatomia patológica','Semiología','Fisiologia','Epidemiologia','Histologia','Bioquímica','Genética','Organização de saúde','Instrumental','Termos gerais']

pt = re.findall(r'>\s*pt\s*<.+\n.+>(.+?)<', texto)
pt = [re.sub(r'\s*\[.+\]', r'', i) for i in pt]
eng = re.findall(r'>\s*en\s*<.+\n.+>(.+?)<', texto)
categoria = [i.strip() for i in re.findall(r'<text.+font="21"><i>(.+)<\/i>.+', texto) if i.lower() != i]

#Casos específicos, tamanho de letra diferente
categoria.insert(507, 'Termos xerais')
categoria.insert(1022, 'Epidemioloxía')
categoria.insert(4358, 'Semioloxía')
categoria.insert(4989, 'Xenética')
#Termos Xerais - 508
#Semioloxía - 4359
#Epidemioloxía - 1023
#Xenética - 4990

categoria = [re.sub(r'  +', r'§', categoria[i]) for i in range(len(categoria))]# Casos em que à várias categorias
categoria = [categoria[i].split('§') for i in range(len(categoria))]# Separar estes casos por split

# Substituir espanhol por português
for i in range(len(categoria)):
    for j in range(len(categoria[i])):
        if categoria[i][j] == 'Preventiva':
            categoria[i][j] == 'Medicina preventiva'
        else:
            categoria[i][j] = categorias_port[categorias.index(categoria[i][j])]

# Criar dicionário
dicionario = [{'termo': pt[i].capitalize().strip(), 'categoria': categoria[i], 'descrição': 'N/A', 'tradução inglês': eng[i].strip()} for i in range(5393)]

    
with open('dicionario_medicina.json', 'w', encoding='utf-8') as ficheiro_json:
    json.dump(dicionario, ficheiro_json, indent= 6, ensure_ascii= False)