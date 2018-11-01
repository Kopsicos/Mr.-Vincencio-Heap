def currentNum(x):
    if x % 2 != 0:
        return x * 3 + 1
    else:
        return x // 2

max_of_min(1,2,3,4)
def max_of_min(a,b,c,d):
    """ Take four values, fin the minimum of the first two and the last two
     then find the max of the the minimums
     max_of_min(1,2,3,4)
     """
    return max(min(a,b), min(c, d))
    
    
number_of_cents(1.50)
def number_of_cents(num):
    return int(num*100)
    """removes the decimal point
    remember to always write the proper monetary notation(two decimal places) """

calculate_tax(20, 0.15)
def calculate_tax(amount, tax):
    return amount * (1 + tax)
    """return the final bill on amount tax added"""

reverse_string("ski")
def reverse_string(str):
    return str[::-1]
    """reverses the word"""

val = "ski"
every_other_letter("ski")
def every_other_letter(str):
    return str[1: :2]
    """prints every other letter"""
    
repeat_word("ski")
def repeat_word(str, x):
    return print(x*(str + _ ))
    """prints the word over and over again"""

Marks
1. Homework
    completion
2. Quizzes
    correctness
    just like homework
3. Tests + Exam
    look like quizzes
    pretty easy
    written by hand
4. Project
    worth a lot

Strings
val = "Steely Dan"
len(val)
                 
def polynomial(a,b,c):
    """ returns a polynomial
    polynomial(1,2,3)
    x^2 + 2x + 3
    """
    return a*x**2 + bx + c

def circle_area(r):
    """returns the area of a circle
    circle_area(3)
    28.274333882308138
    """
    return 3.14159265358979323846264338*r*r

def count_uppercase(word) -> str:
    """Counts the uppercase letters in a word
    count_uppercase("Bhumibol Adulyadej")
    2
    """
    return sum(map(str.islower, string))

def no_vowels(word) -> str:
    """
    gets rid of all of the vowels
    no_vowels("Bhumibol Adulyadej")
    Bhmbl dlydj
    """
    newstr = ""
    vowels = "a", "e", "i", "o", "u"
    for x in word.lower():
        if x in vowels:
            newstr = word.replace(x, "")        
    return newstr

def mystery4(int : number1) - > int:
    """
    returns six times the number
    mystery4(4)
    24
    mystery4(7)
    42
    """
    var1 = number1*2
    var2 = var1 * 3
    var1 = number1
    return var2

felipe.vicencio.heap@mail.utoronto.ca

Lists:
 x =   [1, 2,3,4,5,6]
 y = "Nom Nom"
 y[0]
 x[0]
 z = ["a", "b", "c", "d", "e"]
 z[::2]
 for e in [1,2,3,4,5,6]:
     x= x+e
     return
 
var = ["1", "2", "3", "4", "5"]
5 in var
False
var2 = ["ab", "cd"]
"a" in "ab"
True
s="abcd"


def merge_lists(list1, list2):
    """
    Return two lists but merged
    """
    return list1 + list2
    
def first_and_last(list, item):
    """
    Return True if and only if the first and last irems in a list are equal
    """
    return list[0] == list[-1]   
    
def in_list(list, item):
    """
    Returns True if and only if item is in list
    """
    return item in list

def count_item(list, item, num):
    """
    Return the number of times that item appears in the list
    """
    num = list.count(item)
    return num
    
def reverse_list(list):
    """
    Return list with with items in reverse
    """
    return list[::-1]


def letter_in_words(list1, list2, list3, char) -> bool:
    """
    Return true if letter is in every entry in a
    """
    if ch in list1:
        if ch in list2:
            if ch in list3:
                return True
            else:
                Return False
        
def remove_strings(list):
    """
    Return a copy of list without strings
    """
    for item in list:
        if type(item) == str:
            list.remove(item)
    return list
                 
def enigma1(n, p, list_of_numbers) - > :
    """
    Returns the product of all of the numbers in the list
    """
    p = 1
    for n in list_of_numbers:
        p = p * n
    return p
    
remove and append
