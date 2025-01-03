# Write a function fizz_buzz(n) that returns a list of strings representing the numbers from 1 to n.

# For multiples of 3, store "Fizz" instead of the number.
# For multiples of 5, store "Buzz".
# For numbers that are multiples of both 3 and 5, store "FizzBuzz".

# Example:
# Input: n = 15
# Output:
# ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]


def fizz_buzz(n):
  result = []
  for i in range(1,n+1):
    if i%3 == 0 and i%5 == 0:
      result.append('FizzBuzz')
    elif i % 3 == 0:
      result.append('Fizz')
    elif i % 5 == 0:
      result.append('Buzz')
    else:
      result.append(i)
    
  return result

n = int(input('Enter any number: '))
print(fizz_buzz(n))