def pig_latin(word):
    char_set = []
    pig_latin_word = ''

    for char in word:
        char_set.append(char)

    char_beginning = char_set[0]
    char_set.remove(char_set[0])
    char_set.append(char_beginning)
    char_set.append('AY')

    for i in range(len(char_set)):
        pig_latin_word += char_set[i]

    return pig_latin_word


def main():
    sentence = input('Enter a sentence: ')
    sentence_upper = sentence.upper().split(' ')
    sentence_list = []
    for words in sentence_upper:
        sentence_list.append(words)

    print('The pig latin translation is')
    pig_latin_list = []
    for word_not_pig_latin in sentence_list:
        pig_latin_list.append(pig_latin(word_not_pig_latin))
    for piglatin in pig_latin_list:
        print(piglatin, end=' ')


if __name__ == '__main__':
    main()
