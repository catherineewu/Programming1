import sys
from heifer_generator import HeiferGenerator


def find_cows(name, cows):
    for cow in cows:
        if cow.get_name() == name:
            return cow
    return None


def print_dragon_message(name):  # input parameter: cow.get_name()
    if 'ice-dragon' == name:
        print('This dragon cannot breathe fire.')
    elif 'dragon' == name:
        print('This dragon can breathe fire.')


def main():
    cows = HeiferGenerator.get_cows()

    if sys.argv[1] == '-l':  # python3 cowsay.py -l Lists the available cows
        print('Cows available:', end='')
        for i in range(len(cows)):
            name = cows[i].get_name()
            print(f' {name}', end='')
    elif sys.argv[1] == '-n':  # python3 cowsay.py -n COW MESSAGE Prints out the MESSAGE using the specified COW
        cow = find_cows(sys.argv[2], cows)
        if cow is None:
            print(f'Could not find {sys.argv[2]} cow!')
        else:
            for i in range(3, len(sys.argv)):
                if i == len(sys.argv) - 1:
                    print(sys.argv[i])
                else:
                    print(sys.argv[i], end=' ')
            print(cow.get_image())
            print_dragon_message(cow.get_name())
    else:
        cow = find_cows('heifer', cows)
        for i in range(1, len(sys.argv)):
            if i == len(sys.argv) - 1:
                print(sys.argv[i])
            else:
                print(sys.argv[i], end=' ')
        print(cow.get_image())
        print_dragon_message(cow.get_name())


if __name__ == '__main__':
    main()
