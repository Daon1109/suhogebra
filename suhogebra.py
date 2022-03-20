
import turtle
import planeDrawer

#setting pen
turtle.hideturtle()
turtle.shapesize(1)
turtle.speed(0)

#drawing coordinate plane
planeDrawer.draw()

#input and setting func_string
chasu = int(turtle.textinput("최고차항 입력","함수의 최고차항을 입력하세요"))
gaesu = []
func_string = ""
for i in range(chasu+1):
    #input process
    if (chasu-i) == 0:
        inputgaesu = float(turtle.textinput("계수입력 #"+str(i+1),"상수항의 계수를 입력하세요"))
    else:
        inputgaesu = float(turtle.textinput("계수입력 #"+str(i+1),str(chasu-i)+"차항의 계수를 입력하세요"))
    gaesu.append(inputgaesu)

    #setting func_string
    if gaesu[i] == 0:
        pass
    elif gaesu[i] == 1:
        if (chasu-i) == 1:
            func_string = func_string + "X" + " + "
        elif (chasu-i) == 0:
            func_string = func_string + str(gaesu[i])
        else:
            func_string = func_string + "X^" + str(chasu-i) + " + "
    else:
        if (chasu-i) == 1:
            func_string = func_string + str(gaesu[i]) + "X" + " + " 
        elif (chasu-i) == 0:
            func_string = func_string + str(gaesu[i])
        else:
            func_string = func_string + str(gaesu[i]) + "X^" + str(chasu-i) + " + "
    

#print given function in text
turtle.write("Function: "+func_string)

#input approximation limit
lim = float(turtle.textinput("정확도 입력(0 이상 10 이하 유리수)","정확도를 입력하세요(정확할수록 오래 걸림)"))

#goto start point
turtle.speed(0)
x = -300
ty = 0
for j in range(chasu+1):
    ty = ty + (gaesu[j]*pow(x,(chasu-j)))
turtle.goto(x,ty)


#drawing given function in the coordinate plane
turtle.down()
while x<300:
    y = 0
    for k in range(chasu+1):
        y = y + (gaesu[k]*pow(x,(chasu-k)))
    turtle.goto(x,y)
    x = x + lim


#window_problem_fix
window:object = turtle.Screen()
window.exitonclick()