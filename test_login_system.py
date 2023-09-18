import unittest
import login_system
import login_system_exception_handling
import tester


class TestLoginSystem(unittest.TestCase):
    def test_valid_menu_input_exception(self):
        with self.assertRaises(login_system_exception_handling.CustomErrors.InvalidMenuSelectionError):
            login_system_exception_handling.TestFunctions.valid_menu_input_exception('0', 5)
        with self.assertRaises(login_system_exception_handling.CustomErrors.InvalidMenuSelectionError):
            login_system_exception_handling.TestFunctions.valid_menu_input_exception('one', 1)
        result = login_system_exception_handling.TestFunctions.valid_menu_input_exception('5', 5)
        expected = '5'
        self.assertEqual(result, expected, 'Wrong menu option returned. Should return string of number input.')

    def test_create_new_account(self):
        pass  # FIXME

    def test_practice1(self):  # Practice testcase with tester.py file
        instance1 = tester.Tester(1, 2)
        self.assertEqual(6, instance1.put_together(3))

        # Two equivalent test cases:
        self.assertRaises(TypeError, instance1.put_together, '3')
        with self.assertRaises(TypeError):
            instance1.put_together('3')


def main():
    pass


if __name__ == '__main__':
    unittest.main()
