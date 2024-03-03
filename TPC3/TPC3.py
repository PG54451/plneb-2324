import re

f  = open("TPC3/dicionario_medico.txt", encoding="utf-8")
texto = f.read()

# Data Cleaning
texto = re.sub(r"\f", "", texto)

# Marcar designações
texto = re.sub(r"\n\n(.+?)(?=\n\n|$)", r"\n\n@\1", texto, flags=re.DOTALL)
texto = re.sub(r"@(.+?)\n\n(?=@|$)", r"@\1\n", texto, flags=re.DOTALL)


# Extrair termos
termos = re.findall(r"@(.+)\n([^@]+)", texto)

titulo = "<h3 style='text-align: center;'> Dicionário Médico </h3>"
descricao = "<p> Este é um dicionário desenvolvido na disciplina de PLNEB </p>"

body = "<body style='font-family: Arial, sans-serif;'>"
for termo in termos:
    # Verifica se a descrição começa com uma tag HTML
    if termo[1].startswith("<"):
        body += f"<h5> {termo[0]} </h5> {termo[1]} <hr/>"
    else:
        body += f"<h5> {termo[0]} </h5> <p> {termo[1]} </p> <hr/>"

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
}}
h5 {{
    color: #333;
}}
p {{
    color: #666;
    line-height: 1.6;
}}
hr {{
    border: 0;
    border-top: 1px solid #ddd;
    margin: 20px 0;
}}
</style>
</head>
<body>
<div class='container'>
{titulo}
{descricao}
{body}
</div>
</body>
</html>"""

print(html)
    
with open("TPC3/tpc3.html", "w", encoding="utf-8") as file_out:
    file_out.write(html)