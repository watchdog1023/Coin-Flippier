import random

head = 0
tails = 0

def flip():
	head = 0
	tails = 0
	for x in range(10):
		hort = random.randint(0,1)
		if hort == 0:
			head = head + 1
		if hort == 1:
			tails = tails + 1
	
	print("Heads was " + str(head))
	print("Tails was " + str(tails))
	if tails == head:
		print("Draw,fliping again")
		flip()
	elif tails > head:
		print("Tails Wins")
	elif tails < head:
		print("Heads Wins")

flip()