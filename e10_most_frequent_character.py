import matplotlib.pyplot as plt


def bar_graph(string_input, count_set, char_set):
    plt.bar(char_set, count_set)
    plt.title(f'Most Frequent Characters in the Word "{string_input}"')
    plt.ylabel('Number of Times the Character Appeared')
    plt.xlabel('Characters')
    plt.yticks(count_set, count_set)
    return plt.show()


def count_char(char, string_input):
    count = 0
    for letter in string_input:
        if char == letter:
            count += 1
    return count


def main():
    string_input = input('Enter a string: ')

    char_set = []
    for i in range(len(string_input)):
        for j in range(i):
            if string_input[i] == string_input[j]:
                if string_input[i] not in char_set:
                    char_set.append(string_input[i])

    print(f'The list of characters that occurred most frequently in the word {string_input}:')

    count_set = []
    for char in char_set:
        count = count_char(char, string_input)
        count_set.append(count)
        print(f'The letter "{char}" appeared {count} times')

    bar_graph(string_input, count_set, char_set)


if __name__ == '__main__':
    main()
