#바꿨을 때 vs 안바꿨을 때 확률 계산

from random import randint

c_win = 0
c_lose = 0
nc_win = 0
nc_lose = 0
change = 0

c_win_rate = []
nc_win_rate = []

for m in range (1000):

    r = randint(0,2)

    a = []
    b = []


    for i in range (3):
        a.append('x')


    a[r] = 'o'


    choice = randint(1,3)


    show = r

    while a[show] == 'o' or show == choice-1:
        show = randint(0,2)


    if change%2 == 1:
        choice = 6-choice-(show+1)



    if a[choice-1] == 'o':
        if change%2 == 1:
            c_win = c_win+1
        else:
            nc_win = nc_win+1
    else:
        if change%2 == 1:
            c_lose = c_lose +1
        else:
            nc_lose = nc_lose+1

            

    if change%2 == 1:
        c_win_rate.append(round((c_win / (c_win+c_lose)*100),2))
    else:
        nc_win_rate.append(round((nc_win / (nc_win+nc_lose)*100),2))
                           
                           
    change = change+1
    
        
        
print('바꿨을 때\n승:{}  패:{}  승률:{}%'.format(c_win, c_lose, round((c_win / (c_win+c_lose)*100),2)))
print('\n안바꿨을 때\n승:{}  패:{}  승률:{}%'.format(nc_win, nc_lose, round((nc_win / (nc_win+nc_lose)*100),2)))


import matplotlib.pyplot as plt

plt.plot(c_win_rate)
plt.plot(nc_win_rate)
plt.ylim(0,100)
plt.show()