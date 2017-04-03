import math
import string

def vol(rad):
    return (4/3.0) * math.pi * (rad**3)

def ran_check(num, low, high):
    return num in range(low, high)

def up_low(s):
    low = 0
    high = 0
    for letter in s:
        if letter.islower():
            low += 1
        elif letter.isupper():
            high += 1
    print "No. of Upper case characters: " + str(high)
    print "No. of Lower case characters: " + str(low)

def unique_list(l):
    unique = []
    for number in l:
        if number in unique:
            pass
        else:
            unique.append(number)
    return unique

def multiply(numbers):
    sum = 1
    for number in numbers:
        sum *= number
    return sum

def palindrome(s):
    for i in range(0, len(s)):
        if s[i] != s[(len(s) - 1) - i]:
            return False
    return True

def ispangram(str1, alphabet=string.ascii_lowercase):
    newString = str1.lower()
    for letter in alphabet:
        if not letter in newString:
            return False
    return True

print ran_check(2, 1, 3)
print ran_check(2, 3, 5)
print up_low("How Many")
print unique_list([1, 1, 2, 2, 2, 3, 4])
print multiply([1, 2, 3, -4])
print palindrome("helleh")
print palindrome("hello")
print ispangram("The quick brown fox jumps over the lazy dog")
print ispangram("hello")
