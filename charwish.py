from random import uniform

pity = 0
guarantee = False

def roll(pity):
		chance = 0
		if pity <= 73:
				chance = 0.006
		else:
				chance = (0.006 + ((pity - 73) * 0.06))
		if (uniform(0, 1) <= chance):
				return 'FiveStar'
		return 'NotFiveStar'

def choosecharacter():
	global guarantee
	roll = uniform(0, 1)
	if (roll < 0.55) or (guarantee):
		guarantee = False
		return 'EventFiveStar'
	guarantee = True
	return 'StandardFiveStar'

def rolluntilevent():
	finalpity = 0
	cont = True
	global pity
	while cont:
		if roll(pity) == 'FiveStar':
			if choosecharacter() == 'EventFiveStar':
				cont = False
			finalpity += pity
			pity = 0
		else:
			pity += 1
	return finalpity

def rolluntilc6():
	constellation = 0
	totalpulls = 0
	while constellation < 7:
		totalpulls += rolluntilevent()
		constellation += 1
	return totalpulls

def rolluntilc6fortrials(totaltrials):
	currenttrials = 0
	totalpulls = 0
	while currenttrials < totaltrials:
		totalpulls += rolluntilc6()
		currenttrials += 1
	return totalpulls / currenttrials

if __name__ == "__main__":
	print(rolluntilc6fortrials(10000))
