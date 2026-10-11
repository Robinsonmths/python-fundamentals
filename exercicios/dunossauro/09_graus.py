# Faça um programa que peça a temperatura em graus Celsius,
# transforme e mostre a temperatura em graus Fahrenheit.

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C em Fahrenheit é: {fahrenheit}°F")
