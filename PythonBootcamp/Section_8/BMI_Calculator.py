# BMI Calculator

weight = float(input('Enter weight in kg: '))
height = flaot(input('Enter your height in m: '))
bmi = weight / heigth ** 2 # formula

# bmi = weight(lb) / height(in) **2 *703 (alt formula)
print('Your BMI is', format(bmi, '.2f')) # format the value to 2 # dec place
