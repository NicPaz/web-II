def converte(a,b):
    res = a * b
    return res

cotacao = float(input("Informe a cotação:"))
dolar = float(input("Informe o valor em dolar:"))
real = converte(cotacao,dolar)
print(f"O valor em real é = {real}")
