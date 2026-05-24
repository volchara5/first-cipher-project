print('Добро пожаловать в программу шифрования и дешифрования!')
text = input('Введите текст')
ru_alphabet = ''.join([chr(i) for i in range(ord('а'), (ord('я') + 1))])
ru_alphabet_up = ''.join([chr(i) for i in range(ord('А'), (ord('Я') + 1))])
en_alphabet = ''.join([chr(i) for i in range(ord('a'), (ord('z') + 1))])
en_alphabet_up = ''.join([chr(i) for i in range(ord('A'), (ord('Z') + 1))])
the_way = input('Выберите направление. Если вам нужно шифрование - нажмите "ш", а если вам нужно дешифрование - нажмите "д"')
language = input('Выберите язык. Если русский - то нажмите "р", а если английский - то нажмите "а"')
step = int(input('Назначьте шаг сдвига'))
answer = ''
for i in text:
    if i.isalpha():
        if the_way == 'ш':
            if language == 'р':
                if i.islower():
                    old_index = ru_alphabet.index(i)
                    new_index = (old_index + step) % 32
                    answer += ru_alphabet[new_index]
                else:
                    old_index = ru_alphabet_up.index(i)
                    new_index = (old_index + step) % 32
                    answer += ru_alphabet_up[new_index]
            else:
                if i.islower():
                    old_index = en_alphabet.index(i)
                    new_index = (old_index + step) % 26
                    answer += en_alphabet[new_index]
                else:
                    old_index = en_alphabet_up.index(i)
                    new_index = (old_index + step) % 26
                    answer += en_alphabet_up[new_index]
        else:
            if language == 'р':
                if i.islower():
                    old_index = ru_alphabet.index(i)
                    new_index = (old_index - step) % 32
                    answer += ru_alphabet[new_index]
                else:
                    old_index = ru_alphabet_up.index(i)
                    new_index = (old_index - step) % 32
                    answer += ru_alphabet_up[new_index]
            else:
                if i.islower():
                    old_index = en_alphabet.index(i)
                    new_index = (old_index - step) % 26
                    answer += en_alphabet[new_index]
                else:
                    old_index = en_alphabet_up.index(i)
                    new_index = (old_index - step) % 26
                    answer += en_alphabet_up[new_index]
    else:
        answer += i                
print(answer)