#기본

from random import randint
r = randint(0,2)

a = []
b = []


for i in range (3):
    a.append('x')
    b.append('?')

    
a[r] = 'o'


choice = int(input('숫자 입력(1~3): '))
print('{}번을 선택하셨습니다.\n'.format(choice))


show = r
while a[show] == 'o' or show == choice-1:
    show = randint(0,2)

    
b[show] = 'x'
print(b)
print('{}번은 꽝입니다.'.format(show+1))
change = input('{}번으로 선택을 바꾸시겠습니까?(y/n): '.format(6-choice-(show+1)))


if change == 'y':
    choice = 6-choice-(show+1)
    

print()    
print(a)
if a[choice-1] == 'o':
    print('선택하신 {}번은 당첨입니다.'.format(choice))
else:
    print('선택하신 {}번은 꽝입니다.'.format(choice))