import re

f  = open("dicionario_medico.txt", encoding="utf-8")
texto = f.read()

# Data Cleaning
texto = re.sub(r"\f","", texto)

#Marcar designações
texto = re.sub(r"\n\n(.+)", r"\n\n@\1", texto)
texto = re.sub(r"@(.+)\n\n@", r"@\1\n", texto) #Tentar arranjar forma de arrumar o caractere form feed 

#Extrair termos
conceitos = re.split(r"\n{2,}", texto)

termos = [tuple(conceito.split("\n", maxsplit=1)) for conceito in conceitos] #Percorre os conceitos e só separa em dupla de tuplos

#termos = re.findall(r"@(.+)\n([^@]+)", texto) 


print(conceitos)

