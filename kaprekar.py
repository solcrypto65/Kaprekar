import random

def main():
	
	logfile = open("log9.txt", "a")
	frequency = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	logfile.write("Finding Kaprekar constant for 9 digit numbers \n\n")

	for num in range(100000000,999999999):
		steps = 0
		
		diff = num
		prevDiff = 0
		logText = ''
		while (diff != prevDiff):
			largest, smallest = getLargestAndSmallestNum(diff)
#			print(largest, smallest)
			prevDiff = diff
			diff = largest - smallest
#			print("Largest %d , Smallest %d , Diff %d , Prev Step Diff %d , In steps %d" % (largest,smallest,diff,prevDiff,steps))
			steps = steps + 1
			if (diff == prevDiff):
				logText = "Reached Kaprekar constant " + str(diff) + " in " + str(steps) + " steps for number " + str(num) + "\n"
				frequency[steps] = frequency[steps] + 1
				logfile.write(logText)
			if (steps > 24):
				logText = "Could not reach constant for " + str(num) + " in " + str(steps) + " steps \n"
				logfile.write(logText)
				break
	
	logText = ''
	for int in frequency:
		logText += str(int) + " , "

	logfile.write("\nFrequency Table\n")
	logfile.write(logText)
	logfile.close()

def getLargestAndSmallestNum(num: int) -> int :

	largest = "".join(sorted(str(num),reverse=True))
	smallest = "".join(sorted(str(num)))
	return int(largest), int(smallest)

if __name__== "__main__":
	main()
