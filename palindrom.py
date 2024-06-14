#PALIDROME
def is_palindrome(s):
    return s == s[::-1]

# Example usage
s = "racecar"
print(f"Is '{s}' a palindrome? {is_palindrome(s)}")

#FACTORIAL
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
n = 5
print(f"Factorial of {n} is {factorial(n)}")

#MERGE LIST
def merge_lists(list1, list2):
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list

# Example usage
list1 = [1, 3, 5]
list2 = [2, 4, 6]
print("Merged list:", merge_lists(list1, list2))



#RECURATION
def sum_of_natural_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)

# Example usage
n = 10
print(f"Sum of first {n} natural numbers is {sum_of_natural_numbers(n)}")


#SECOND LARGET NUM
def second_largest(numbers):
    first, second = float('-inf'), float('-inf')
    for number in numbers:
        if number > first:
            first, second = number, first
        elif first > number > second:
            second = number
    return second

# Example usage
numbers = [10, 5, 20, 8]
print("Second largest number is", second_largest(numbers))


# 7. Maximum Number

def maximum_number(numbers):
    max_num = float('-inf')
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num

# Example usage
numbers = [10, 5, 20, 8]
print("Maximum number is", maximum_number(numbers))




