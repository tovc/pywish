import charwish
import wepwish

def rolluntilc6r5():
	totalpulls = 0
	totalpulls += charwish.rolluntilc6()
	totalpulls += wepwish.rolluntilr5()
	return totalpulls

def rolluntilc6r5fortrials(totaltrials):
	currenttrials = 0
	totalpulls = 0
	while currenttrials < totaltrials:
		totalpulls += rolluntilc6r5()
		currenttrials += 1
	return totalpulls / currenttrials
if __name__ == "__main__":
	print(rolluntilc6r5fortrials(10000))
