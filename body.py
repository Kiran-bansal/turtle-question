import turtle

def draw_body1():
    window=turtle.Screen()
    window.bgcolor("white")
    draw_kiran()
    window.exitonclick()
    
def draw_kiran():
    kiran=turtle.Turtle()
    kiran.shape("turtle")
    kiran.color("red")
    draw_head(kiran)
    draw_body(kiran)
    draw_arm(kiran)
    draw_leg1(kiran)
    draw_leg2(kiran)
    
def draw_head(kiran):
    kiran.circle(60)
    kiran.speed(3)
    kiran.right(60)

def draw_body(kiran):
    num=0
    while num<3:
        kiran.forward(150)
        kiran.right(120)
        kiran.speed(1)
        num+=1
        
def draw_arm(kiran):
    kiran.forward(60)
    kiran.left(60)
    kiran.forward(60)
    
    
    kiran.backward(60)
    kiran.right(60)
    kiran.backward(60)
    
    kiran.right(60)
    
    kiran.forward(60)
    kiran.right(60)
    kiran.forward(60)
    
    
    kiran.backward(60)
    kiran.left(60)
    kiran.forward(90)
    
def draw_leg1(kiran):
    kiran.left(120)
    kiran.forward(40)
    kiran.right(120)
    kiran.forward(120)
    draw_foot1(kiran)
    
def draw_leg2(kiran):
    kiran.right(180)
    kiran.forward(120)
    kiran.right(60)
    kiran.forward(70)
    kiran.right(60)
    kiran.forward(120)
    draw_foot2(kiran)
    
def draw_foot1(kiran):
    kiran.color("blue")
    num=0
    while num<4:
        kiran.forward(20)
        kiran.left(90)
        num+=1
        
def draw_foot2(kiran):
    kiran.color("blue")
    num=0
    while num<4:
        kiran.forward(20)
        kiran.left(90)
        num+=1
        
draw_body1()
    
