import requests
from bs4 import BeautifulSoup
import string
import json

termos = []
definicao = []

for i in string.ascii_lowercase:
    html_text = requests.get(f"https://www.boasaude.com.br/dicionario-medico/{i}")
    soup = BeautifulSoup(html_text.text, 'html.parser')
    paginas = soup.find(id="paginacao")
    if paginas:
        pag_href = [a['href'] for a in paginas.find_all("a") if a.text.isdigit()]
        for href in pag_href:
            pag_termos = requests.get(href)
            soup = BeautifulSoup(pag_termos.text, 'html.parser')
            list_terms = soup.find("ul", class_="listagem")
            terms_href = [a['href'] for a in list_terms.find_all("a", href=True)]
            for refs in terms_href:
                def_text = requests.get(refs)
                soup = BeautifulSoup(def_text.text, 'html.parser')
                termo = soup.find(id="col-center").h2.text
                termo_def = soup.find(id="col-center").h2.find_next("p").text.strip()
                termos.append(termo)
                definicao.append(termo_def)
    else:
        list_terms = soup.find("ul", class_="listagem")
        terms_href = [a['href'] for a in list_terms.find_all("a", href=True)]
        for refs in terms_href:
            def_text = requests.get(refs)
            soup = BeautifulSoup(def_text.text, 'html.parser')
            termo = soup.find(id="col-center").h2.text.strip()
            termo_def = soup.find(id="col-center").h2.find_next("p").text.strip()
            termos.append(termo)
            definicao.append(termo_def)

dicionario = [{'termo': termo, 'categoria': ['N/A'], 'descrição': definicao, 'tradução inglês': 'N/A'} for termo, definicao in zip(termos, definicao)]

with open('dicionario_online.json', 'w', encoding='utf-8') as ficheiro_json:
    json.dump(dicionario, ficheiro_json, indent= 6, ensure_ascii= False)