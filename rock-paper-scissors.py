import random
input1 = input ('do you want to play rock, paper, scissors VS the super computer?')
var1 = input('Rock, Paper or Scissors?').lower().strip()



while input1 != 'no':
    random_var = random.randint(1, 3)
    if random_var == 1:
        var2 = 'rock'
    elif random_var == 2:
        var2 = 'paper'
    else:
        var2 = 'scissors'

    if var1 == 'rock' and var2 == 'scissors':
        print (f'{var1} beats {var2}')
        print ('you win')

    elif var1 == 'paper' and var2 == 'rock':
        print(f'{var1} beats {var2}')
        print('you win')

    elif var1 == 'scissors' and var2 == 'paper':
        print(f'{var1} beats {var2}')
        print('you win')

    elif var1 == var2:
        print(f'{var1} and {var2}')
        print('wow you drew! what are the chances')
    else:
        print (f'{var1} doesnt beat {var2}')
        print ('you lose')
    input1 = input('do you want to play again?')
    var1 = input('Rock, Paper or Scissors?').lower().strip()
