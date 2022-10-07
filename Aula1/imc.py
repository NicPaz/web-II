def calculaImc (peso,altura):
    imc = peso / (altura*altura)
    return imc

pes = float(input("Informe o peso: "))
alt = float(input("Informe a altura: "))
imc = calculaImc(pes,alt)
print(f"O imc é = {imc:.2f}")