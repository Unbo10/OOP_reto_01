def find_anagrams(ls: list) -> list:
    matching_words = []
    i: int = 0
    while i < len(ls):
        j: int = i + 1
        word = ls[i]
        while j < len(ls):
            if len(word) == len(ls[j]):
                chr_count = 0
                k: int = 0
                characters_in_word = list(word)
                characters_in_compared_word = list(ls[j])
                characters_in_word.sort()
                characters_in_compared_word.sort()
                while k < len(word):
                    if characters_in_word[k] == characters_in_compared_word[k]:
                        chr_count += 1
                    k += 1
                if chr_count == len(word):
                    print("", end = "") if word in matching_words else matching_words.append(word)
                    print("", end = "") if ls[j] in matching_words else matching_words.append(ls[j])
                    ls.pop(j)
                    j -= 1
            j += 1
        ls.pop(i)
        i += 1
    return matching_words

if __name__ == "__main__":
    word_list = []
    done: bool = False
    print("To stop entering words, enter a non-alphabetic character. This program will return the words that have matching characters in the list.")
    while done == False:
        word = input("Enter a word: ")
        if word.isalpha():
            word_list.append(word)
        else:
            done = True
    print("The words with matching characters in {} are:".format(word_list), find_anagrams(word_list))