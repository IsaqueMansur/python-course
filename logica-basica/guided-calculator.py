while True:
    number1 = input('Digite o primeiro número:\r\n')
    number2 = input('Digite o segundo número:\r\n')
    operator = input('Digite o operador para o cálculo | * | / | - | + |\r\n')
    handle_quit = False
    VALID_OPERATORS = '/*-+'

    try:
        number1 = float(number1)
        number2 = float(number2)
    except:
        print('Você não digitou dois números válidos')
        continue
        
    if operator not in VALID_OPERATORS:
        print('Você não digitou um operador válido')
        continue
        
    if len(operator) > 1:
        print('Digite apenas um operador')
        continue
    
    def sum(value1: float, value2: float): return value1 + value2
    def subtract(value1: float, value2: float): return value1 - value2
    def multiply(value1: float, value2: float): return value1 * value2
    def divide(value1: float, value2: float): return value1 / value2
    
    if operator == '+': print(f'O valor da soma de {number1} e {number2} é: {sum(number1, number2)}')
    if operator == '-': print(f'O valor da subtração de {number1} e {number2} é: {subtract(number1, number2)}')
    if operator == '*': print(f'O valor da multiplicação de {number1} e {number2} é: {multiply(number1, number2)}')
    if operator == '/': print(f'O valor da divisão de {number1} e {number2} é: {divide(number1, number2)}')
    
    handle_quit = input('Deseja sair da calculadora ? [s]im ').lower().startswith('s')
    
    if handle_quit:
        break
    