#1 - Print all integers from 0 to 150.
for x in range(0,151):
    print(x)
#2 - Print all the multiples of 5 from 5 to 1,000
for x in range(5, 1000, 5):
    print(x)
#3 - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(1, 100):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)
#4 - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for x in range(0, 500001):
    if x % 2 != 0:
        sum += x
print(sum)
#5 - Print positive numbers starting at 2018, counting down by fours.
for x in range(2018, 0, -4):
    print(x)
#6 - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
for x in range(2, 18, 3):
    print(x)






