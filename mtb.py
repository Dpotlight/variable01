#어떤 사람이 산악 자전거로 등산을 계획하고 있다. 평지에서는 시속20km/h가 가능하고 오르막에서는 10km/h
#내리막에서는 30km/h가 가능하다고 하자.
#위와 같은 경로를 자전거로 주행한다면 시간이 얼마나 걸릴까?


#시간 = 거리/속력



from math import *    #sqrt 혹은 math library 전부를 가져와도 상관없다.

#(10/20) + sqrt(3**2 + 4**2) / 10 + sqrt(3**2 + 4**2) / 30 + 8/20

time1 = 10/20
distance = sqrt(3**2 + 4**2)
time2 = distance / 10
time3 = distance / 30
time4 = 8/20

total = time1 + time2+ time3+ time4


print("자전거 주행 시간은 총", total, '시간입니다')
