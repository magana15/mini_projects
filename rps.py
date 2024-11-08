import random
choices = ("r", "p", "s")
quit = ('n')
emojis = {'r':'🥌', 'p':'📄', 's':'✂'}

while True:
    uc = input('Rock, paper, scissors? (r/p/s): ').lower()
    if uc not in choices:
        if uc in quit:
            print('thank you for playing, goodbye')
            break
        print('invalid choice')
        continue

    cc = random.choice(choices)

    print(f'computer chose {emojis[cc]}')
    print(f'You chose {emojis[uc]}')
    if cc == uc:
        print('a tie')

        

    elif cc == 'r' and uc == 'p' or cc == 'p' and uc == 's' or cc == 's' and uc == 'r':
        print('you win')
    else:
        print('You lose')
        
