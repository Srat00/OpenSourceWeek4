import turtle
import random
from tkinter.simpledialog import *

inputStr = ''
sWidth, sHeight = 300, 300
tX, tY, tSize = [0] * 3

turtle.title('글자쓰는 거북이')
turtle.shape('turtle')
turtle.setup(width=sWidth + 50, height=sHeight + 50)
turtle.screensize(sWidth, sHeight)
turtle.penup()

inputStr = askstring('문자열 입력', '거북이가 쓸 문자열을 입력')

for ch in inputStr:
    tX = random.randrange(-sWidth/2, sWidth/2)
    tY = random.randrange(-sHeight/2, sHeight/2)
    r = random.random()
    g = random.random()
    b = random.random()
    txtSize = random.randrange(10, 50)
    
    turtle.goto(tX, tY)
    
    turtle.pencolor((r, g, b))
    turtle.write(ch, font=('맑은 고딕', txtSize, 'bold'))
    
turtle.done()