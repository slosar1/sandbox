import random


number = input("Enter a number")
number = int(number)

secret = random.randint(0,25)

if(number > secret):
	print("too high")
	number = input("enter a number")
	number = int(number)
	if(number > secret):
		print("too high")
	elif(number < secret):
		print("too low")
	else:
		print("you got it!")
elif(number < secret):
	print("too low")
	number = input("enter a number")
	number = int(number)
	if(number > secret):
	 	print("too high")
	elif(number < secret):
		print("too low")
	else:
		print("you got it")
else:
	print("you got it!")
print(secret)
