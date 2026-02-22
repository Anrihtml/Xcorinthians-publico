peso = float(input("digite seu peso em kg:").replace(",", "."))
altura = float(input("digite sua altura em metros: ").replace(",", "."))
imc = peso / (altura**2)
print(f"seu imc é igual a {imc:.2f}")

if imc < 18.5: 
   print("você está abaixo do peso")

elif imc < 25:
   print("você está no peso normal")
elif imc < 30:
   print("você está com obesidade grau 1")
elif imc < 39.9:
   print("você está com obesidade grau 2")
elif imc > 40:
   print("você está com obesidade grave")