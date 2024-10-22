from random import uniform

pity = 0
guarantee = False

def roll(pity):
		chance = 0
		if pity <= 62:
				chance = 0.007
		else:
				chance = (0.007 + ((pity - 62) * 0.07))
		if (uniform(0, 1) <= chance):
				return 'FiveStar'
		return 'NotFiveStar'

def chooseweapon():
	global guarantee
	roll = uniform(0, 1)
	if (roll < 0.375) or guarantee:
		guarantee = False
		return 'RightFiveStar'
	guarantee = True
	if (roll < 0.75):
		return 'WrongFiveStar'
	return 'StandardFiveStar'

def rolluntilevent():
	finalpity = 0
	cont = True
	global pity
	while cont:
		if roll(pity) == 'FiveStar':
			if chooseweapon() == 'RightFiveStar':
				cont = False
			finalpity += pity
			pity = 0
		else:
			pity += 1
	return finalpity

def rolluntilr5():
	refinement = 0
	totalpulls = 0
	while refinement < 5:
		totalpulls += rolluntilevent()
		refinement += 1
	return totalpulls

def rolluntilr5fortrials(totaltrials):
	currenttrials = 0
	totalpulls = 0
	while currenttrials < totaltrials:
		totalpulls += rolluntilr5()
		currenttrials += 1
	return totalpulls / currenttrials

if __name__ == "__main__":
	print(rolluntilr5fortrials(10000))
