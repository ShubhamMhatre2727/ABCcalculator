def BMI(height, weight):
    
    bmi = weight/(height**2)
    # Conditions to find out BMI category
    if (bmi < 18.5):
        msg = "Underweight"
    
    elif ( bmi >= 18.5 and bmi < 24.9):
        msg = "Healthy"
    
    elif ( bmi >= 24.9 and bmi < 30):
        msg = "Overweight"
    
    elif ( bmi >=30):
        msg = "Suffering from Obesity"      
    
    bmiDict = {
        'value': bmi,
        'msg': msg
    }
    return bmiDict
 
# # Driver code
# height = 1.79832
# weight = 70
 
# # calling the BMI function
# bmi = BMI(height, weight)
# print(bmi)
