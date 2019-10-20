# coloradd
 This is the color increase command that matches the python turtle drawing command.
example code:
    """
        pip install coloradd
   
    """

    import turtle
    from coloradd import *
    screen = turtle.getscreen()
    screen.delay(0)
    screen.colormode(255)         # 使用coloradd模块需要设置颜色模式为255
    screen.title("draw lollipop 画棒棒糖 by lixingqiu")
    c  = (255,0,0)                  # RGB红色
    turtle.ht()                   # 隐藏海龟
    turtle.penup()                # 抬起笔来
    turtle.goto(0,100)            # 定位坐标
    turtle.pendown()              # 落下画笔
    for i in range(300):          # 迭代变量
        turtle.width(i/10)        # 画笔笔宽
        turtle.fd(i/10)           # 海龟前进
        turtle.rt(10)             # 海龟右转
        c = coloradd(c,0.01)      # 颜色增加
        turtle.pencolor(c)        # 画笔颜色
        
    turtle.penup()                # 抬起笔来
    turtle.goto(0,100)            # 定位坐标
    turtle.setheading(-90)        # 方向向下
    turtle.color("brown")         # 画笔颜色
    turtle.pendown()              # 落下笔来
    turtle.fd(340)                # 前进440
    turtle.penup()                # 抬起笔来
    turtle.fd(28)                 # 前进28
    turtle.color("gray")          # 画笔颜色
    turtle.write("www.lixingqiu.com",align='center',font=("",12,"normal"))
    screen.mainloop()
