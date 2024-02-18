# OOP_reto_01

1. Create a function that performs basic operations (addition, subtraction, multiplication, division) between two numbers, according to the user's choice. The function's input will be the two operands and the character used for the operation.

    To complete the task, the function ``operations`` was used. It has *three arguments* -the operation and the two numbers- and through a *match-case statement* it performs the desired operation on the two numbers, returning the result.

2. Perform a function that allows you to validate if a word is a palindrome. Condition: You are not allowed to use slicing to reverse the word and check if it's equal to the original.
    
    To check if a word is palindrome the function ``is_palindrome`` uses the ``len()`` function to set a numeric limit at the middle of it (``n``). It then compares two characters that are *i* characters away from their closest end (start or end of the word) until `i = n`. For every equal pair of characters, a counter variable ``count`` is increased by one, so it can be compared with n after the iterations to determine wheter the word is palindrome.

3. Write a function that receives a list of integers and returns only those that are prime.

    By using the [optimized prime number algorithm](https://en.wikipedia.org/wiki/Primality_test#Simple_methods), a function ``filter_primes`` takes a list of integers as an argument and: makes another one that filters any even numbers; goes through each element in it and uses the function ``is_prime`` to check the numbers' primality and adds to the return list the prime ones.

4. Write a function that receives a list of integers and returns the highest sum between two consecutive elements.

    The function ``find_greatest_consecutive_sum`` takes a list and iterates through it, comparing the greatest sum up to the *i-th* iteration (stored in ``gsum``) with the sum of the *i-th* element on the list and the next one, until ``i`` is equal to the list's length.

5. Write a function that receives a list of strings and returns only those elements that have the same characters.

    ``get_matching_words`` takes a list of strings and iterates through all of them, comparing in each iteration a word with all the others, checking first if their length (using ``len()``) is the same and if it is, it makes the strings lists and sorts them so they can then be compared character by character, regardless of the strings' order. It then appends the words to ``matching_words`` if they are the same (i.e., if ``chr_count`` is equal to the words' length) and removes them from the input list to make the program more efficient.
