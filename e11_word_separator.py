def main():
    print('This program accepts a sentence where the words are run together,')
    print('but the first character of each word is uppercase.')
    sentence_input = input('Enter a sentence: ')

    print(sentence_input[0], end='')
    for index in range(1, len(sentence_input)):
        if sentence_input[index].isupper():
            char = sentence_input[index].lower()
            print('', char, end='')
        else:
            print(sentence_input[index], end='')


if __name__ == '__main__':
    main()
