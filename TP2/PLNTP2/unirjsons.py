from deep_translator import GoogleTranslator
import json


ficheiros = ['glossario','glossario_ministerio','medicina','mini','online']

json_final = 'glossario.json'


def unir_jsons(ficheiros, json_final):
    dados_unidos = []
    termos = []
    for dicio in ficheiros:
        nome = 'dicionario_' + dicio + '.json'
        with open(nome, 'r', encoding='utf-8') as file:
            dados = json.load(file)
            for item in dados:
                if item['termo'] not in termos:
                    termos.append(item['termo'])
                    dados_unidos.append(item)

    translator = GoogleTranslator(source='pt', target='en')

    for item in dados_unidos:
        if item['tradução inglês'] == 'N/A':
            termo = item['termo']
            termo_ingles = translator.translate(termo)
            item['tradução inglês'] = termo_ingles

    with open(json_final, 'w', encoding='utf-8') as output:
        json.dump(dados_unidos, output, ensure_ascii=False, indent=4)


unir_jsons(ficheiros, json_final)