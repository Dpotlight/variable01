import turtle
t = turtle.Turtle()
t.shape("turtle")    #거북이모양표시하기   
t.color('orange', 'yellow')  #  색바꾸기 , but 채우기 칸이 없어서 yellow는 나타나지않음.
t.width(22)   # 선 너비 변경하기      

t.up()                 # 붓 들기
t.goto(-200,-200)     #이 좌표로 이동   
t.down()              #붓 내리기     
t.fd(300)              # 앞으로 300만큼 그리기      

t.up()                 #붓 들기    
t.goto(-200,100)     # 처음 시작좌표보다 y좌표만위로 이동    
t.down()             #붓 내리기       
t.fd(300)           #그리기     

