import random


effect = ['R', 'P', 'S']



rule1 = ['R', 'P'] 
rule2 = ['S', 'R']
rule3 = ['P', 'S']


def choose():
    choice = "'R' for 'rock' \n'P' for 'paper', \n'S' for 'scissors'"
    user_effect = input(f'Pick an option among R, P, S:\n{choice}\n:')
    return user_effect.upper()


def check_moves(sys_effect, curr, rule):
    effect = rule  # sort list according to increasing value
    if effect.index(curr) == effect.index(sys_effect):
        sys_effect = random.choice(effect)
        return True

    elif effect.index(curr) > effect.index(sys_effect):
        print('You WIN!!!')
        print(rule)
        return False

    elif effect.index(sys_effect) > effect.index(curr):
        print(rule)
        print('A.I WIN!!!')
        return False

game = True


while game:
    curr = choose()
    if curr.upper() not in effect:
        print('Input correct value: ')
        continue
    
    sys_effect = random.choice(effect)
    if sys_effect in rule1 and curr in rule1:
        rule = rule1
    elif sys_effect in rule2 and curr in rule2:
        rule = rule2
    elif sys_effect in rule3 and curr in rule3:
        rule = rule3

    print(f'Player ({curr}) : Computer ({sys_effect})')
    game = check_moves(sys_effect, curr, rule)






