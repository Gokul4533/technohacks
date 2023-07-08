temp = False

def celsius_to_fahrenheit(value_Celsius):
    value1 = ((9 / 5) * value_Celsius) + 32
    return value1


def fahrenheit_to_celsius(value_fahrenheit):
    value2 = (value_fahrenheit - 32) * 5.0 / 9.0
    return value2


while not temp == True:

    print('(1) Convert Celsius to Fahrenheit\n(2) Convert Fahrenheit to Celsius')

    choice = int(input('\nEnter your choice : '))

    if choice == 1:
        value1 = float(input('\nEnter a value in Celsius:\n'))
        print(celsius_to_fahrenheit(value1))

    if choice == 2:
        value2 = float(input('\nEnter a value in Fahrenheit:\n'))
        print(fahrenheit_to_celsius(value2))