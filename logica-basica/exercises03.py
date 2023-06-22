import random
words = ['abelha', 'caneta', 'pneu', 'leque', 'orelha']
random_number = random.randint(0, 4)
secret_word = words[random_number]
hit = False
attempts = 0
kicked_letters = []

print('PALAVRA SECRETA')
while not hit:
    chosen_letter = input('Digite uma letra e te falarei se ela existe na palavra procurada ou não: ').lower()
    
    if len(chosen_letter) > 1 or chosen_letter.isdigit():
        print('\r\nVocê não digitou uma letra válida (Digite apenas uma letra, não digite números)\r\n')
        continue
    
    
    if chosen_letter in kicked_letters:
        print('\r\nVocê já chutou essa letra, tente outra \r\n')
        continue
    
    kicked_letters.append(chosen_letter)
        
    if chosen_letter in secret_word:
        print(f'\r\nBoa ! \r\nA letra "{chosen_letter}" pertence a palavra secreta\r\n')
    else:
        print(f'\r\nIxii :( \r\nA letra "{chosen_letter}" não pertence a palavra secreta\r\n')
        
    chosen_word = input('Tenta aí !\r\nDigite a possível palavra secreta: ').lower()
    attempts += 1
    
    if chosen_word == secret_word:
        print(f'\r\nParabéns, você acertou !\r\nTentativas: {attempts}\r\n\r\n-----Game finalizado-----\r\n')
        input('\r\nPressione qualquer tecla para sair...')
        break
    else:
        print(f'Você errou, tentativas: {attempts}')
        continue
        
    
    
