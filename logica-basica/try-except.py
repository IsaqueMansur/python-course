float_number = 0

while(True):
    try:
        str_number = input("Digite um número para ser dobrado: ")   
        float_number = float(str_number)
        print(f'O dobro de {float_number} é {float_number *2:.1f}')
        break
    except:
        print('Você não digitou um número válido.')
        continue