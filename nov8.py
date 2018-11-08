
for j in range(5)
j = 0
j = 1
j = 2
j = 3
j = 4

s= "abcde"
for j in range(s)
    ch = s[j]

For problems with two lists:
n1=len(list1)
n2=len(list2)
n = min(n1, n2)
for it in range(n):
    list1[it]
    list2[it]
    

def largest(list_of_numbers) -> list:
    """
    Return the largest number in list_of_numbers
    """
    highest = max(list_of_numbers)
    return highest

def remove_duplicates(old_list, new_list) -> list:
    """
    Return a copy of old_list which has no duplicate elements
    """
    import collections
    return [item for item, count in collections.Counter(a).items() if count > 1]

def common_element(list1, list2) -> list:
    """
    Return true if and only if list1 and list2 have at least one
    element in common
    """
    for item in list1:
        if item in list2:
            return True
    return False

def list_to_string(list_of_numbers) -> list:
    """
    Return a string consisting of each element of list_of_numbers in order
    """
    newstr = ""
    """
    I need help with this one
    """

def extend_a_list(list2, list1) -> list:
    """
    Add all of the elements of list2 to the end of list1
    """
    return list1 + list2

def all_squares(max_number) -> list:
    """
    Return a list of all the squares of the numbers from 0 to max_number
    """
    new_list = []
    for j in range(max_number):
        if j*j <= max_number:
            new_list.append(j*j)
    return new_list

def items_in_common(list1, list2) -> list:
    """
    Return a list consisting of all of the elements in common
    """
    newlist = []
    for i in list1:
        if i in list2:
            newlist = newlist + i
    return newlist

def mystery12(list_of_numbers, upper_limit) -> list:
    """
    Return True if and only if upper_limit is greater than or equal to the
    numbers in the list
    """
    b = True
    for e in list_of_numbers:
        if e > upper_limit:
            b = False
    return b

