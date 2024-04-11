#Creation of variables
"""patient_name = "John Smith"
age = 20
is_new = True
print("Hello World")"""

"""
#Type conversion.Can be converted to str(), bool(), int(),float().
#Input records values as string therefore should be converted when mixing with int or float
name = input("What is your name? ")
print("Hello " + name)
first = input("First: ")
second = input("Second: ")
comb = float(first) + float(second)
print(comb)
"""

"""
#Working with string functions
course = "I am very intelligent"
print(course.upper())
print(course.lower())
print(course.find('y'))
print(course.replace('am','is'))
print('very' in course)
"""
"""
#if statement

weight = input('Weight: ')
kg_lbs = input('Please write K for kg or L for lbs: ')

if kg_lbs.lower() == 'k':
    print("Weight in Kg: " + weight)
elif kg_lbs.lower() == 'l':
    print("Weight in Lbs: " + weight)
else:
    print("Unknown")

#while loop
i = 1

while i <= 10:
    print(i * '*')
    i += 1

#lists
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.insert(1, 1.5)
numbers.remove(1.5)
numbers.pop() # removes last value
numbers.reverse() # reverses order of list
numbers.sort() # sorts in order
print(numbers)
print(len(numbers))

#tuples cannot be changed, appended

number_1 = int(input(f"Enter first number:"))
number_2 = int(input(f"Enter second number:"))


def product(number_1, number_2):

    prod = number_1 * number_2

    if prod <= 1000:
        print(f"The result is: {prod}")
    else:
        add = number_1 + number_2
        print(f"The result is: {add}")


product(number_1, number_2)


#prints current number, previous number nd the sum in a range
def numbers(rang):
    range_fun = range(rang)

    lis_rng = list(range_fun)
    prev = 0
    for num in range_fun:

        total = num + prev
        print(f"Current number: {num} Previous number: {prev} Sum: {total}")
        prev = num


numbers(10)


user_str = input("Enter your string: ")


def even_letters():
    str_len = len(user_str)
    for i in range(0, str_len, 2):
        print(user_str[i])
    print(user_str[2:])


even_letters()


def pattern():
    for num in range(10):
        for i in range(num):
            print(num, end=" ")
        print("\n")
pattern()



def isPalindrome():
    num = int(input("Enter the number: "))
    original_number = num
    rev_num = 0

    while num > 0:
        remainder = num % 10
        rev_num = (rev_num * 10) + remainder
        num = num // 10


    if original_number == rev_num:
        print("Yes is palindrome")
    else:
        print("No is not palindrome")


isPalindrome()
"""

students = [{'name': 'Gloria', 'project': 'Garbatula'},
            {'name': 'Daudi', 'project': 'Home Science'}]
c_no =1001
for i in students:
    print("Student's name: ", i["name"])
    print("Student's Project: ", i["project"])
    print("Unique Certificate Number:", c_no)
    print()
    c_no += 1

print("All certificates generated successfully")