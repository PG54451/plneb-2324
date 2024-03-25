from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Carrega os conceitos do arquivo JSON
def carregar_conceitos():
    with open('TPC6/conceitos_v2.json', 'r', encoding='utf-8') as f:
        dados_json = json.load(f)
        conceitos = [{"conceito_pt": k, **v} for k, v in dados_json.items()]
        return conceitos

@app.route('/')
def index():
    conceitos = carregar_conceitos()
    pesquisa = request.args.get('pesquisa')
    if pesquisa:
        conceitos = [c for c in conceitos if pesquisa.lower() in c['conceito_pt'].lower()]
    return render_template('index.html', conceitos=conceitos)


@app.route('/conceito/<string:nome>')
def conceito(nome):
    conceitos = carregar_conceitos()
    conceito = next((c for c in conceitos if c['conceito_pt'] == nome), None)
    if conceito:
        return render_template('conceito.html', conceito=conceito)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
