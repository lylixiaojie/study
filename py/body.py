#这个程序是用来判断BMI体重指数
w=input("please input your weight:")
weight=float(w)
h=input("please input your high:")
high=float(h)
bmi=weight/(high*high) 
if bmi >=32:
	print("your BMI is:",bmi,"your body is 严重肥胖")
elif bmi >=28:
	print("your BMI is:",bmi,"your body is 肥胖")
elif bmi >=25:
	print("your BMI is:",bmi,"your body is 过重")
elif bmi >=18.5:
	print("your BMI is:",bmi,"your body is 正常")
else:
	print("your BMI is:",bmi,"your body is 过轻")
