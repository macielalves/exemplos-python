def celsius(fahrenheit):
    return ((fahrenheit - 32) / 9) * 5


while True:
    try:
        fah = float(input("\nTemperatura em Fahrenheit: "))
        print("A temperatura equivale a %.2f °C" % celsius(fah))
        break
    except ValueError:
        print("\nRevise o valor inserido e tente novamente!")
