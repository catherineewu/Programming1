
class CustomErrors:

    class InvalidMenuSelectionError(Exception):
        def __init__(self):
            pass


class TestFunctions:
    def __init__(self):
        pass

    @staticmethod
    def valid_menu_input_exception(option, num_options):
        valid_options = []
        for i in range(1, num_options + 1):
            valid_options.append(str(i))
        if option in valid_options:
            return option
        else:
            raise CustomErrors.InvalidMenuSelectionError


class StaticMethods:
    def __init__(self):
        pass

    @staticmethod
    def take_menu_selection(num_options):
        option = input('Enter menu selection: ')
        try:
            option = TestFunctions.valid_menu_input_exception(option, num_options)
            print()
            return option
        except CustomErrors.InvalidMenuSelectionError:
            print('Invalid menu selection. Returning to menu.\n')


def main():
    pass


if __name__ == "__main__":
    main()
