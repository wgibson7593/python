divisible_by_30 = 0
divisible_by_5 = 0
divisible_by_3 = 0
divisible_by_2 = 0
divisible_by_3_and_2 = 0
not_meet_criteria = 0


# Get user input 
while True:
    try:
        smaller = int(input("Enter the lower number: "))
        if smaller > 0: 
            break
    except: 
        print("Please enter valid number")
        
while True:
    try:
        larger = int(input("Enter the larger number: "))
        if larger > smaller:
            break
    except:
        print("Enter number larger than smaller number: ")

totalNumber = larger - smaller

for number in range(smaller, larger +1):
    
    if number % 30 == 0:
        print("Foo")
        divisible_by_30 += 1
    elif number % 5 == 0:
        print("Bar")
        divisible_by_5 += 1
    elif number % 3 == 0 and number % 2 == 0:
        print("FizzBuzz")
        divisible_by_3_and_2 += 1
    elif number % 3 == 0:
        print("Fizz")
        divisible_by_3 += 1
    elif number % 2 == 0:
        print("Buzz")
        divisible_by_2 += 1
    else:
        print("Bazz")
        not_meet_criteria += 1


print("The total numbers evaluated was {}.".format(totalNumber))
print("There were {} numbers that are divisible by 30.".format(divisible_by_30))
print("There were {} numbers that are divisible by 5.".format(divisible_by_5))
print("There were {} numbers that are divisible by 3.".format(divisible_by_3))
print("There were {} numbers that are divisible by 2.".format(divisible_by_2))
print("There were {} numbers that are divisible by both 3 and 2.".format(divisible_by_3_and_2))
print("There were {} numbers that didn’t meet any of the requirements above.".format(not_meet_criteria))
