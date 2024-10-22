import charwishold
import wepwishold

def rolluntilc6r5():
	totalpulls = 0
	totalpulls += charwishold.rolluntilc6()
	totalpulls += wepwishold.rolluntilr5()
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
