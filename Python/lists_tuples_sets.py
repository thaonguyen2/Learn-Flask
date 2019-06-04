# average bad way
grade_one = 77
grade_two = 80
grade_three = 90

print((grade_one + grade_two + grade_three) / 3)

# list
grades = [33, 55, 66, 77, 88]
grades.append(199)
print(sum(grades) / len(grades))

# tuple
numbers = (1, 2, 3, 4, 5) # immutable
numbers = numbers + (99,) # add 99 to tuple and return new tuple
print(numbers)

# set
set_grades = {22, 44, 55, 66} # unique & unordered => can't access via item index
print(set_grades)

## set operations
your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9}

print(your_lottery_numbers.intersection(winning_numbers)) # numbers in both sets
print(your_lottery_numbers.union(winning_numbers)) # add two sets ignore dupblicated
your_lottery_numbers.difference(winning_numbers)