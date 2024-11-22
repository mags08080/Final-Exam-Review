# -*- coding: utf-8 -*-
"""lab_final_review_questions

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1T9VFD7g6l4NDGsVl0sVlR03BMjK4oBsT
"""

## Q1. What will the following code return when you call the function?
def rectangle_area(length, width=5):
  return length * width

print(rectangle_area(10, width=7))
#guess: 10 * 7

## Q2. What will the following code return when you run it?
a = [1,2,3,4,5,6,7,8,9]
#will print last 2 numbers
b = a[-2:]

print(b)
#guess: [8,9]

## Q3. Write the line of code that will return the following:
## I'm reading "Hamlet" tonight
print("I'm reading \"Hamlet\" tonight.")

## Q4. Write a program to get an item's original price with input() and calculate
## its sale price, with a 30% discount and display price after discount.
original_price = float(input("Enter the item's original price: $"))

#calculate new price with 30% off
sale_price = original_price - (original_price * .30)

print(f"The price after discount is: ${sale_price:.2f}")

## Q5. What will the following code return when you run it?
a = 2
b = 3
c = 2
print(a**b**c)
#guess: 2^(3^2)

## Q7. Write the line of code to combine format specifier to simultaneously
## round the number to one and insert comma separators.
number = 1234567890.12345

print(f'{number:,.1f}')

## Q8. Write the lines of code to delete the entry for ‘Bob’ from the dictionary.
## And print the message of deletion and updated dictionary.
student_grades = {'Alice':90,'Bob':85,'Charlie':92}

#delete 'Bob'
del student_grades['Bob']

#deletion message and updated dictionary
print(f'The entry "Bob" has been deleted from the dictionary. Here is the updated dictionary:',student_grades)

## Q9. Write the lines of code to add the number to total until the user enters a zero. Display the total sum.
def main():
  total_sum = sum_numbers()
  print(f'The total sum is: {total_sum}')

#pass variable total_sum as argument
def sum_numbers(total_sum=0):
  number = int(input('Enter a number (0 to stop): '))
  #if the number is not 0
  if number != 0:
    #add number to total sum
    total_sum += number
    return sum_numbers(total_sum)
  else:
    return total_sum


if __name__ == '__main__':
  main()

## Q10. Write the lines of code to loop through numbers from 1 to 20 and
## skip if the number is a multiple of 3. Display numbers.
print('Numbers from 1 to 20, skipping multiplies of 3:')

#for loop to print numbers 1 to 20
for i in range (1,21):
  #if the number is divisible by 3 continue
  if i % 3 == 0:
    #asks as a skip
    continue
  else:
    print(i)