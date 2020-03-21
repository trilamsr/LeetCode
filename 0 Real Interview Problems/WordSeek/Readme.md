# 9999 Word SeekPlease

Given a grid of letters, find the words in the grid. The letters can be in straight sequence in any of the 8 directions from the first character of the word. All words might not be in the grid. Print the word and the start row and column position for each word that is found. For words that are not found, print -1 for both the row and column position. All indices start from 0

Sample Input - Here is a 4x4 grid of letters as sample input. The grid is followed the by the words to find after a blank line. All characters will be in upper case.

**Example:**

    Grid:
        ['ABCD',
        'PRAT',
        'KITA',
        'ANDY']
    Words:
        [ANDY, CAT, DOG]

    Sample Output:
        ANDY 3 0
        CAT 0 2
        DOG -1 -1
    
**Example 2**:
    Grid:
        ['TRAP',
        'CARD',
        'FACT',
        'DART']
    Words: ['CAT', 'DOG', 'FACT']
    
    Output:
        CAT 2 2
        DOG -1 -1
        FACT 2 0

>>The input words are sorted alphabetically. The output words should also be sorted.The accepted solution should have the lowest complexity ie. You should iterate over the grid of characters only once (not once per word). ie. If there are "n" words given, don't parse through the grid "n" times.