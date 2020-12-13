##como mostrar dados mais facil de ler
nome = 'viviane'
idade = 27
altura = 1.58
e_maior = idade > 18
data_1 =  True
data_atual = 2020
peso = 60

imc = peso / altura ** 2

print('Nome', nome)
print('Idade', idade)
print('É maior:', e_maior)

print(idade * altura)

print(nome, 'tem', idade, 'de idade e seu imc é', imc)
 #leitura fica mais facil de ler desta outra forma
print(f'{nome} tem {idade} anos de idade e sue imc é {imc:.2f}')

