#encoding=utf-8

## MAIN PROGRAM
FAR_TO_CEL='1'
BMI='2'
SUM_NATURAL='3'
SUM_EVEN='4'
PRIME='5'
SUM_DIGITS='6'
TRI_CHECK='7'
EXIT_CALL = 'exit'
EXCEPTION_CODE = 'EXCEPTION'

def main_func(): #select function
    """
    Program Intro
    """
    print "==================================================="
    print "python function group"
    print "1. 화씨 to 섭씨 변환"
    print "2. 비만 여부 판별"
    print "3. 자연수의 합 계산"
    print "4. 짝수의 합 계산"
    print "5. 소수 판별"
    print "6. 각 자리 숫자합"
    print "7. 삼각형 체크"
    print "you can exit program that input 'exit'"
    select_func = raw_input("select function(num): ")
    print "==================================================="
    """
    Select function for user needs
    """
    if select_func == FAR_TO_CEL:
        far_to_cel()
        return FAR_TO_CEL
    elif select_func == BMI:
        bmi()
        return BMI 
    elif select_func == SUM_NATURAL:
        sum_natural()	
        return SUM_NATURAL
    elif select_func == SUM_EVEN:
        sum_even()
        return SUM_EVEN
    elif select_func == PRIME:
        prime()
        return PRIME
    elif select_func == SUM_DIGITS:
        sum_digits()
        return SUM_DIGITS
    elif select_func == TRI_CHECK:
        tri_check()
        return TRI_CHECK
    elif select_func == EXIT_CALL:
        return EXIT_CALL
    else:
        print 'Your COde is FUCKING CODE Y KNOW? YOU ARE FOOLSITH BOY'
        return EXCEPTION_CODE

def far_to_cel():
    """화씨/섭씨 변환 프로그램"""
    temp_f = float(input("Input the current temperature in Fahrenheit: "))
    temp_c = float((temp_f - 32) * 5 / 9)

    print "The current temperature in Celsius is: %f"%temp_c 

def bmi():
    """비만 여부 판별 프로그램"""
    person = []
    p_status = ""
    name = raw_input("Person name is: ")
    height = float(input("Person height is: "))
    weight = float(input("Person weight is: "))

    bmi = weight / ((height * 0.01) ** 2)

    if bmi < 16:
        p_status = "Severely underweight"
    elif bmi < 18.5:
        p_status = "Underweight"
    elif bmi < 25:
        p_status = "Normal"
    elif bmi < 30:
        p_status = "Overweight"
    else:
         "Obese"

    print "%s's bmi = %s"%(name,p_status)

def sum_natural():
    """자연수의 합 계산 프로그램"""
    num = input("Input num: ") + 1
    total = 0 
    for sum in range(num):
       total += sum 
    print total
def sum_even():
    """짝수의 합 계산 프로그램"""
    num = input("Input num: ") + 1
    total = 0
    for sum in range(num):
        if sum % 2 == 0:
            total += sum
    
    print total
def prime() :
    """소수 판별 프로그램"""
    num = input("Input num: ")
    check = True
    if num == 2:
       check = True
    elif num < 2:
       check = False
    else:
       for i in range(2,num):
           if num % i == 0:
            check = False
    if check == True:
           print "%d if Prime"%num
    else:
         print "%d if not Prime"%num
     
def sum_digits():
    """각 자리 숫자합 프로그램"""
    print "im sum_digits()"
def tri_check ():
    """삼각형 체크 프로그램"""
    print "im tri_check()"


def game_wrapper():
	flag = True
	count_dic = {
		FAR_TO_CEL:0,
		BMI:0,
        SUM_NATURAL:0,
        SUM_EVEN:0,
        PRIME:0,
        SUM_DIGITS:0,
        TRI_CHECK:0,
		EXCEPTION_CODE:0
		}
	while True:
		flag = main_func()
		if flag == EXIT_CALL:
			break
		count_dic[flag] += 1
	
	print count_dic

game_wrapper()


