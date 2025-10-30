# Dicionário

## Questão 1

aluno = {
    'nome': 'gustavo',
    'idade': '19',
    'curso': 'administração'
}

for chave, valor in aluno.items():
    print(f'{chave}: {valor}')

## Questão 2

produto = {
    'nome': 'teclado mecânico',
    'preço': 350,
    'estoque': 10
}

produto['marca'] = 'logitech'

produto['preço'] = 350

produto['estoque'] = produto['estoque'] - 2

## Questão 3

notas = {
    'alice': 8.5,
    'bruno': 7.0,
    'carla': 9.2,
    'daniel': 6.8
}

for chave, valor in notas.items():
    print(f'{chave}: {valor}')

soma_das_notas = sum(notas.values())

quantidade_de_notas = len(notas)

media = soma_das_notas / quantidade_de_notas
print(f'A média das notas é: {media}')

## Questão 4

numeros = {
    'a': 10,
    'b': 20,
    'c': 30
}

soma_dos_numeros = sum(numeros.values())
print(f'A soma dos números é {soma_dos_numeros}')

## Questão 5

lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
contador = {}

for fruta in lista:
    if fruta in contador:
        contador[fruta] = contador[fruta] + 1
    else:
        contador[fruta] = 1

print(contador)

## Questão 6

produtos = {
    "caneta": 10,
    "mochila": 80,
    "caderno": 45,
    "notebook": 3000
}

filtro = []

for produto, valor in produtos.items():
    if valor >= 50:
        filtro.append((produto, valor))
print(filtro)

## Questão 7

tradutor = {
    'house':'casa',
    'party': 'festa',
    'pool': 'piscina',
    'milk': 'leite'
}

palavra = input('Digite uma palavra em inglês:')

traducao = tradutor.get(palavra)

if traducao:
    print(f'A tradução da palavra {palavra} é: {traducao}')
else:
    print('Palavra não encontrada')

# Lista

## Questão 1

frutas = ['maçã', 'banana', 'laranja', 'uva']

## Questão 2

print(frutas[-1])

## Questão 3

frutas.append('manga')
print(frutas)

## Questão 4

frutas.remove('banana')
print(frutas)

## Questão 5

frutas[1] = 'abacaxi'
print(frutas)

## Questão 6

lista1 = list(range(1,11))
print(lista1)

## Questão 7

soma = sum(lista1)
print(soma)

## Questão 8

maximo = max(lista1)
minimo = min(lista1)
print(maximo)
print(minimo)

## Questão 9

lista_invertida = lista1[::-1]
print(lista_invertida)

## Questão 10

cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]

## Questão 11

cidades_ordenadas = sorted(cidades)
print(cidades_ordenadas)

## Questão 12

cidades.append("Porto Alegre")
print(cidades)

## Questão 13

cidades.index('Curitiba')

## Questão 14

cidades.remove('Rio de Janeiro')
print(cidades)

## Questão 15

lista2 = [1, 2, 3]
lista3 = [4, 5, 6]

## Questão 16

lista4 = lista2 + lista3

## Questão 17

print(lista4)

## Questão 18

animais_domesticos = ["cachorro", "gato", "coelho"]
animais_selvagens = ["leão", "tigre", "urso"]

## Questão 19

todos_os_animais = animais_domesticos + animais_selvagens

## Questão 20

print(todos_os_animais)

# Loop for

## Questão 21

nomes = ["Ana", "Pedro", "Maria", "João"]

## Questão 22

for nome in nomes:
    print(nome)

## Questão 23

nomes_maiusculos = []

for nome in nomes:
    nomes_maiusculos.append(nome.upper()) 
print(nomes_maiusculos)

## Questão 24

lista5 = list(range(1,21))

for pares in lista5:
    if pares % 2 == 0:
        print(pares)

## Questão 25

linguagens_de_programacao = ["python", "java", "c", "javascript"]

for palavra in linguagens_de_programacao:
    print(len(palavra))

## Questão 27

idades = [12, 18, 25, 40, 60]
maior_de_idade = []
menor_de_idade = []

for idade in idades:
    if idade < 18:
        menor_de_idade.append(idade)
    else:
        maior_de_idade.append(idade)

print(f'Maior de idade: {maior_de_idade}')
print(f'Menor de idade: {menor_de_idade}')

## Questão 28

notas = [5.5, 7.0, 8.3, 4.9, 6.2]

aprovados = []
reprovados = []

for nota in notas:
    if nota < 7:
        reprovados.append(nota)
    else:
        aprovados.append(nota)

quantidade_de_aprovados = (len(aprovados))
quantidade_de_reprovados = (len(reprovados))

print(f'A quantidade de aprovados é: {quantidade_de_aprovados}')
print(f'A quantidade de reprovados é: {quantidade_de_reprovados}')

## Questão 29

palavras = ["arara", "banana", "radar", "python"]

palindromos = []

for palavra in palavras:
    if palavra == palavra[::-1]:
        palindromos.append(palavra)

print(f'São palíndromos as palavras: {palindromos}')

## Questão 30

compras = ["arroz", "feijão", "batata", "carne"]

for compra in compras:
    print(f'Preciso comprar: {compra}')

# Loop while

## Questão 31

numero = 0

while numero <= 9:
    numero = numero + 1
    print(numero)

## Questão 32

numero = int(input('Digite um número inteiro:'))

while numero != 0:
    numero = int(input('Inválido. Digite outro número inteiro:'))

## Questão 33

numero_atual = 1
soma = 0

while numero_atual <= 100:
    soma = soma + numero_atual
    numero_atual = numero_atual + 1

print(f'A soma dos números de 1 a 100 é {soma}')

## Questão 34
