###案例二
# fin = open('words.txt')
# line = fin.readline()
# word = line.strip()
# for line in fin:
#     word = line.strip()
#     print(word)

##practice9.1
def printf_20():
    fin = open('words.txt')
    for line in fin:
        if len(line) > 20:
            word = line.strip()
            print(word)


##practice9.2
def has_no_e():
    fin = open('words.txt')
    n = 1
    n1 = 0
    n2 = 0
    for line in fin:
        n1 += 1
        for word in line:
            if word != 'e':
                n = 1
            else:
                n = 0
                break
        if n == 1:
            n2 += 1
            print(line)
    print(n1, n2, n2 / n1)


##practice9.3
def avoids(ban):
    fin = open('words.txt')
    n = 1
    n1 = 0
    for line in fin:
        for word1 in ban:
            for word in line:
                if word == word1:
                    n = 0
                    break
                else:
                    n = 1
            if n == 0:
                break
        if n == 1:
            n1 += 1
            print(line)
    print(n1)


def five(five):
    n = len(five)
    s = 'abcdefghijklmnopqrstuvwxyz'
    # for s1 in s:


#     for 1 in n:

## practice 9.4
def uses_only(word, string):
    for letter in word:
        if letter not in string:
            print(letter)
            return False
    return True


##practice 9.5
def uses_all(word, string):
    for letter in string:
        if letter not in word:
            return False
    return True


# def uses_all(word, required):
#     return uses_only(required, word)

##practice 9.6
def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True


# def is_abecedarian(word):
# #     if len(word) <= 1:
# #         return True
# #     if word[0] > word[1]:
# #         return False
# #     return is_abecedarian(word[1:])

# def is_abecedarian(word):
#     i = 0
#     while i < len(word)-1:
#         if word[i+1] < word[i]:
#             return False
#         i = i+1
#     return True

##practice 9.7
##参考答案
def is_triple_double(word):
    """Tests if a word contains three consecutive double letters.

    word: string

    returns: bool
    """
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            i = i + 1 - 2 * count
            count = 0
    return False


def find_triple_double():
    """Reads a word list and prints words with triple double letters."""
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


print('Here are all the words in the list that have')
print('three consecutive double letters.')
find_triple_double()
print('')


##practice9.8
##参考答案
def has_palindrome(i, start, length):
    """Checks if the string representation of i has a palindrome.

    i: integer
    start: where in the string to start
    length: length of the palindrome to check for
    """
    s = str(i)[start:start + length]
    return s[::-1] == s


def check(i):
    """Checks if the integer (i) has the desired properties.

    i: int
    """
    return (has_palindrome(i, 2, 4) and
            has_palindrome(i + 1, 1, 5) and
            has_palindrome(i + 2, 1, 4) and
            has_palindrome(i + 3, 0, 6))


def check_all():
    """Enumerate the six-digit numbers and print any winners.
    """
    i = 100000
    while i <= 999996:
        if check(i):
            print(i)
        i = i + 1


print('The following are the possible odometer readings:')
check_all()
print()


##practice9.9
def str_fill(i, n):
    """Returns i as a string with at least n digits.

    i: int
    n: int length

    returns: string
    """
    return str(i).zfill(n)


def are_reversed(i, j):
    """Checks if i and j are the reverse of each other.

    i: int
    j: int

    returns:bool
    """
    return str_fill(i, 2) == str_fill(j, 2)[::-1]


def num_instances(diff, flag=False):
    """Counts the number of palindromic ages.

    Returns the number of times the mother and daughter have
    palindromic ages in their lives, given the difference in age.

    diff: int difference in ages
    flag: bool, if True, prints the details
    """
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff

        # assuming that mother and daughter don't have the same birthday,
        # they have two chances per year to have palindromic ages.
        if are_reversed(daughter, mother) or are_reversed(daughter, mother + 1):
            count = count + 1
            if flag:
                print(daughter, mother)
        if mother > 120:
            break
        daughter = daughter + 1
    return count


def check_diffs():
    """Finds age differences that satisfy the problem.

    Enumerates the possible differences in age between mother
    and daughter, and for each difference, counts the number of times
    over their lives they will have ages that are the reverse of
    each other.
    """
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print(diff, n)
        diff = diff + 1


print('diff  #instances')
check_diffs()

print()
print('daughter  mother')
num_instances(18, True)
