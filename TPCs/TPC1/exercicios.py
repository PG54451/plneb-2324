# Function 1: given a string “s”, reverse it.
def func1(s):
    string_reversa = s[::-1]
    return f"A string {s} ao contrário é: {string_reversa}!"

# Function 2: given a string “s”, returns how many “a” and “A” characters are present in it.
def func2(s):
    string_minuscula = s.lower()
    a_ocorrencias = string_minuscula.count()
    return f"As letras 'a' e 'A' aparecem {a_ocorrencias} vezes!"

# Function 3: given a string “s”, returns the number of vowels there are present in it.
def func3(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return f"Na string {s} as vogais aparecem {count} vezes!"

# Function 4: given a string “s”, convert it into lowercase.
def func4(s):
    lower = s.lower()
    return f" A string {s} em minúsculo fica: {lower}"

# Function 5: given a string “s”, convert it into uppercase.
def func5(s):
    upper = s.upper()
    return f" A string {s} em minúsculo fica: {upper}"

# Function 6: Verifica se uma string é capicua
def func6(s):
    reversa = s[::-1]
    if s == reversa:
        return f"A string {s} é capícua!"
    else:
        return f"{s} não é capícua!"    

# Function 7: Verifica se duas strings estão balanceadas (Duas strings, s1 e s2, estão
#             balanceadas se todos os caracteres de s1 estão presentes em s2.)
def func7(s1, s2):
    char_s1 = set(s1)
    char_s2 = set(s2)

    if char_s1.issubset(char_s2):
        return f"As strings estão balanceadas!"
    else:
        return f"Não estão balanceadas!"

# Function 8: Calcula o número de ocorrências de s1 em s2
def func8(s1, s2):
    contador = s2.count(s1)
    return f"O número de ocorrências de {s1} em {s2} é: {contador} vezes."

# Function 9: Verifica se s1 é anagrama de s2.
def func9(s1, s2):
    if sorted(s1) == sorted(s2):
        return f"A string {s1} é anagrama de {s2}!"
    else:
        return f"A string {s1} não é anagrama de {s2}!" 

