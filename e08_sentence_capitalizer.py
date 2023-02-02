def sentence_capitalize(sentences):
    sentence_updated_list = []
    sentence_updated = sentences.split(". ")

    for sentence in sentence_updated:
        upper = sentence[0].upper()
        all_sentence = ""
        for i in range(1, len(sentence)):
            all_sentence += sentence[i]
            if all_sentence[-1].isalnum():
                period = '.'
            else:
                period = ''
        sentence_updated_list.append(upper + all_sentence + period)

        sentence_capitalize_result = ''
        for phrase in sentence_updated_list:
            sentence_capitalize_result += (phrase + " ")

    return sentence_capitalize_result


def main():
    sentences = input('Enter sentences: ')
    print(sentence_capitalize(sentences))


if __name__ == '__main__':
    main()
