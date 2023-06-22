number_str = input("Digite um número inteiro: ")
if number_str.isdigit():
    print(f'Número par: {(int(number_str) % 2) == 0}')
else:
    print("Você não digitou um número inteiro")


def returnHelloMessage(hour):
    if (hour > 23): return 'Hora inválida'
    if hour >= 0 and hour < 12: return 'Bom dia'
    if hour >= 12 and hour < 18: return 'Boa tarde'
    return 'Boa noite'

hours_str = input("Digite a hora (formarto: HH:MM): ")
if (':' in hours_str 
    and hours_str.split(':')[0].isdigit() 
    and hours_str.split(':')[1].isdigit()
    ):
    hour = hours_str.split(':')[0]
    print(f'Pela hora seria: {returnHelloMessage(int(hour))}')
else:
    print("Você não digitou uma hora válida")


name_user = input("Digite seu nome: ")

if len(name_user) < 5: print('Seu nome é curto')
if len(name_user) >= 5 and len(name_user) < 7: print('Seu nome é médio')
if len(name_user) > 6: print('Seu nome é longo')


