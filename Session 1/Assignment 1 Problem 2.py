# 2. Write a program to compute and display 10 times 100 times 1000 times 10000. 

print("Enter a number:")
enterNumber = int(input())
timesTen = enterNumber * 10
timesHundred = enterNumber * 100
timesThousand = enterNumber * 1000
print(str(enterNumber) + " * 10 = " + str(timesTen) + ", " + str(enterNumber) + " * 100 = " + str(timesHundred) + ", " + str(enterNumber) + " * 1000 = " + str(timesThousand))
