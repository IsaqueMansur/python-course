runMessageMovimentSystem = True

while(runMessageMovimentSystem):
    print("\r\n")
    user_input = input("Você deseja 'entrar' ou 'sair' do sistema ? \r\n")
    if user_input.lower() == 'entrar':
        print('Entrando no sistema')
        runMessageMovimentSystem = False
        break
    elif user_input.lower() == 'sair':
        print('Saindo do sistema')
        runMessageMovimentSystem = False
        break
    else:
        print('Não reconheci o comando.')
        continue

print('Programa finalizado')