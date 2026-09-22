def calculate_bmi(weight: float, height: float)-> float:
   bmi = weight / ((height / 100) ** 2)
   return bmi     
'''저체중 : 18.5 미만
정상 : 18.5~22.9
비만 전단계(과체중) : 23~24.9
1단계 비만 : 25~29.9
2단계 비만 : 30~34.9
3단계 비만(고도비만) : 35 이상'''

def bmi_status(bmi: float) -> str:  
    if bmi < 18.5:
        return "저체중"
    elif bmi < 23:
        return "정상"
    elif bmi < 25:
        return "과체중"
    elif bmi < 30 :
        return "1단계 비만"
    elif bmi < 35:
        return "2단계 비만"
    else:
        return "고도비만"
    
weight = float(input("몸무게를 입력하시오"))
height = float(input("키(cm)를 입력하시오"))
bmi = calculate_bmi(weight,height)
print(f"BMI: {bmi:.2f}")
print(f"건강 상태: {bmi_status(bmi)}") 