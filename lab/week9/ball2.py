from tkinter import *
import time
import random

window = Tk()
window.title("공 30개 튀기기 게임")
canvas = Canvas(window, width=600, height=400, bg="white")
canvas.pack()

class Ball:
    def __init__(self, color, size):
        # 겹치지 않게 무작위 시작 위치 지정
        start_x = random.randint(0, 400)
        start_y = random.randint(0, 300)
        self.id = canvas.create_oval(start_x, start_y, start_x + size, start_y + size, fill=color)
        self.dx = random.randint(1, 10)
        self.dy = random.randint(1, 10)
        
    def move(self):
        canvas.move(self.id, self.dx, self.dy)
        x0, y0, x1, y1 = canvas.coords(self.id)
        
        # 위·아래 벽 충돌 시 부호 반전
        if y1 > canvas.winfo_height() or y0 < 0:
            self.dy = -self.dy
            
        # 왼쪽·오른쪽 벽 충돌 시 부호 반전
        if x1 > canvas.winfo_width() or x0 < 0:
            self.dx = -self.dx

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
ballList = []

# 공 30개 생성
for i in range(30):
    ballList.append(Ball(random.choice(colors), 40))

# 애니메이션 반복문
while True:
    for i in range(30):
        ballList[i].move()
    window.update()
    time.sleep(0.03)

window.mainloop()