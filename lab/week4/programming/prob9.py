# 작성자 202611823 남요한
# 작성일 26.10.03
# 문제: 프로그래밍09 Turtle클래스

import turtle
if __name__ == '__main__':

    lee = turtle.Turtle()
    lee.shape("turtle")

    lee.forward(80)
    lee.right(90)
    lee.forward(40)
    lee.left(90)
    lee.forward(80)

    park = turtle.Turtle()
    park.shape("turtle")
    park.color("blue")

    park.setheading(180)

    park.forward(80)
    park.right(90)
    park.forward(40)
    park.left(90)
    park.forward(80)

    turtle.done()