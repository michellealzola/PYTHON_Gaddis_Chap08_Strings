def get_initial(name):
    return name[0].upper()


def main():
    initial_all = ''
    names = ('first', 'middle', 'last')
    for name in names:
        get_name = input(f'Enter {name}: ')
        initial = get_initial(get_name)
        initial_all += (initial + '. ')
    print(initial_all)


if __name__ == '__main__':
    main()
