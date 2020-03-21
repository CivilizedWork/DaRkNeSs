##practice12.1
# t = (1,'a'),(2,'c'),(3,'b')
# t = sorted(t)
def make_histogram(s):
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist


def most_frequent(string):
    n = len(string)
    hist = make_histogram(string)
    t = hist.items()
    t1 = []
    for string1, number in t:
        t1.append((number, string1))
    t1 = sorted(t1)
    for number1, string2 in reversed(t1):
        print(number1, string2)


# def most_frequent(s):
#     hist = make_histogram(s)
#     t = []
#     for x, freq in hist.items():
#         t.append((freq, x)
#     # t.sort(reverse=True)
#     res = []
#     for freq, x in t:
#         res.append(x)
#     return res
#
#  def make_histogram(s):
#     hist = {}
#     for x in s:
#         hist[x] = hist.get(x, 0) + 1
#      return hist
#
# def read_file(filename):
#     return open(filename).read()
#
# if __name__ == '__main__':
#     string = read_file('emma.txt')
#     letter_seq = most_frequent(string)
#     for x in letter_seq:
#         print(x)

##practice12.2
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def structure():
    hist = {}
    inverse = {}
    fin = open('words.txt')
    for word in fin:
        n = len(word)
        if n >= 6:
            hist[word] = int(hist.get(word, 0)) + int(n)
    inverse = invert_dict(hist)
    print(inverse)
    for number in inverse:
        n = len(inverse[number])
        n1 = 0
        # while n1 < n:
        #     if list(inverse[number[n1]]) not in list(inverse[number[:]]):
        #         n1 += 1
        #     else:
        #         print(inverse[number[n1]])
# def signature(s):
#     t = list(s)
#     t.sort()
#     t = ''.join(t)
#     return t
#
#
# def all_anagrams(filename):
#     d = {}
#     for line in open(filename):
#         word = line.strip().lower()
#         t = signature(word)
#         if t not in d:
#             d[t] = [word]
#         else:
#             d[t].append(word)
#     return d
#
#
# def print_anagram_sets(d):
#     for v in d.values():
#         if len(v) > 1:
#             print(len(v), v)
#
#
# def print_anagram_sets_in_order(d):
#     # make a list of (length, word pairs)
#     t = []
#     for v in d.values():
#         if len(v) > 1:
#             t.append((len(v), v))
#
#     # sort in ascending order of length
#     t.sort()
#
#     # print the sorted list
#     for x in t:
#         print(x)
#
#
# def filter_length(d, n):
#     res = {}
#     for word, anagrams in d.items():
#         if len(word) == n:
#             res[word] = anagrams
#     return res
#
#
# if __name__ == '__main__':
#     anagram_map = all_anagrams('words.txt')
#     print_anagram_sets_in_order(anagram_map)
#
#     eight_letters = filter_length(anagram_map, 8)
#     print_anagram_sets_in_order(eight_letters)

##practice12.3
# def metathesis_pairs(d):
#     for anagrams in d.values():
#         for word1 in anagrams:
#             for word2 in anagrams:
#                 if word1 < word2 and word_distance(word1, word2) == 2:
#                     print(word1, word2)
#
#
# def word_distance(word1, word2):
#     assert len(word1) == len(word2)
#
#     count = 0
#     for c1, c2 in zip(word1, word2):
#         if c1 != c2:
#             count += 1
#
#     return count
#
#
# if __name__ == '__main__':
#     sets = anagram_sets.all_anagrams('words.txt')
#     metathesis_pairs(sets)
