import login_system_exception_handling


class Profiles:

    def __init__(self, name, age, job, account, id_num):
        self.name = name
        self.age = age
        self.job = job
        if account == 'Y':
            self.account = "Premium"
        else:
            self.account = "Standard"
        self.id_num = id_num

    def update_account_type(self):
        # Change account status of existing, non-VIP accounts.
        if self.account == 'Premium':
            change = input('Downgrade from Standard to Standard account? (Y/N): ')
            if change == 'Y':
                self.account = 'Standard'
        elif self.account == 'Standard':
            change = input('Upgrade Standard account to Premium account? (Y/N): ')
            if change == 'Y':
                self.account = 'Premium'

    @staticmethod
    def create_new_account(account_id, profiles):
        """Initiate creation of new account, using user input. Creates instance of Profiles under temporary variable 'p'
        and then calls update_profile_directory function to list Profile instance permanently in profiles dictionary
        under key of string of account_id #. Prints new account_id # to user and returns updated profiles dictionary."""

        print('CREATING NEW ACCOUNT:')

        # FIXME: Add exception handling
        info_list = input('Enter your information in the form (First Name Last Name, Age, Job, Upgrade to Premium '
                          'Account (Y/N)): ').split(',')
        name = info_list[0].strip()
        age = int(info_list[1])
        job = info_list[2].strip()
        account = info_list[3].strip()
        p = Profiles(name, age, job, account, account_id)
        profiles = Profiles.update_profile_directory(account_id, p, profiles)
        print(f'Your Account # is {account_id}. Keep this number to log in to your account in the future.\n')
        return profiles

    @staticmethod
    def update_profile_directory(account_id, profile, profiles):
        # Function called whenever a profile is updated, to return profiles dictionary with updated profile.
        profiles[account_id] = profile
        return profiles

    @staticmethod
    def retrieve_profile(profiles):
        """Function takes user input account_id #, returns profile instance if one exists under account_id #, and prints
        an error message if no profile exists, returning user to menu."""
        account_id = input('Enter your Account #: ')
        try:
            profile = profiles[account_id]
            return profile
        except KeyError:
            return 'Account # not valid. No profile exists in system.'

    @staticmethod
    def delete_profile(account_id, profiles):
        del profiles[account_id]
        return profiles

    def __str__(self):
        # When non-VIP profile instance is printed, this string is returned.
        return f'\nThis is the pofile of user #{self.id_num}:\n\tName: {self.name}\n\tAge: {self.age}\n\tJob: ' \
               f'{self.job}\n\tAccount Type: {self.account}'


class SpecialProfiles(Profiles):

    def __init__(self, name, age, job, account, id_num, donor_amount):
        Profiles.__init__(self, name, age, job, account, id_num)
        self.account = account
        self.donor_amount = donor_amount

    @staticmethod
    def create_new_vip_account(account_id, profiles):
        print('ESTABLISHING NEW VIP MEMBER:')

        info_list = input('Enter your information in the form (First Name Last Name, Age, Job): ').split(',')
        name = info_list[0].strip()
        age = int(info_list[1])
        job = info_list[2].strip()

        print('\nVIP MEMBERSHIP LEVELS:\n\tBronze: $1 - $100\n\tSilver: $101 - $1,000\n\tGold: $1,000+\n')
        while True:
            account = ''
            donor_amount = int(input('Enter monthly donation amount: '))
            if 0 < donor_amount <= 100:
                account = 'Bronze'
                break
            elif 100 < donor_amount <= 1000:
                account = 'Silver'
                break
            elif donor_amount >= 1000:
                account = 'Gold'
                break
            else:
                'Invalid donation. Please try again.'
                continue

        # name, age, job, account, id_num, donor_amount
        p = SpecialProfiles(name, age, job, account, account_id, donor_amount)
        profiles = Profiles.update_profile_directory(account_id, p, profiles)
        print(
            f'You have established yourself as a {account} Level VIP member. Your Account # is {account_id}. Keep this '
            f'number to log in to your account in the future.\n')
        return profiles

    def __str__(self):
        return f'\nThis is the VIP profile of {self.name}:\n\tDonor Status: {self.account}\n\tDonor Amount: ' \
               f'${self.donor_amount}\n'


