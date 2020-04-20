"""A program that counts how many times a word occurs in a string."""
"""https://github.com/jasongan234/CP1401p/blob/master/word_occurences.py"""
def main():
    words_to_count = {}
    sentence = input("Enter a sentence: ")
    word = sentence.split()

    for sentence in word:
        if sentence in words_to_count:
            words_to_count[sentence] += 1
        else:
            words_to_count[sentence] = 1

    word = list(words_to_count.keys())
    word.sort()

    max_lenght = max((len(sentence) for sentence in word))
    for sentence in word:
        print("{:{}} = {}".format(sentence, max_lenght, words_to_count[sentence]))

if __name__== '__main__':
    main()
