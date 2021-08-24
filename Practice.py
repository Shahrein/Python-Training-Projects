

while True:
    print('Who are you?: ')
    name = input()
    if name != 'evan':
        continue
    print('Hello there '+ name + '. What is the password: ')
    password = input()
    if password == 'evan12345':
        break
print('ok')