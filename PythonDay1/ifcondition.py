n = 5
if n == 10:
    print('n equal to 10')
else:
    print('n is something else except 10')

name = 'James'
if name == 'Mateo':
    print('Hi, Mateo.')
else:
    print('Who are you?') 

money = 300
if money >= 350:
    print('You can buy an iPad')
else:
    print('You don\'t have enough money to buy an iPad')


print('Welcome to marcuscode\'s game')
level = input('Enter level (1 - 4): ')

if level == '1':
    print('Easy')
elif level == '2':
    print('Medium')
elif level == '3':
    print('Hard')
elif level == '4':
    print('Expert')
else:
    print('Invalid level selected')

# Ternary Operation
x, y = 50, 25
small = x if x < y else y
print(small)