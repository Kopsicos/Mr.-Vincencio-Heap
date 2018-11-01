def is_palindrome(str, firstDigit, lastDigit):
    if firstDigit == lastDigit:
        return True
    else:
        return False
    """checks if they are palindromes and then returns true or false"""


reverse_string("ski")
def reverse_string(str):
    return str[::-1]
    """reverses the word"""
    
def contains_length:
    


def double_vowels(word):
    for char in word:
    if char in "aeiou":
        return print(2*char)
    """prints the vowels twice"""

def count_uppercase(str):
    return sum(map(str.islower, string))
    """count the uppercase"""

def all_in_word(word1,word2):
    if word1 == word2:
        return True
    else:
        return False
    """if the words are the same return true"""


"""Map applies a function to all the items in an input_list. items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
    items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
While normal functions are defined using the def keyword, in Python anonymous functions are defined using the lambda keyword."""

def double(val):
    return val*2
    """doubles the number"""

def my_max(val1, val2):
    if val1 < val2:
        return val2
    else:
        return val1
    """finds the maximum"""

def min_of_max(a,b,c,d):
    return min(max(a,b), max(c,d))
    """ finds the minimum of maximum"""

def earlier_name(name1, name2):
    return

def ticket_price(age):
    if age > 65 or 13 < age < 25:
        return 7.50
    elif 25 < age < 64:
        return 11.25
    elif age < 12:
        return 4.75
    """Calculates the ticket price"""
    

def double_letters(str):
    return str.join([x*2 for x in strs])
    """doubles letters"""


A B   A and B  A or B    Not A    A XOR B
0 1    0         1         1         1
0 0    0         0         1         0
1 1    1         1         0         0
1 0    0         1         0         1


def num_letter(word, char)
    """
    the number of times char appear in word
    """
    num = 0
    for ch in word:
        if ch in char:
            num = num+1
    return num
        
def replace_letter(word, old, new)
    """
    copy word with the old letter replaced by new
    """
    var = ""
    for char in word:
        if old in word:
            old = old + new
    return new

def mystery6(word, s, char)
    """
    return word but the vowels are _
    """
    s = ""
    for char in word:
        if char in "aeiouAEIOU":
            s = s + "_"
        else:
            s = s + char
    return s

def every_other_new(list):
    """
    Return new list consisting of every other element of list starting from
    the first
    """
    return list[::2]

def every_other_modify(list):
    """
    Return list but without every other element
    """
    return list - list[::2]

def sum_of_even(list_of_numbers, num, sum) -> int:
    """
    Return sum of all even numbers in list
    """
    for num in list_of_numbers:
        if num % 2 == 0:
            sum = num
    return sum

def collect_strings(str, item, list) -> str:
    """
    Return new list containing all strs
    """
    for item in list:
        if item != str:
            item = ""
    return list

def count_int(int, num, list) -> int:
    """
    Return total number of ints
    """
    num = 0
    if item in list:
        num = num + 1
    return num

def remove_strings_modify(str, item, list) -> str:
    """
    Return list without strs
    """
    for item in list:
        if item == str:
            item = ""
    return list













