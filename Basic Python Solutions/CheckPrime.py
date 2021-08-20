def main():
	try:
		myNum=int(input("Enter a number : "))
		a=2
		checkPrime=0
		if(myNum%1 == 0 and myNum%1 == 0):
			while(a<myNum):
				if(myNum%a == 0):
					print(a)
					checkPrime = checkPrime + 1
				a =a + 1
				
		if(checkPrime == 0):
			print("This is a prime number")
		else:
			print("This is not a prime number")
	except ValueError:
		print("Invalid Input")
		
main()