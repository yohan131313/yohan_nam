# 작성자 202611823 남요한
# 작성일 26.10.03
# 문제: 프로그래밍08 Song클래스

class Song:
    def __init__(self, title, lyrics):
        self.title = title
        self.lyrics = lyrics

    def sing(self):
        for line in self.lyrics:
            print(line)


if __name__ == '__main__':
    aSong = Song("TWINKLE, TWINKLE, LITTLE STAR", [
        "TWINKLE, twinkle, little star,",
        "How I wonder what you are!",
        "Up above the world so high,",
        "Like a diamond in the sky."
    ])
    aSong.sing()