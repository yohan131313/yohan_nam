def congratulate(name):
    print("안녕하세요?")
    print(name + "님, 생일 축하합니다!")
    return None

def test_congratulate():
    name_list = ["요한", "민", "필구", "현준"]
    for name in name_list:
        congratulate(name)

if __name__ == "__main__":
    test_congratulate()

