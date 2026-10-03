# 작성자 202611823 남요한
# 작성일 26.10.02 
# 문재: TV클래스 정의
"""TV클래스를 만들고 속성(체널번호,볼륨,전원상태)과
동작(켜기,끄기,채널변경하기,볼륨변경하기)을 만들기"""

class TV:
    def __init__(self):
        self.channel = 1
        self.volume = 10
        self.power = False

    def turn_on(self):
        self.power = True
        print("TV가 켜졌습니다.")

    def turn_off(self):
        self.power = False
        print("TV가 꺼졌습니다.")

    def change_channel(self, channel):
        self.channel = channel
        print(f"채널이 {self.channel}번으로 변경되었습니다.")

    def change_volume(self, volume):
        self.volume = volume
        print(f"볼륨이 {self.volume}으로 변경되었습니다.")

    def show_status(self):
        print(f"전원: {'켜짐' if self.power else '꺼짐'}")
        print(f"볼륨: {self.volume}")
        print(f"채널: {self.channel}")


tv = TV()
tv.turn_on()
tv.change_channel(7)
tv.change_volume(10)
tv.show_status()
tv.turn_off()
