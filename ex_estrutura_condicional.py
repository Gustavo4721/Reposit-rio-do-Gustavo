# 1 - Par ou ímpar
n = int(input("Digite um número:"))
if n % 2 == 0:
    print(f"O número {n} é par.")
else:
    print(f"O número {n} é ímpar.")

# 2 - Aprovado ou reprovado
nota = float(input("Digite a sua nota:"))
if nota >= 7:
    print("Você foi aprovado!")
else:
    print("Você foi reprovado!")

# 3 - Cálculo de desconto
valor = float(input("Digite o valor da sua compra:"))
if valor > 100:
    print(f"Um desconto de 10% foi aplicado ao valor da sua compra, totalizando: {valor-(valor*0.1)}")
else:
    print(f"O valor final da sua compra foi de: {valor}")

# 4 - Conversão de temperatura
celsius = float(input("Digite a temperatura em graus celsius:"))
fahrenheit = float((celsius*9/5)+32)
print(f"Essa temperatura em fahrenheit é: {fahrenheit}")

# 5 - Maior número (Dois valores)
n1 = int(input("Insira o primeiro valor:"))
n2 = int(input("Insira o segundo valor:"))
if n1 != n2:
    print(f"O maior valor é: {max(n1,n2)}")
else:
    print("Os valores são iguais.")

# 6 - Maior número (Três valores)
n3 = int(input("Insira o primeiro valor:"))
n4 = int(input("Insira o segundo valor:"))
n5 = int(input("Insira o terceiro valor"))
print(f"O maior valor é: {max(n3,n4,n5)}!")

# 7 - Calculadora simples
n6 = float(input("Insira o primeiro valor:"))
n7 = float(input("Insira o segundo valor:"))

# Questão 10 - Intervalo de idade
idade = int(input("Digite sua idade: "))
if 18<=idade<=65:
    print("Dentro da faixa permitida")
else:
    print("Fora da faixa permitida")

# Questão 11 - Acesso ao sistema
usuario = input("Digite o usuário: ")
senha = input("Digite a senha")
if usuario=="admin" and senha=="1234":
    print("Acesso permitido")
else:
    print("Acesso negado")

# Questão 12 - Voto obrigatório
idade = int(input("Digite a sua idade: "))

if 18<=idade<=70:
    print("Voto obrigatório")
elif idade<16:
    print("Não vota")
else:
    print("Voto facultativo")

# Questão 13 - Número fora do intervalo
num = int(input("Digite um número: "))
if 10<=num<=50:
    print("Dentro do intervalo")
else:
    print("Fora do intervalo")

# Questão 14 - Aluno aprovado
media = float(input("Digite sua média final: "))
if media>=7:
    print("Aprovado")
elif 5<=media<7:
    print("Recuperação")
else:
    print("Reprovado")