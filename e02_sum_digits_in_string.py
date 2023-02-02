def main():
    number = input('Enter a single digit number: ')
    total = 0
    if number.isdigit():
        for num in number:
            ch = int(num)
            total += ch
        print(f'The total of the number {number} is {total}')
    else:
        print('That is not a number')



if __name__ == '__main__':
    main()
