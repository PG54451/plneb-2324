import re

f  = open("TPC3/dicionario_medico.txt", encoding="utf-8")
texto = f.read()

# Data Cleaning
texto = re.sub(r"\f", "", texto)

# Marcar designações
texto = re.sub(r"\n\n(.+)", r"\n\n@\1", texto) #Coloca @ antes da designacao
texto = re.sub(r"(@[^\n]+)\n(\n|\f)+", r"@\1\n", texto)

# Extrair termos
termos = re.findall(r"@(.+)\n([^@]+)", texto)

titulo = "<h3> Dicionário Médico </h3>"
descricao = "<p style='text-align: center; font-size: 20px; padding-bottom: 15px;'> Este é um dicionário desenvolvido na disciplina de PLNEB </p>"

body = "<body style='font-family: Arial, sans-serif;'>"
for termo in termos:
    # Verifica se a descrição começa com uma tag HTML
    if termo[1].startswith("<"):
        body += f"<div style='background-color: #6ab7b9; color: white; padding: 10px; margin-bottom: 10px; border-radius: 10px;'> <h5> {termo[0]} </h5> {termo[1]} </div>"
    else:
        body += f"<div style='background-color: #6ab7b9; color: white; padding: 10px; margin-bottom: 10px; border-radius: 10px;'> <h5> {termo[0]} </h5> <p> {termo[1]} </p> </div>"

body += "</body>"

html = f"""<!DOCTYPE html>
<html lang='pt-br'>
<head>
<meta charset='UTF-8'>
<title>Dicionário Médico</title>
<style>
body {{
    margin: 0;
    padding: 0;
    background-color: #f2f2f2;
}}
.container {{
    width: 80%;
    margin: auto;
    padding: 20px;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
}}
h3 {{
    color: white;
    font-size: 30px;
    border-radius: 10px;
    padding: 20px;
    background-color: teal;
    text-align: center;
    width: 50%;
    margin: 20px auto 0;
}}
h5 {{
    color: black;
}}
p {{
    color: black;
    line-height: 1.6;
}}
hr {{
    border: 0;
    border-top: 1px solid #ddd;
    margin: 20px 0;
}}
</style>
</head>
{titulo}
<body>
<div class='container'>
{descricao}
{body}
</div>
</body>
</html>"""


with open("TPC3/TPC3.html", "w", encoding="utf-8") as file_out:
    file_out.write(html)
