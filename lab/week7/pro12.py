# 작성자 202611823 남요한
# 작성일 26.10.14
# 단어 랜덤출력
import random
box=["학습","컴퓨터","마우스","메인보드","키보드",'헤드셋','마이크','드래그''그래픽카드','cpu']
randomBox = [random.choice(box) for i in range(3)]
print(randomBox)