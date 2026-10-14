# 작성자 202611823 남요한
# 작성일 26.10.13
# 문제: 파일에서 데이터를 읽을 때, 파일이 없으면 IOError가 발생한다. 이것을 try와 except로 처리해보자.

while True:
    filename = input("입력 파일 이름: ")
    try:
        infile = open(filename, "r")
        print(f"파일이 성공적으로 열렸습니다.")
        infile.close()
        break
    except IOError:
        print(f"파일 {filename}이 없습니다. 다시 입력하시오.")