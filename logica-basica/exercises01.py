while(True):
    name_user = input('Digite seu nome: ')
    age_user = input('Digite sua idade: ')
    if (name_user and age_user):
        reversed_name_user = name_user[::-1]
        name_user_has_spaces = (' ' in name_user)
        length_of_name_user = len(name_user) 
        first_letter_name_user = name_user[0]
        last_letter_name_user = name_user[-1]
        print(f'\r\n Nome: {name_user} \r\n Nome Invertido: {reversed_name_user} \r\n Tamanho do nome: {length_of_name_user} caractéres \r\n Primeira letra: {first_letter_name_user} \r\n Última letra: {last_letter_name_user} \r\n Possui espaço: {name_user_has_spaces} \r\n')
        break
    else:
        print('Desculpe, você não preencheu todos os campos')
        continue
    