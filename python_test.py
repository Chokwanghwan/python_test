#encoding=utf-8

## MAIN PROGRAM
FAR_TO_CEL='FAR TO CEL'
CEL_TO_FAR='CEL TO FAR'
EXIT_CALL = 'EXIT'
EXCEPTION_CODE = 'EXCEPTION'

def main_func(): #select function
	"""
	Program Intro
	"""
	print "==================================================="
	print "python function group"
	print "1. 화씨 - 섭씨 변환"
	print "2. 섭씨 - 화씨 변환"
	print "you exit to press ''exit''"
	select_func = raw_input("select function(num): ")
	
	print "==================================================="
	"""
	Select function for user needs
	"""
	if select_func == FAR_TO_CEL:
		far_to_cel()
		return FAR_TO_CEL
	elif select_func == CEL_TO_FAR:
		cel_to_far()
		return CEL_TO_FAR
	elif select_func == EXIT_CALL:
		return EXIT_CALL
	else:
		print 'Your COde is FUCKING CODE Y KNOW? YOU ARE FOOLSITH BOY'
		return EXCEPTION_CODE

def far_to_cel(): #화씨/섭씨 변환 프로그램
		temp_f = float(input("Input the current temperature in Fahrenheit: "))
		temp_c = float((temp_f - 32) * 5 / 9)
	
		print "The current temperature in Celsius is: %f"%temp_c 

def cel_to_far():
	"""섭씨/화씨 변환 프로그램"""
	print 'cel_to_far'

def game_wrapper():
	flag = True
	count_dic = {
		FAR_TO_CEL:0,
		CEL_TO_FAR:0,
		EXCEPTION_CODE:0
		}
	while True:
		flag = main_func()
		if flag == EXIT_CALL:
			break
		count_dic[flag] += 1
	
	print count_dic

game_wrapper()


