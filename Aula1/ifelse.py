# Comentario de uma linha

''' 
Comentario
em bloco
'''

#if else
idade = 18

if idade <= 15:
    print('acesso')
elif idade > 15 and idade < 18:
    print('necessita autorizacao')
else:
    print('acesso liberado')

#formas de printar diferentes
valor = 150
print (f"valor igual = {valor}")       
print ("valor igual =", valor)       


#Vetor/lista
materias = ['web II','OO I','BD'] 
print (type(materias))   #tipo da variavel materia
print (f"tamanho da lista = {len(materias)}")   #tamanho da lista 

#for imprimindo o vetor, incrementa 1 
for i in range(0, len(materias)):
    print(materias[i])

#lista com 5 precos de produtos, calcular o total 
precos = [5,3,2,8]
soma = 0

for i in range(0, len(precos)):
    soma = soma + precos[i]

print(f"Valor total da compra: {soma}")