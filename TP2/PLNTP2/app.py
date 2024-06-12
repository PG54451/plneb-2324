from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

with open('glossario.json', 'r', encoding='utf-8') as f:
    terms = json.load(f)

unique_categories = sorted(set(cat for term in terms for cat in term['categoria']))

@app.route('/')
def index():
    return render_template('index.html', terms=terms, unique_categories=unique_categories)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query'].lower()
    search_type = request.form['search_type']
    selected_category = request.form['category']

    if search_type == 'term':
        results = [term for term in terms if query in term['termo'].lower()]
    elif search_type == 'description':
        results = [term for term in terms if query in term['descrição'].lower()]
    elif search_type == 'translation':
        results = [term for term in terms if query in term.get('tradução inglês', '').lower()]
    else:
        results = [term for term in terms if query in term['termo'].lower() or query in term['descrição'].lower() or query in term.get('tradução inglês').lower()]

    if selected_category != 'all':
        results = [term for term in results if selected_category in term['categoria']]
    print(results)

    return render_template('index.html', terms=terms, unique_categories=unique_categories, results=results)

@app.route('/novo_termo', methods=['GET', 'POST'])
def novo_termo():
    if request.method == 'POST':
        new_term = {
            'termo': request.form['termo'],
            'descrição': request.form['descrição'],
            'tradução inglês': request.form.get('tradução inglês'),
            'categoria': request.form['categoria'].split(',')
        }
        terms.append(new_term)
        with open('glossario.json', 'w', encoding='utf-8') as f:
            json.dump(terms, f, ensure_ascii=False, indent=4)
        return redirect(url_for('index'))
    return render_template('novo_termo.html')

@app.route('/term/<string:termo>')
def termos_detalhes(termo):
    term_details = next((t for t in terms if t['termo'].lower() == termo.lower()), None)
    return render_template('termos_detalhes.html', term=term_details)

@app.route('/term/<string:termo>/edit', methods=['GET', 'POST'])
def edit_term(termo):
    term_details = next((t for t in terms if t['termo'].lower() == termo.lower()), None)
    if request.method == 'POST':
        term_details['descrição'] = request.form['descrição']
        term_details['tradução inglês'] = request.form.get('tradução inglês')
        term_details['categoria'] = request.form['categoria'].split(',')
        with open('glossario.json', 'w', encoding='utf-8') as f:
            json.dump(terms, f, ensure_ascii=False, indent=4)
        return redirect(url_for('termos_detalhes', termo=termo))
    return render_template('edit_termo.html', term=term_details)

@app.route('/remove/<string:termo>', methods=['POST'])
def remove_term(termo):
    global terms
    terms = [term for term in terms if term['termo'] != termo]

    with open('glossario.json', 'w', encoding='utf-8') as f:
        json.dump(terms, f, ensure_ascii=False, indent=4)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)