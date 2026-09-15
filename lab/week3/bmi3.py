#문제
#여러학생들의 키와몸무게를 리스트로 입력받아 BMI리스트로 출력하는
# 함수와 테스트하는 함수를 작성하시오
# BMI 함수는 저번시간에 작성한 get_BMI함수를 이용하여 작성하시오

def calculate_bmi(weight: float, height: float)-> int:
   bmi = weight / ((height / 100) ** 2)
   return bmi      

while True:
    weight = float(input("몸무게를 입력하시오"))
    height = float(input("키(cm)를 입력하시오"))
    print("BMI:", int(calculate_bmi(weight, height)))
    x=input("계속하시겠습니까? (y/n)")
    if x=="n":
        break  
 


       