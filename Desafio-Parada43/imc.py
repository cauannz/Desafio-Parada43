peso = float(input("Informe seu peso: (Kg) "))
altura = float(input("Informe sua altura: (m) "))
imc = peso / (altura*altura)

print("Seu IMC é: {:.2f}".format(imc))
if imc < 18.5:
    print("Faixa de peso: Abaixo do peso.")
elif 25 > imc >= 18.5:
    print("Faixa de peso: Peso ideal")
elif 30 > imc >= 25:
    print("Faixa de peso: Sobrepeso")
elif 40 > imc >= 30:
    print("Faixa de peso: Obesidade")
else:
    print("Faixa de peso: Obesidade Mórbida")