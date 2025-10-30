# Questão 1

aluno = {
    "Nome": "Gustavo",
    "Idade": 18,
    "Curso": "Administração"
}

print(aluno["Nome"])
print(aluno["Idade"])
print(aluno["Curso"])

# Questão 2

produto = {
    "Nome": "Teclado mecânico",
    "Preço": 350.00,
    "Estoque": 10
}

produto["Marca"] = "Toshiba"
produto["Preço"] = 320.00
produto["Estoque"] = produto["Estoque"] - 2
produto.pop("Marca")
print(produto)

# Questão 3

notas = {
    "Alice": 8.5,
    "Bruno": 7.0,
    "Carla": 9.2,
    "Daniel": 6.8
}

for nome, nota in notas.items():
    print(f"O aluno é {nome} e a nota é {nota}")

media = sum(notas.values()) / len(notas)
print(media)

# Questão 4

numeros = {"a": 10, "b": 20, "c": 30}

soma = sum(numeros.values())
print(soma)

# Questão 5

lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]

frequencia = {}
for fruta in lista:
    if fruta in frequencia:
        frequencia[fruta] += 1
    else:
        frequencia[fruta] = 1
print(frequencia)

# Questão 6


