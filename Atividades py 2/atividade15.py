def celsius_fahrenheit(temp_celsius):
    return (temp_celsius * 9/5) + 32

def fahrenheit_celsius(temp_fahrenheit):
    return (temp_fahrenheit - 32) * 5/9

try:
    escolha = input("Escolha a conversão:\n1 - Celsius para Fahrenheit\n2 - Fahrenheit para Celsius\n")

    if escolha == "1":
        temp_celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"{temp_celsius} Celsius é igual a {celsius_fahrenheit(temp_celsius):.2f} Fahrenheit.")
    elif escolha == "2":
        temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"{temp_fahrenheit} Fahrenheit é igual a {fahrenheit_celsius(temp_fahrenheit):.2f} Celsius.")
    else:
        print("Escolha inválida. Digite 1 ou 2 para escolher a conversão.")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar um número válido para a temperatura.")
