'''
Question 4
Write a script that prints the multiples of 7 between 0
 and 100. Print one multiple per line and avoid printing
  any numbers that aren't multiples of 7. 
  Remember that 0 is also a multiple of 7.
'''
for number in range(101):
    if number%7==0:
        print(number)