def start(repeat, a_ap, a_num, a_icr,
          b_ap, b_num, b_age_max, b_age_min, b_hunt, b_hgr, b_bir,
          c_ap, c_num, c_age_max, c_age_min, c_hunt, c_hgr, c_bir, c_net):
  


  from random import randint as rd

  #<생산자>
  na = a_num
  ga_ap = a_ap
  ga = [na]
  sc_ga1 = 1000/na
  ga1 = [na*sc_ga1]
  ga2 = []
  ga_0 = -10

  ga2.append(None)

  #<1차 소비자>
  nb = b_num
  lb = []
  gb_ap = b_ap
  gb = [nb]
  sc_gb1 = 1000/nb
  gb1 = [nb*sc_gb1]
  gb2 = []
  gb_0 = -10
  gb3_ys = []
  gb3_sc = sc_ga1*2
  gb4_bir = []
  gb4_hg = []
  gb4_hted = []

  gb2.append(None)

  for i in range(1,b_age_max+1):
    lb.append([i,nb//b_age_max])
  lb[0][1] += (nb % b_age_max)

  for i in range(len(lb)):
    gb3_ys.append(lb[i][1]*gb3_sc) 

  #<2차 소비자>
  nc = c_num
  lc = []
  gc_ap = c_ap
  gc = [nc]
  sc_gc1 = 1000/nc
  gc1 = [nc*sc_gc1]
  gc2 = []
  gc_0 = -10
  gc3_ys = []
  gc3_sc = sc_gc1*2
  gc4_bir = []
  gc4_hg = []
  gc4_hted = []

  gc2.append(None)

  for i in range(1,c_age_max+1):
    lc.append([i,nc//c_age_max])
  lc[0][1] += (nc % c_age_max)

  for i in range(len(lc)):
    gc3_ys.append(lc[i][1]*gc3_sc)


  #<시작>
  for m in range(repeat):

  #<생산자>
    na += a_icr

  #<1차 소비자>
    gb4_hg_t = 0
    gb4_bir_t = 0

    #사냥
    for i in range(nb):
      if (rd(1,100) <= b_hunt) and (na != 0):
        na -= 1

    #굶어죽음
      else:
        if rd(1,100) <= b_hgr:
          nb -= 1
          gb4_hg_t -= 1
          r = rd(0,b_age_max-1)

          while lb[r][1] == 0:
            r = rd(0,b_age_max-1)

          lb[r][1] -= 1 

    #번식
    for i in range(int(nb/2)):
      if rd(1,100) <= b_bir:
        nb += 1
        gb4_bir_t += 1
        lb[rd(b_age_min,b_age_max-1)][1] += 1

    nb -= lb[0][1]

    #사망(수명)
    for i in range(len(lb)-1):
      lb[i][1] = lb[i+1][1]
    lb[len(lb)-1][1] = 0

  #<2차 소비자>
    gb4_hted_t = 0

    gc4_hg_t = 0
    gc4_bir_t = 0

    #사냥(먹이그물x)
    if c_net == 0:

      for i in range(nc):
        if (rd(1,100) <= c_hunt) and (nb != 0):
          nb -= 1
          gb4_hted_t -= 1
          r = rd(0,b_age_max-1)

          while lb[r][1] == 0:
            r = rd(0,b_age_max-1)

          lb[r][1] -= 1

    #굶어죽음(먹이그물x)
        else:
          if rd(1,100) <= c_hgr:
            nc -= 1
            gc4_hg_t -= 1
            r = rd(0,c_age_max-1)

            while lc[r][1] == 0:
              r = rd(0,c_age_max-1)

            lc[r][1] -= 1       


    #사냥(먹이그물o)
    if c_net == 1:

      for i in range(nc):

        if (rd(1,100) <= c_hunt) and ((na != 0) or (nb != 0)):

          if (na != 0) and (nb != 0):

            if rd(1,2) == 1:
              na -= 1

            else:
              nb -= 1
              gb4_hted_t -= 1
              r = rd(0,b_age_max-1)

              while lb[r][1] == 0:
                r = rd(0,b_age_max-1)

              lb[r][1] -= 1

          elif nb == 0:
            na -= 1

          else:
            nb -= 1
            gb4_hted_t -= 1
            r = rd(0,b_age_max-1)

            while lb[r][1] == 0:
              r = rd(0,b_age_max-1)

            lb[r][1] -= 1

    #굶어죽음(먹이그물o)
        else:
          if rd(1,100) <= c_hgr:
            nc -= 1
            gc4_hg_t -= 1
            r = rd(0,c_age_max-1)

            while lc[r][1] == 0:
              r = rd(0,c_age_max-1)

            lc[r][1] -= 1 

    #번식
    for i in range(int(nc/2)):
      if rd(1,100) <= c_bir:
        nc += 1
        gc4_bir_t += 1
        lc[rd(c_age_min,c_age_max-1)][1] += 1

    nc -= lc[0][1]

    #사망(수명)
    for i in range(len(lc)-1):
      lc[i][1] = lc[i+1][1]
    lc[len(lc)-1][1] = 0

  #<Cycle당 값 정리>
    ga.append(na)
    gb.append(nb)
    gc.append(nc)

    ga1.append(na*sc_ga1)
    gb1.append(nb*sc_gb1)
    gc1.append(nc*sc_gc1) 

    ga2.append(ga1[-1] - ga1[-2])
    gb2.append(gb1[-1] - gb1[-2])
    gc2.append(gc1[-1] - gc1[-2])

    for i in range(len(lb)):
      gb3_ys.append(lb[i][1]*gb3_sc) 

    for i in range(len(lc)):
      gc3_ys.append(lc[i][1]*gc3_sc)


    gb4_bir.append(gb4_bir_t*1/1000)
    gb4_hg.append(gb4_hg_t*1/1000)
    gb4_hted.append(gb4_hted_t*1/1000)

    gc4_bir.append(gc4_bir_t*1/1000)
    gc4_hg.append(gc4_hg_t*1/1000)


    if ga[-2] != 0 and ga[-1] == 0:
      ga_0 = len(ga)-1

    if gb[-2] != 0 and gb[-1] == 0:
      gb_0 = len(gb)-1

    if gc[-2] != 0 and gc[-1] == 0:
      gc_0 = len(gc)-1


    if nb == 0 and nc == 0:
      break

  #<그래프 처리>
  g2_ylim = max([max(gb1), max(gc1)])

  gb3_x = []
  gb3_y = []
  n = 0
  for i in range(len(gb)):
    for j in range(len(lb)):
      gb3_x.append(n)
      gb3_y.append(j+1)
    n += 1

  gc3_x = []
  gc3_y = []
  n = 0
  for i in range(len(gc)):
    for j in range(len(lc)):
      gc3_x.append(n)
      gc3_y.append(j+1)
    n += 1

  #<그래프 출력>
  import matplotlib.pyplot as plt
  plt.rc('font', family='NanumBarunGothic')

  g_xlim = len(ga)

  if ga_ap != 1:
    ga = ga1 = ga2 = []

  if gb_ap != 1:
    gb = gb1 = gb2 = []

  if gc_ap != 1:
    gc = gc1 = gc2 = []


  plt.figure(figsize=(15, 23))
  plt.subplots_adjust(hspace=0.3)

  #개체수
  plt.subplot(711)
  plt.xlim([-2, g_xlim])
  plt.plot(ga, label='생산자')
  plt.plot(gb, label='1차소비자')
  plt.plot(gc, label='2차소비자')
  plt.axvline(ga_0, color='#73a1c7', linestyle='--', linewidth=1)
  plt.axvline(gb_0, color='#FFA575', linestyle='--', linewidth=1)
  plt.axvline(gc_0, color='#73c791', linestyle='--', linewidth=1)
  plt.legend(loc='upper right')
  plt.title('개체수')

  #개체수(상대값)
  plt.subplot(712)
  plt.xlim([-2, g_xlim])
  plt.ylim([0, g2_ylim+100])
  plt.plot(ga1, label='생산자')
  plt.plot(gb1, label='1차소비자')
  plt.plot(gc1, label='2차소비자')
  plt.axvline(ga_0, color='#73a1c7', linestyle='--', linewidth=1)
  plt.axvline(gb_0, color='#FFA575', linestyle='--', linewidth=1)
  plt.axvline(gc_0, color='#73c791', linestyle='--', linewidth=1)
  plt.legend(loc='upper right')
  plt.title('개체수(상대값)')

  #개체수 증가/감소율(평균변화율)
  plt.subplot(713)
  
  plt.xlim([-2, g_xlim])
  plt.plot(ga2, label='생산자')
  plt.plot(gb2, label='1차소비자')
  plt.plot(gc2, label='2차소비자')
  plt.axvline(ga_0, color='#73a1c7', linestyle='--', linewidth=1)
  plt.axvline(gb_0, color='#FFA575', linestyle='--', linewidth=1)
  plt.axvline(gc_0, color='#73c791', linestyle='--', linewidth=1)
  plt.axhline(0, color='black', linestyle='--', linewidth=1)
  plt.legend(loc='upper right')
  plt.title('개체수 증가/감소율(평균변화율)')

  if gb_ap == 1:
    from matplotlib.colors import LinearSegmentedColormap
    colors = ['#FFDECC','#FF5900','#E65000','#CC4700','#993600']
    cmap_gb3 = LinearSegmentedColormap.from_list('my_cmap',colors,gamma=2)

  #1차소비자 연령분포
    plt.subplot(714)
    plt.xlim([-2, g_xlim])
    plt.scatter(gb3_x, gb3_y, s=gb3_ys, c=gb3_ys, cmap=cmap_gb3, alpha=0.7)
    plt.axvline(ga_0, color='#73a1c7', linestyle='--', linewidth=1)
    plt.axhline(b_age_min, color='gray', linestyle='--', linewidth=1)
    plt.title('연령분포 - 1차소비자')

  #1차소비자 증가/감소비율
    plt.subplot(715)
    plt.xlim([-2, g_xlim])
    plt.plot(gb4_bir, color='#FF5200', label='출생')
    plt.plot(gb4_hg, color='#993100', label='굶어죽음')
    plt.plot(gb4_hted, color='#000000', label='사냥당함')
    plt.axvline(ga_0, color='#73a1c7', linestyle='--', linewidth=1)
    plt.axvline(gb_0, color='#FFA575', linestyle='--', linewidth=1)
    plt.axhline(0, color='black', linestyle='--', linewidth=1)
    plt.legend(loc='upper right')
    plt.title('개체수 증가/감소비율 - 1차소비자')

  if gc_ap == 1:
    from matplotlib.colors import LinearSegmentedColormap
    colors = ['#ACE6C0','#00CC47','#00B33E','#009936','#006624']
    cmap_gc3 = LinearSegmentedColormap.from_list('my_cmap',colors,gamma=2)

  #2차소비자 연령분포
    plt.subplot(716)
    plt.xlim([-2, g_xlim])
    plt.scatter(gc3_x, gc3_y, s=gc3_ys, c=gc3_ys, cmap=cmap_gc3, alpha=0.7)
    plt.axvline(gb_0, color='#FFA575', linestyle='--', linewidth=1)
    plt.axhline(c_age_min, color='gray', linestyle='--', linewidth=1)
    plt.title('연령분포 - 2차소비자')

  #2차소비자 증가/감소비율
    plt.subplot(717)
    plt.xlim([-2, g_xlim])
    plt.plot(gc4_bir, color='#00D22A', label='출생')
    plt.plot(gc4_hg, color='#007417', label='굶어죽음')
    plt.axvline(gb_0, color='#FFA575', linestyle='--', linewidth=1)
    plt.axvline(gc_0, color='#73c791', linestyle='--', linewidth=1)
    plt.axhline(0, color='black', linestyle='--', linewidth=1)
    plt.legend(loc='upper right')
    plt.title('개체수 증가/감소비율 - 2차소비자')

  plt.show()