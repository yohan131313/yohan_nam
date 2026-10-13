# 작성자 202611823 남요한
# 작성일 26.10.13 
# 앨범이 여러노래를 가질 수 있게 하는 프로그램

class Artist:
    def __init__(self, name):
        self.name = name

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class Album:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.tracks = []

    def add_track(self, song):
        self.tracks.append(song)

class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []

    def add_track(self, song):
        self.tracks.append(song)

lee = Artist("Lee's Band")
album = Album("첫 번째 앨범", lee)

song1 = Song("첫 번째 노래", lee)
song2 = Song("두 번째 노래", lee)

album.add_track(song1)
album.add_track(song2)

playlist = Playlist("애창곡")
playlist.add_track(song1)

print(f"플레이리스트 이름: {playlist.name}")
for song in playlist.tracks:
    print(f"노래 제목: {song.title}, 아티스트: {song.artist.name}")