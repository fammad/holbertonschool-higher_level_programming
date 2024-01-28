#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
p_number = number
if number < 0:
	p_number = number * -1
	last = p_number % 10
	if last != 0:
		last = last * -1
else:
	last = p_number % 10
	print(f"Last digit of {number} is {last}", end="")
if last > 5:
	print(" and is greater than 5")
elif last == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
