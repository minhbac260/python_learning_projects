"""

# Bruce Force's keyboard is broken, only a few keys are still working. Bruce has figured out he can still type texts by
# switching the keyboard layout whenever he needs to type a letter which is currently not mapped to any of the m working keys
# of the keyboard.
# You are given a text that Bruce wishes to type, and he asks you if you can tell him the maximum number of consecutive characters
# in the text which can be typed without having to switch the keyboard layout.
# For simplicity, we assume that each key of the keyboard will be mapped to exactly one character,
# and it is not possible to type other characters by combination of different keys.
# This means that Bruce wants to know the length of the largest substring
# of the text which consists of at most m different characters.

# Input:

# The input contains several test cases, each test case consisting of two lines.
# The first line of each test case contains the number m (1 ≤ m ≤ 128),
# which specifies how many keys on the keyboard are still working.
# The second line of each test case contains the text which Bruce wants to type.
# You may assume that the length of this text does not exceed 1 million characters.
# Note that the input may contain space characters, which should be handled like any other character.

# The last test case is followed by a line containing one zero.

# Output:

# For each test case,
# print one line with the length of the largest substring of the text which consists of at most m different characters.


# Example:

# Input:

# 5
# This can't be solved by brute force.
# 1
# Mississippi
# 0

# Output:

# 7
# 2

"""



from numpy import equal
from pathlib import Path


file_inp = str(Path(__file__).parent) + "/input_broken_keyboard.INP"

def process(text_inp):
    f_pointer = open(text_inp,"r")
    char_arr = []
    key_number = 0
    text = f_pointer.readline()
    while text != '0':
        key_number = int(text)
        text = f_pointer.readline()
        
        
        
        print(key_number)
        print(text)
        
        
        
        text = f_pointer.readline()
    f_pointer.close()
        
process(file_inp)
        