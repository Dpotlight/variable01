import turtle          #turtle 라이브러리 (함수) 불러오기
t= turtle.Turtle()

size = int(input('집의 크기를 입력하세요: '))    #size입력받기     
house_color = str(input('그리는 색을 입력하세요: '))    #집 색깔 입력받기      
t.color(house_color)

t.width(54)  #펜의 두께설정하기      

t.fd(size)  #fd = 앞으로 이동시킴   
t.rt(90)    #90도 오른쪽으로 회전시킴   --> 정사각형      
t.fd(size)
t.rt(90)
t.fd(size)    
t.rt(90)         
t.fd(size)
t.rt(90)

t.fd(size)
t.lt(120)       #120도 왼쪽으로 회전시킴  --> 정삼각형       
t.fd(size)
t.lt(120)
t.fd(size)
t.lt(120)

#t.color(blue, yellow) 선색깔 --> 채우기색깔

