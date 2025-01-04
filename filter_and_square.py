# You are given a list of integers. Write a Python function called filter_and_square() that:

# Filters out all the numbers that are even.
# Squares the odd numbers in the list.
# Returns a sorted list of the squared values in ascending order.


def filter_and_square():

  list = [17,23,12,7,13,32,5]

  for i in list:        # removing even numbers
    if i % 2 == 0:     
      list.remove(i)
  
  square_list = []         # Square of all odd numbers 
  for i in list:
    square_list.append(i**2)

  square_list.sort()
   
  return list,square_list


list,square_list = filter_and_square()
print('Odd Numbers list: ',list)
print('Square and Sorted list: ',square_list)    # Square wali list ko sort kiya
