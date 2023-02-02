import e10_most_frequent_character


def get_total_price(price_set):
    total = 0
    for price in price_set:
        total += float(price)
    return total


def get_average_price(price_set):
    total = 0
    for price in price_set:
        total += float(price)
    return total / (len(price_set))


def arrange_data(arrange_set):
    for data in arrange_set:
        print(data)


def main():
    infile = open('GasPrices.txt', 'r')
    gas_prices_list = infile.readlines()
    infile.close()
    for i in range(len(gas_prices_list)):
        gas_prices_list[i] = gas_prices_list[i].rstrip('\n')

    new_data = []
    for data in gas_prices_list:
        new_data.append(data.replace(':', '-'))

    usable_data = []
    for d in new_data:
        usable_data.append(d.split('-'))

    price_yearly_set = []
    print("TOTAL PRICE PER YEAR")
    for y in range(1993, 2014):
        price_set_y = []
        for ud in usable_data:
            if ud[2] == str(y):
                price_set_y.append(ud[3])
        print(f'{y}: ${get_total_price(price_set_y):,.2f}')
        price_yearly_set.append(get_total_price(price_set_y))

    print("AVERAGE PRICE PER MONTH PER YEAR")
    for y in range(1993, 2014):
        for m in range(1, 13):
            price_set_m = []
            for ud in usable_data:
                if int(ud[1]) == m:
                    price_set_m.append(ud[3])
            print(f'{y}: month {m}: ${get_average_price(price_set_m):,.2f}')

    print("LIST OF PRICES LOWEST TO HIGHEST")
    ud_arrange_from_lowest = []
    for ud in usable_data:
        ud_data = ud[3] + ':' + ud[0] + '/' + ud[1] + '/' + ud[2]
        ud_arrange_from_lowest.append(ud_data)
    ud_arrange_from_lowest.sort()
    arrange_data(ud_arrange_from_lowest)

    print("LIST OF PRICES HIGHEST TO LOWEST")
    ud_arrange_from_highest = []
    for ud in usable_data:
        ud_data = ud[3] + ':' + ud[0] + '/' + ud[1] + '/' + ud[2]
        ud_arrange_from_highest.append(ud_data)
    ud_arrange_from_highest.sort(reverse=True)
    arrange_data(ud_arrange_from_highest)

    outfile1 = open('GasPriceFromLowest.txt', 'w')
    for entry in ud_arrange_from_lowest:
        outfile1.write(entry + '\n')
    outfile1.close()

    outfile2 = open('GasPriceFromHighest.txt', 'w')
    for entry in ud_arrange_from_highest:
        outfile2.write(entry + '\n')
    outfile2.close()


if __name__ == '__main__':
    main()