def main():
    profiles = {}
    num_profiles = 0
    deleted_free_spaces = []

    while True:
        print('MENU:\n\t1. Create new account\n\t2. Log in to account\n\t3. Update account type\n\t4. VIP Menu\n\t5. '
              'Delete account\n\t6. Quit program\n')
        option = login_system_exception_handling.StaticMethods.take_menu_selection(6)  # 6 is number of menu options
        if option == '1':
            if not bool(deleted_free_spaces):
                num_profiles += 1
                profiles = Profiles.create_new_account(str(num_profiles), profiles)
            else:
                next_free_space = deleted_free_spaces[0]
                deleted_free_spaces.pop(0)
                profiles = Profiles.create_new_account(next_free_space, profiles)
        elif option == '2':
            profile = Profiles.retrieve_profile(profiles)
            print(f'{profile}\n')
        elif option == '3':
            profile = Profiles.retrieve_profile(profiles)
            change = input(f'You currently have a {profile.account} account. Would you like to change between '
                           f'Standard/Premium account types (Y/N)? ').strip()
            if change == 'Y':
                if profile.account == 'Premium':
                    profile.account = 'Standard'
                elif profile.account == 'Standard':
                    profile.account = 'Premium'
                print(f'Account type successfully changed to {profile.account}.\n')
            else:
                print('Account type not changed.\n')
            profiles[profile.id_num] = profile
        elif option == '4':
            while True:
                print('VIP MENU:\n\t1. Create new VIP account\n\t2. Log in to VIP account\n\t3. Change donation '
                      'amount\n\t4. Become a VIP\n\t5. Return to main menu\n')
                vip_option = login_system_exception_handling.StaticMethods.take_menu_selection(5)
                if vip_option == '1':
                    if not bool(deleted_free_spaces):
                        num_profiles += 1
                        profiles = SpecialProfiles.create_new_vip_account(str(num_profiles), profiles)
                    else:
                        next_free_space = deleted_free_spaces[0]
                        deleted_free_spaces.pop(0)
                        profiles = SpecialProfiles.create_new_vip_account(next_free_space, profiles)
                elif vip_option == '2':
                    profile = Profiles.retrieve_profile(profiles)
                    print(f'{profile}\n')
                elif vip_option == '3':
                    profile = Profiles.retrieve_profile(profiles)
                    print(
                        f'You are currently a {profile.account} Level VIP, with a monthly contribution of $'
                        f'{profile.donor_amount}.')
                    change = input('\nWould you like to change your monthly donation (Y/N)? ').strip()
                    if change == 'Y':
                        while True:  # FIXME: Add exception handling
                            donor_amount = int(input('Enter new monthly donation amount: '))
                            profile.donor_amount = donor_amount
                            if 0 < donor_amount <= 100:
                                profile.account = 'Bronze'
                                break
                            elif 100 < donor_amount <= 1000:
                                profile.account = 'Silver'
                                break
                            elif donor_amount >= 1000:
                                profile.account = 'Gold'
                                break
                            else:
                                'Invalid donation. Please try again.'
                                continue
                        print(f'\nMonthly donation successfully changed to ${donor_amount}. You are now a '
                              f'{profile.account} Level VIP.\n')
                    else:
                        print()
                elif vip_option == '4':
                    profile = Profiles.retrieve_profile(profiles)
                    print()
                    profiles = SpecialProfiles.create_new_vip_account(profile.id_num, profiles)
                elif vip_option == '5':
                    break
        elif option == '5':
            profile = Profiles.retrieve_profile(profiles)
            print(f'{profile}\n')
            delete_confirm = False
            if input('Are you sure you want to delete your account (Y/N)? ').strip() == 'Y':
                delete_confirm = True
            else:
                print('Account deletion canceled. Returning to menu.\n')
            if delete_confirm:
                deleted_free_spaces.append(profile.id_num)
                profiles = Profiles.delete_profile(profile.id_num, profiles)
                print('Your account has been deleted.\n')
        elif option == '6':
            break


if __name__ == '__main__':
    main()
