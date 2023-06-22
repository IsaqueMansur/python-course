phrase = input('Digite a frase: \r\n').lower()
index = 0
most_repeated_letter = None
quantity_repeated = 0

while index < len(phrase):
    
    if phrase[index] == ' ': 
        index += 1
        continue
    
    if phrase.count(phrase[index]) > quantity_repeated:
        quantity_repeated = phrase.count(phrase[index])
        most_repeated_letter = phrase[index]
        
    if phrase.count(phrase[index]) == quantity_repeated:
        if phrase[index] not in most_repeated_letter:
            most_repeated_letter += f' | {phrase[index]}'
            
    index += 1 
    
print(f'\r\nLetra(s) mais repetida(s): {most_repeated_letter}')
print(f'Quantidade: {quantity_repeated}\r\n')