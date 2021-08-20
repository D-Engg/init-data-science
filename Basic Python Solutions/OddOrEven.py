def odd_or_even():
    while True:
        number = int(input('Enter a number more than 2: '))
        if number in (0,1,2):
            print('Please see the fucking statement first then enter')
        elif number%2 == 0:
            print('It is an even number')
            break
        else:
            print('It is an odd number')
            break


def main():
    odd_or_even()

main()
