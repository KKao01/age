driving = input('請問你有沒開過車?')
if driving !='有' and driving != '沒有':
	print('只能輸入有或沒有')
age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('??????????')
elif driving == '沒有':
	if age >= 18:
		print("考")
	else:
		print("VVVV")

