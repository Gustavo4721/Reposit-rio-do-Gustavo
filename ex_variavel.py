# 1 - Crie variáveis que representam:
# Sua idade
idade = 18
# Sua altura
altura = 1.66
# Seu nome
nome = "Gustavo"
# Se você é estudante:
e_estudante = False
# Para ver o tipo da variável
type(e_estudante)

# 2 - O usuário digita a sua idade:
# - Converta essa entrada pra número inteiro;
# - Some mais 5 anos e mostre sua idade.
idade = input("Digite a sua idade:")
idade = int(idade) + 5
print(f"Daqui a 5 anos, sua idade será: {idade}")

# 3 - Soma de números inteiros:
# Leia dos números inteiros e exiba a soma deles.
# Entrada: Dois números inteiros.
# Saída: A soma dos dois números.
# Exemplo: Entrada: 3, 5. Saída: 8.
num1 = input("Digite o primeiro número:")
num2 = input("Digite o segundo número:")
soma = int(num1) + int(num2)
print(f"A soma é igual a: {soma}")

# 4 - Médiade três números inteiros:
# Escreva um programa que leia três números inteiros e determine a média deles.
# Entrada: Três números inteiros.
# Saída: Média dos três números.
num3 = input("Digite o primeiro número:")
num4 = input("Digite o segundo número:")
num5 = input("Digite o terceiro número:")
média = (int(num3) + int(num4) + int(num5))/3
print(f"A média é igual a: {média}")

# 5 - Média ponderada (Padrão Ibmec)
# Escreva um programa que receba as 3 notas das avaliações dos alunos e determine a média final através da ponderação padrão do Ibmec.
# Entrada: Três números (notas).
# Saída: Nota final.
AP1 = float(input("Digite a nota da sua AP1:"))
AP2 = float(input("Digite a nota da sua AP2:"))
AC = float(input("Digite a nota da sua AC:"))
média = 0.4 * AP1 + 0.4 * AP2 + 0.2 * AC
print(f"A sua média final é: {média}")

# 6 - Manipuação de Strings:
# Peça o nome completo do usuário.
# Mostre o nome com letras maiúsculas.
# Mostre o primeiro nome.
# Mostre a quantidade de letras no nome (Sem contar os espaços)
nome2 = input("Digite o seu nome completo:")
print(nome2.upper())
print(nome2.split()[0])
print(len(nome2))