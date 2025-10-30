# Questão 1

funcao1 = lambda x: x**22
print(funcao1(4))

# Questão 2

funcao2 = lambda x: 5*x-3
print(funcao2(2))

# Questão 3

funcao3 = lambda x: x**2 + 2*x + 1
print(funcao3(-1))
print(funcao3(0))
print(funcao3(1))

# Questão 4

funcao4 = lambda x, y: x**2 + 2*x*y + y**2
print(funcao4(2, 4))

# Questão 5

funcao5 = lambda x, y, z: x**y + z
print(funcao5(3, 2, 10))

# Questão 6

def lucro(receita, custo):
    lucro = receita - custo
    return lucro

print(lucro(10000, 7500))

# Questão 7

def margem_lucro(lucro, receita):
    margem_lucro = (lucro / receita) * 100
    return margem_lucro

print(margem_lucro(20000, 15000))

# Questão 8

def ponto_equilibrio(custo_fixo, preco, custo_variavel):
    qe = custo_fixo / (preco - custo_variavel)
    return qe

print(ponto_equilibrio(5000, 50, 30))

# Questão 9

def folha(funcionarios):
    for funcionario in funcionarios:
        total = 0
        total = total + funcionario['salario']
    return total

funcionarios = [
    {'nome': 'Ana', 'salario': 3000},
    {'nome': 'Carlos', 'salario': 4500}
]

folha(funcionarios)

# Questão 10

def juros_compostos(capital, taxa, tempo):
    montante = capital * ((1 + taxa) / tempo)
    return montante

print(juros_compostos(1000, 0.02, 12))