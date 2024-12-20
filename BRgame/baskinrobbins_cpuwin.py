#cpu 필승

from random import randint
from time import sleep


lim = int(input('숫자 설정: '))
c_num = int(input('숫자 개수 설정: '))


win = 0

n = 1
cpunum = (c_num+1)*(n-1)+(lim-1)%(c_num+1)
count = 0

n = 2

if cpunum != 0:
    print('\033[34m' + '\n컴퓨터가 선공입니다.' + '\033[0m')
    print('\n\ncpu: {}'.format(cpunum))
    print('\033[35m' + 'number: ' + '\033[0m', end='')

    for k in range (cpunum):
        count = count + 1
        print('\033[35m' + str(count) + '\033[0m', end=' ')
        
        
else:
    print('\033[34m' + '\n플레이어가 선공입니다.' + '\033[0m')

print()

while count < lim and win == 0:

    next = 0

    if count != lim-1:
        usernum = int(input('\nyou: '))

        if usernum >= 1 and usernum <= c_num and win == 0:
            print('\033[31m' + 'number: ' + '\033[0m', end='')

            for i in range (usernum):
                count = count + 1
                print('\033[31m' + str(count) + '\033[0m', end=' ')
                
            if count >= lim:
                print('\n\nYou Lose..')
                win = 1
                
            else:
                next = 1

        else:
            print('\033[34m' + '1에서 {} 사이의 숫자를 입력하세요.'.format(c_num) + '\033[0m')

    else:
        print('\033[34m' + '\nYou Lose..' + '\033[0m')
        win = 1

        
    cpunum = lim
        
    if next == 1 and win == 0:

        if count != lim-1:

            while count + cpunum >= lim:
                while count + cpunum != (c_num+1)*(n-1)+(lim-1)%(c_num+1):
                    cpunum = randint(1,c_num) 

            print('\n\ncpu: {}'.format(cpunum))
            print('\033[35m' + 'number: ' + '\033[0m', end='')

            for i in range (cpunum):
                count = count + 1
                print('\033[35m' + str(count) + '\033[0m', end=' ')
            print()
            n = n+1
               
        else:
            print('\033[34m' + '\n\nYou Win!' + '\033[0m')
            win = 1
