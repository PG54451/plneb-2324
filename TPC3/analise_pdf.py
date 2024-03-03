import re

f  = open("dicionario_medico.txt", encoding="utf-8")
texto = f.read()

# Data Cleaning
texto = re.sub(r"\f","", texto)

#Marcar designações
texto = re.sub(r"\n\n(.+)", r"\n\n@\1", texto)
texto = re.sub(r"@(.+)\n\n@", r"@\1\n", texto) #Tentar arranjar forma de arrumar o caractere form feed 

#Extrair termos
#designacao = []
#designacao = re.findall(r"@(.+)\n", texto)

#Extrair descricoes
#descricoes = []
#descricoes = re.findall(r"@.+\n([^@]+)", texto)
termos = re.findall(r"@(.+)\n([^@]+)", texto) 

titulo = "<h3> Dicionário Médico </h3>"
descricao = "<p> Este é um dicionário desenvolvido na disciplina de PLNEB </p>"

body = "<body>"
for termo in termos:
    body += f"<h5> {termo[0]} </h5>"
    body += f"<p> {termo[1]} </p>"
    body += f"<hr/>"

body += "</body>"

html = titulo + descricao + body

print(html)
    
file_out = open("aula3.html", "w")
file_out.write(html)
file_out.close()



