import random
import time


def fRollDice(Dices=3, pointer=None):
    print('<' * 5, 'Role the Dice', '>' * 5)
    if pointer is None:
        pointer = []
    while Dices:
        pointer.append(random.randrange(1, 7))
        Dices -= 1
    else:
        return pointer


def fRollResult(pointer):
    vSum = sum(pointer)
    isBig = 11 <= vSum <= 18
    isSmall = 3 <= vSum <= 10
    if isBig:
        return 'b'
    elif isSmall:
        return 's'


def fmoneyPocket(youWin, rate, money=1000):
    if youWin:
        money += rate
    else:
        money -= rate
        if money < 0:
            money = 0
    return money


def fStartGame(money):
    while money > 0:
        print('<' * 5, 'Game Start!', '>' * 5)
        choice = ['b', 's']
        vAns = input('Guess Big(b) or Small(s):')
        # vAns = int(vAns)
        if vAns == '-1':
            return print('Your current money : ', money)
        else:
            vRate = int(input('How much you want to bet ?(>0,integer)-'))
        
        if vAns in choice and vRate == abs(vRate // 1):
            pointer = fRollDice()
            youWin = vAns == fRollResult(pointer)
            swinLoss = ['You Loss!', 'You Win!']
            print('The pointers are ', pointer, swinLoss[youWin])
            money = fmoneyPocket(youWin, vRate, money)
            sgainLost = ['lost', 'gained']
            print('you {} {rate}, you have {money} now.'.format(sgainLost[youWin], rate=vRate, money=money))
        else:
            print('Not valid input~ \n if you want to exit, please input \'-1\'\n\n')
    else:
        print('Game Over')


t0 = time.clock()
fStartGame(1000)
t1 = time.clock() - t0
print(t1, 'seconds process time.')
