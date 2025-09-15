"""
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
Complete the function that takes an array of words.

You must concatenate the nth letter from each word to construct a new word which should
be returned as a string, where n is the position of the word in the list.

for example:
["yoda", "best", "has"]  --> "yes"
   ^       ^        ^
   n=0     n=1      n=2

Note:Test cases contain valid input only - i.e. a string array or an empty array; and each
word will have enough letters.
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
"""
def concatenate(input_list):
    output_word = ""

    for n, word in enumerate(input_list):
        output_word += word[n]

    return output_word

if __name__ == "__main__":
    input_list = ["yoda", "best", "has"]
    print(concatenate(input_list))