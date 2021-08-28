#number guessing game using random module. 

from  random import randint

n=randint(1,100)
count=1

print("------WELCOME TO NUMBER GUESSING GAME.------\n".center(50))
print("SYSTEM WILL GENERATE RANDOM NUMBER FROM 0-100.\n\nYOU NEED TO FIND THAT NUMBER.\n\nENTER YOUR GUESS: ")

while True:
		
		try:
			a=int(input("".center(20)))
			
		except ValueError:
			print("Invalid Input. Enter Numbers Only".center(50))
			
			continue
			
		if a==n:
			print(f"\nCongratulations You Won  ;)\n\nYou Took {count} Chances")
			break
	
		print("\nEnter Small Number: " if (a>n) else "\nEnter Big Number: ")
		count+=1
