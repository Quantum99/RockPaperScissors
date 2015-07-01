from random import randint

x = randint(1,3)
user = -1
win = 0

while (win != 1):
	x = randint(1,3)
	print "1.Rock"
	print "2.Paper"
	print "3.Scissor"
	user = int(raw_input("Choice: "))
	if (x == 1):
		if (user == 1):
			print "Tie do again"
		elif (user == 2):
			print "You Lose"
		elif (user == 3):
			print "You Win"
			win = 1;
	elif (x == 2):
		if (user == 1):
			print "You Win"
			win = 1
		elif (user == 2):
			print "Tie do again"
		elif (user == 3):
			print "You Lose"
	elif (x == 3):
		if (user == 1):
			print "You Lose"
		elif (user == 2):
			print "Win"
			win = 1;
		elif (user == 3):
			print "Tie do again"
