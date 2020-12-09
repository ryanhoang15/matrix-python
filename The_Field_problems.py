# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.





## 1: (Problem 1.7.1) Python Comprehensions: Filtering
def myFilter(myList, num):
    updateList = []
    for i in range(len(myList)):
        if myList[i] % num != 0:
            updateList.append(myList[i])

    return updateList



## 2: (Problem 1.7.2) Python Comprehensions: Lists of Lists

def my_lists(myList):
    updateList = []
    for i in range(len(myList)):
        nestedList = []
        for j in range(myList[i]):
            nestedList.append(j+1)

        updateList.append(nestedList)

    return updateList



## 3: (Problem 1.7.3) Python Comprehensions: Function Composition
def myFunctionComposition(dict_1, dict_2):
    updateDict = {}
    for key_1 in dict_1:
        keyValue = dict_1[key_1]
        for key_2 in dict_2:
            if keyValue == key_2:
                updateDict[key_1] = dict_2[keyValue]

    return updateDict



## 4: (Problem 1.7.4) Summing numbers in a list
def mySum(list_1):
    result = 0
    for i in range(len(list_1)):
        result = result + list_1[i]

    return result



## 5: (Problem 1.7.5) Multiplying numbers in a list
def myProduct(myList):
    result = 1
    for i in range(len(myList)):
        result = result * myList[i]
    return result



## 6: (Problem 1.7.6) Minimum of a list
def myMin(myList):
    minimum = myList[0]
    for i in range(1, len(myList)):
        if minimum > myList[i]:
            minimum = myList[i]

    return minimum


## 7: (Problem 1.7.7) Concatenation of a List
def myConcat(L):
    '''
    Input:
      -L:a list of strings
    Output:
      -the concatenation of all the strings in L
Be sure your procedure works for the empty list.
    Examples:
    >>> myConcat(['hello','world'])
    'helloworld'
    >>> myConcat(['what','is','up'])
    'whatisup'
    '''
    pass



## 8: (Problem 1.7.8) Union of Sets in a List
def myUnion(L):
    '''
    Input:
      -L:a list of sets
    Output:
      -the union of all sets in L
Be sure your procedure works for the empty list.
    Examples:
    >>> myUnion([{1,2},{2,3}])
    {1, 2, 3}
    >>> myUnion([set(),{3,5},{3,5}])
    {3, 5}
    '''
    pass



## 9: (Problem 1.7.10) Complex Addition Practice
# Each answer should be a Python expression whose value is a complex number.

complex_addition_a = ...
complex_addition_b = ...
complex_addition_c = ...
complex_addition_d = ...



## 10: (Problem 1.7.12) Combining Complex Operations
#Write a procedure that evaluates ax+b for all elements in L

def transform(a, b, L):
    '''
    Input:
      -a: a number
      -b: a number
      -L: a list of numbers
    Output:
      -a list of elements where each element is ax+b where x is an element in L
    Examples:
    >>> transform(3,2,[1,2,3])
    [5, 8, 11]
    '''
    pass



## 11: (Problem 1.7.13) GF(2) Arithmetic
GF2_sum_1 = ... # answer with 0 or 1
GF2_sum_2 = ...
GF2_sum_3 = ...
