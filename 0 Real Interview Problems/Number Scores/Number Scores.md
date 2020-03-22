# 7. Number Scores

You have developed a scoring system for positive integers that works as follows:

+1 points for every 7 found in the number. 
    
    For example, 7571 would score 2 points.
    
+3 points for each pair of consecutive 5s. If there are more than two 5s in a row, add +3 for each additional 5, since it makes an additional pair 
    
    For example, four consecutive 5s gives +15).

+N2 points for a sequence of length N (N >= 1) where each digit is 1 less than the previous digit. 

    For example, 9765320 (9-765-32-0) would be 1 + 32 + 22 + 1 = 15 points.
    
+2 if the entire number is a multiple of 3

+4 for each even digit (note that 0 is even)

Each component of the score is evaluated separately, so a given digit may contribute to more than one component.

    For example, the number 765 would score 9 for the sequence of length 3, 4 for one even digit (6), 1 for the 7 digit, and 2 because 765 is a multiple of 3, for a total of 9 + 4 +1 + 2 = 16.

Write a function compute_number_score that computes (and returns) a score for an integer passed to it. The number will be in the range 0<=number<1000000000