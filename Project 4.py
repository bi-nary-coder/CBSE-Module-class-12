# Python program for finding frequency of each element in the given list
# importing counter function from collections
from collections import Counter
# given list which may contains the duplicates
given_list1 = ["Hello", "this", "is", "this", "is", "BTechGeeks", "Hello",
               "is", "is", "this", "BTechGeeks", "is", "this", "Hello", "python"]
# finding frequency of each elements using Counter() function
freqcyCounter = Counter(given_list1)
# printing the frequency of each element
for key in freqcyCounter:
    # frequency of the respective key
    count = freqcyCounter[key]
    # print the element and its frequency
    print("The element", key, "Has frequency =", count)