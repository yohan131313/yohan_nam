def calculate_bmi(weight: float, height: float)-> float:
   bmi = weight / ((height / 100) ** 2)
   return bmi      

weight = float(input("몸무게를 입력하시오"))
height = float(input("키(cm)를 입력하시오"))


print("BMI:", calculate_bmi(weight, height))         