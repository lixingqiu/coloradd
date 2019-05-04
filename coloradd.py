"""
   This is the color increase command that matches the turtle drawing command.
   颜色增加与颜色设定命令,用来在海龟画图中做颜色渐变。
   作者:李兴球 2019/4/13晚更新
   本程序定义了两个函数，coloradd是用来增加颜色的，colorset是把一个整数转换成rgb三元色值。

"""
__author__ = "lixingqiu"
__blog__ = "www.lixingqiu.com"

import colorsys

def coloradd(color,dh):
    """color：three tuple color value，example：(1,1,0)，dh：0-1.0
       color是三元组,分别为0-1之间的浮点数。
       此函数把颜色转换成hls模式,对色度h进行增加色度dh的操作
       然后转换回去,dh是小于1的浮点数。       
    """
    if len(color)==3 :
        h,l,s, = colorsys.rgb_to_hls(color[0],color[1],color[2])
        h =  h + dh
        r,g,b = colorsys.hls_to_rgb(h,l,s)
        return r,g,b
    else:
        return color
addcolor = coloradd   # define alias name 定义别名

def colorset(color):
    """color：a integer from 1 to 360
       turn a interger in three tuple color value
       把一个整数转换成三元颜色值
    """
    color = color % 360
    color = color / 360.0    
    r,g,b = colorsys.hsv_to_rgb(color,1.0,1.0)
    
    return r,g,b
    
setcolor = colorset    # define alias name 定义别名

if __name__ == "__main__":

    import turtle
    screen = turtle.getscreen()
    screen.delay(0)
    screen.title("draw lollipop 画棒棒糖 by lixingqiu")
    c  = (1,0,0)                  # RGB红色
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




