from maincode import start

#먹이그물o(2차소비자가 생산자를 먹을 때)

#반복횟수
repeat = 50

#생산자
a_ap = 1          #그래프출력여부
a_num = 100000    #개체수
a_icr = 10000     #증가

#1차소비자
b_ap = 1          #그래프출력여부
b_num = 40000     #개체수
b_age_max = 20    #최대수명
b_age_min = 17    #최소수명
b_hunt = 50       #사냥성공(%)
b_hgr = 41        #굶어죽음(%)
b_bir = 52        #번식(%)

#2차소비자
c_ap = 1          #그래프출력여부
c_num = 5000      #개체수
c_age_max = 30    #최대수명
c_age_min = 27    #최소수명
c_hunt = 50       #사냥성공(%)
c_hgr = 41        #굶어죽음(%)
c_bir = 52        #번식(%)
c_net = 1         #먹이그물(생산자포식)



start(repeat, a_ap, a_num, a_icr,
      b_ap, b_num, b_age_max, b_age_min, b_hunt, b_hgr, b_bir,
      c_ap, c_num, c_age_max, c_age_min, c_hunt, c_hgr, c_bir, c_net)