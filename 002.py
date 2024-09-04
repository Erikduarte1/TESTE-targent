def verificar_letra_a(s):
    s = s.lower()
    quantidade = s.count('a')
    existe = quantidade > 0
    return existe, quantidade
string = input("Digite uma string para verificar a letra 'a': ")
existe, quantidade = verificar_letra_a(string)
if existe:
    print(f"A letra 'a' aparece {quantidade} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")
