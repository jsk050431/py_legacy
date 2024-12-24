from random import randint
a = int(0)
b = int(0)
c = int(0)

while a == b or a == c or b == c: #같은 수가 나오는 것을 방지.
  a = randint(1, 9) #백의 자리 숫자
  b = randint(0, 9) #십의 자리 숫자
  c = randint(0, 9) #일의 자리 숫자
#print(a, b, c,)

att = input('시도 횟수 설정 : ')


tryy = int(att)
tryy2 = int(att)

print()
print()
print('적절한 추리로 세 자리 숫자를 맞춰 보세요. 기회는 총', tryy, '번!')
print('그럼, 시작!')
print()
 

s = int(0) #밑의 조건 사용을 위한 임시 정의.
while s != 3 and tryy != 0:
  
  cn = 0 #bool 함수 사용을 위한 임시 정의
  while bool(cn) != True:
    an = input('숫자 입력 (세 자리 수) : ')
    num = int(an)
      
    #사용자가 입력한 수를 각 자릿수대로 분리. 나머지 값 함수 이용
    ccc = int(num%10)
    bbb = int((num%100-ccc)/10)
    aaa = int((num-10*bbb-ccc)/100)
    
    #입력한 숫자가 서로 중복되지 않는지 확인.
    if aaa == bbb or bbb == ccc or aaa == ccc:
      print()
      print()
      print('서로 중복되지 않는 세 자리 숫자를 입력해 주세요.')
      cn = 0

    elif 100 <= num <= 999: #제대로 된 세 자리 숫자인지 판별.
      cn = 1
   
    else:
      print()
      print()
      print('제대로 된 세 자리 숫자를 입력해 주세요.')
      cn = 0

  s = int(0) #스트라이크

  if a == aaa:
    s = s+1

  if b == bbb:
    s = s+1

  if c == ccc:
    s = s+1

  print(s, 's')


  ba = int(0) #볼

  if a == bbb:
    ba = ba+1

  if a == ccc:
    ba = ba+1

  if b == aaa:
    ba = ba+1

  if b == ccc:
    ba = ba+1

  if c == bbb:
    ba = ba+1

  if c == aaa:
    ba = ba+1

  print(ba, 'b')

  tryy = tryy-1 #남은 기회 계산
  print('남은 기회 :',tryy )
  print()
  print()

if s == 3: #승리
  print()
  print()
  print('정답!')
  print(tryy2-tryy, '번만에 맞추셨네요!')
else: #패배
  print()
  print()
  print('정답 : ', 100*a+10*b+c)
  print('게임 오버..')

  