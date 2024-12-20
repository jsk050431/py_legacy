#디자인

from random import randint

r = randint(0,2)

a = []
b = []


for i in range (3):
    a.append('x')
    b.append('?')

    
a[r] = 'o'


for k in range (len(b)):
    print('[{}] '.format(b[k]) , end = '')
        
choice = int(input('\n숫자 입력(1~3): '))
print('{}번을 선택하셨습니다.\n'.format(choice))


show = r

while a[show] == 'o' or show == choice-1:
    show = randint(0,2)

    
b[show] = 'x'



for k in range (len(b)):
    if k+1 == choice:
        print('\033[34m' + '[{}] '.format(b[k]) + '\033[0m' , end = '')
    else:
        print('[{}] '.format(b[k]) , end = '')



print('\n{}번은 꽝입니다.'.format(show+1))
change = input('{}번으로 선택을 바꾸시겠습니까?(y/n): '.format(6-choice-(show+1)))


if change == 'y':
    choice = 6-choice-(show+1)
    

print()    
for k in range (len(a)):
    if k+1 == choice:
        print('\033[34m' + '[{}] '.format(a[k]) + '\033[0m' , end = '')
    else:
        print('[{}] '.format(a[k]) , end = '')


if a[choice-1] == 'o':
    print('\n선택하신 {}번은 당첨입니다.'.format(choice))
else:
    print('\n선택하신 {}번은 꽝입니다.'.format(choice))