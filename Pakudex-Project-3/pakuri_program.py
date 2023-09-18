from pakudex import Pakudex


def get_capacity():
	while True:
		capacity = input('Enter max capacity of the Pakudex: ')
		try:
			capacity = int(capacity)
			if capacity <= 0:
				raise ValueError
			break
		except ValueError:
			print('Please enter a valid size.')
	return capacity


def print_menu():
	print('Pakudex Main Menu\n-----------------\n1.\tList Pakuri\n2.\tShow Pakuri\n3.\tAdd Pakuri\n4.'
		'\tEvolve Pakuri\n5.\tSort Pakuri\n6.\tExit\n')


def main():
	print('Welcome to Pakudex: Tracker Extraordinaire!')
	capacity = get_capacity()
	print(f'The Pakudex can hold {capacity} species of Pakuri.\n')
	pakudex = Pakudex(capacity)
	while True:
		print_menu()
		option = input('What would you like to do? ')

		# List Pakuri
		if option == '1':
			species_array = pakudex.get_species_array()
			if species_array is None:
				print('No Pakuri in Pakudex yet!\n')
			else:
				print('Pakuri In Pakudex:')
				for i in range(1, len(species_array) + 1):
					print(f'{i}. {species_array[i - 1]}')
				print()

		# Show Pakuri
		elif option == '2':
			species = input('Enter the name of the species to display: ')
			stats = pakudex.get_stats(species)
			if stats is None:
				print('Error: No such Pakuri!\n')
			else:
				print(f'Species: {species}\nAttack: {stats[0]}\nDefense: {stats[1]}\nSpeed: {stats[2]}\n')

		# Add Pakuri
		elif option == '3':
			if pakudex.get_size() == capacity:
				print('Error: Pakudex is full!\n')
			else:
				species = input('Enter the name of the species to add: ')
				success = pakudex.add_pakuri(species)
				if not success:
					print('Error: Pakudex already contains this species!\n')
				else:
					print(f'Pakuri species {species} successfully added!\n')

		# Evolve Pakuri
		elif option == '4':
			species = input('Enter the name of the species to evolve: ')
			success = pakudex.evolve_species(species)
			if not success:
				print('Error: No such Pakuri!\n')
			else:
				print(f'{species} has evolved!\n')

		# Sort Pakuri
		elif option == '5':
			pakudex.sort_pakuri()
			print('Pakuri have been sorted!\n')

		# Exit
		elif option == '6':
			print('Thanks for using Pakudex! Bye!')
			break

		# Invalid Menu Input
		else:
			print('Unrecognized menu selection!\n')


if __name__ == '__main__':
	main()

