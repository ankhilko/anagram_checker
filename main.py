def an_checker() -> bool:
    """check if two strings are anagrams"""
    # welcome message
    print("Welcome to the anagram checker!")
    # create a data set to store the strings
    lists = []
    # get user input
    for i in range(2):
        # read line
        word = input(f'Please enter the line #{i + 1}: ')
        # convert to lowercase
        word = word.lower()
        # leave only letter in the line
        word = [i for i in word if i.islower()]
        # sort
        word = sorted(word)  # or word.sort()
        # add to 'lists'
        lists.append(word)
    return lists[0] == lists[1]


def an_check_v2() -> bool:
    """check if two strings are anagrams"""
    # welcome message
    print("Welcome to the anagram checker!")
    # create a data set to store the strings
    temp = []
    # ask for, read,and  convert the input
    for i in range(2):
        temp.append([j for j in sorted(list(input(f'Please enter the line #{i + 1}: ').lower())) if j.islower()])
    # compare and return the comparison result
    print("The strings are anagrams: ", end="")
    # compare and return the comparison result
    return temp[0] == temp[1]


def an_check_in_one_line() -> bool:
    """check if two strings are anagrams in one line"""
    return [i for i in sorted(list(input(f'line #1: ').lower())) if i.islower()] == \
           [i for i in sorted(list(input(f'line #2: ').lower())) if i.islower()]


print(an_checker())

print(an_check_v2())

print(an_check_in_one_line())
