# PROJECT 2: Run-Length Encoding with Images


# CLASS METHODS 1-6
# 1 WORKS, Checked by ZB
def to_hex_string(data):
    # Translates data (RLE or raw) a hexadecimal string (without delimiters). This method can also aid debugging.
    # Ex: to_hex_string([3, 15, 6, 4]) yields string "3f64".
    hex_list = []
    for value in data:
        if 0 <= value <= 9:
            hex_list.append(str(value))
        else:
            hex_list.append(chr(value + 87))
    hex_string = ''.join(hex_list)
    return hex_string


# 2 WORKS, Checked by ZB
def count_runs(flat_data):
    # Returns number of runs of data in an image data set; double this result for length of encoded (RLE) list.
    # Ex: count_runs([15, 15, 15, 4, 4, 4, 4, 4, 4]) yields integer 2.
    # Needs to differentiate between raw data and RLE data list.

    # Finds indexes in raw data list where value changes from the previous.
    places_change = [0]
    for i in range(1, len(flat_data)):
        if flat_data[i] != flat_data[i-1]:
            places_change.append(i)

    # Finds interval between each value.
    intervals = []
    for i in range(len(places_change)):
        if i == len(places_change) - 1:
            intervals.append((len(flat_data)) - places_change[i])
        else:
            intervals.append(places_change[i + 1] - places_change[i])

    # Finds and modifies data for runs > 15.
    additions = 0  # How much to shift index for editing list.
    for i in range(len(intervals)):
        if intervals[i + additions] > 15:
            store = intervals[i + additions]
            while store > 15:
                store -= 15
                intervals[i + additions] = 15
                intervals.insert(i + 1 + additions, store)
                additions += 1

    runs = len(intervals)
    return runs


# 3 WORKS, Checked by ZB
def encode_rle(flat_data):
    # Returns encoding (in RLE) of raw data passed in; used to generate RLE representation of data.
    # Ex: encode_rle([15, 15, 15, 4, 4, 4, 4, 4, 4]) yields list [3, 15, 6, 4]
    rle_list = []

    # Finds indexes in raw data list where value changes from the previous.
    places_change = [0]
    for i in range(1, len(flat_data)):
        if flat_data[i] != flat_data[i-1]:
            places_change.append(i)
    # print(f'places_change: {places_change}')

    # Finds list of values.
    values = []
    for i in range(len(places_change)):
        values.append(flat_data[places_change[i]])
    # print(f'values: {values}')

    # Finds interval between each value.
    intervals = []
    for i in range(len(places_change)):
        if i == len(places_change) - 1:
            intervals.append((len(flat_data)) - places_change[i])
        else:
            intervals.append(places_change[i + 1] - places_change[i])
    # print(f'intervals: {intervals}')

    # Finds and modifies data for runs > 15.
    additions = 0  # How much to shift index for editing list.
    for i in range(len(intervals)):
        if intervals[i + additions] > 15:
            store = intervals[i + additions]
            while store > 15:
                store -= 15
                intervals[i + additions] = 15
                intervals.insert(i + 1 + additions, store)
                values.insert(i + 1 + additions, values[i + additions])
                additions += 1
    # print(f'\nnew intervals: {intervals}')
    # print(f'new values: {values}\n')

    # Combines lists: values[] and intervals[] for encoded RLE List
    for i in range(len(values)):
        rle_list.append(intervals[i])
        rle_list.append(values[i])

    return rle_list


# 4 WORKS, Checked by ZB
def get_decoded_length(rle_data):
    # Returns decompressed size RLE data; used to generate flat data from RLE encoding. (Counterpart to #2).
    # Ex: get_decoded_length([3, 15, 6, 4]) yields integer 9
    length = 0
    for num in range(0, len(rle_data), 2):
        length += rle_data[num]
    return length


# 5 WORKS, Checked by ZB
def decode_rle(rle_data):
    # Returns the decoded data set from RLE encoded data. This decompresses RLE data for use. (Inverse of #3).
    # Ex: decode_rle([3, 15, 6, 4]) yields list [15, 15, 15, 4, 4, 4, 4, 4, 4].
    decoded_rle = []
    for num in range(0, len(rle_data), 2):
        repetitions = rle_data[num]
        value = rle_data[num + 1]
        for repetition in range(repetitions):
            decoded_rle.append(value)
    return decoded_rle


# 6 WORKS, Checked by ZB
def string_to_data(data_string):
    # Translates a string in hexadecimal format into byte data (can be raw or RLE). (Inverse of #1).
    # Ex: string_to_data ("3f64") yields list [3, 15, 6, 4].
    hex_data = []
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for char in data_string:
        if char in numbers:
            hex_data.append(int(char))
        else:
            hex_data.append(ord(char.lower()) - 87)
    return hex_data


# 7 WORKS, Not Checked by ZB
def to_rle_string(rle_data):
    # Translates RLE data into a human-readable representation. For each run, in order, it should display the run length
    # in decimal (1-2 digits); the run value in hexadecimal (1 digit); and a delimiter, ‘:’, between runs.
    # Ex: to_rle_string([15, 15, 6, 4]) yields string "15f:64".
    readable_list = []
    for i in range(len(rle_data)):
        if i % 2 == 1:
            if 0 <= rle_data[i] <= 9:
                readable_list.append(str(rle_data[i]))
            else:
                readable_list.append(chr(rle_data[i] + 87))
            if i != len(rle_data) - 1:
                readable_list.append(':')
        else:
            readable_list.append(str(rle_data[i]))
    readable_string = ''.join(readable_list)
    return readable_string


# 8 WORKS, Not checked in ZB
def string_to_rle(rle_string):
    # Ex: string_to_rle("15f:64") yields list [15, 15, 6, 4]. (Inverse of #7).
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    rle_units_list = rle_string.split(':')
    rle_list = []
    for i in range(len(rle_units_list)):
        rle_units_list[i] = list(rle_units_list[i])
    for i in range(len(rle_units_list)):
        if len(rle_units_list[i]) == 3:
            rle_list.append(int(rle_units_list[i][0] + rle_units_list[i][1]))
            if rle_units_list[i][2] in numbers:
                rle_list.append(int(rle_units_list[i][2]))
            else:
                rle_list.append(ord(rle_units_list[i][2].lower()) - 87)
        else:  # len(rle_units_list) == 2
            rle_list.append(int(rle_units_list[i][0]))
            if rle_units_list[i][1] in numbers:
                rle_list.append(int(rle_units_list[i][1]))
            else:
                rle_list.append(ord(rle_units_list[i][1].lower()) - 87)
    return rle_list


def main():
    from console_gfx import ConsoleGfx

    print('Welcome to the RLE image encoder!\n')
    print('Displaying Spectrum Image: ')
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    print()

    menu = "\nRLE Menu\n--------\n0. Exit\n1. Load File\n2. Load Test Image\n3. Read RLE String\n4. Read RLE Hex " \
           "String\n5. Read Data Hex String\n6. Display Image\n7. Display RLE String\n8. Display Hex RLE Data\n9. " \
           "Display Hex Flat Data\n"

    image_data = None
    ''' 
    DATA ASSIGNED NAME AND TYPE:
    
    image_data = Raw Byte Data (ex: [15, 15, 15, 4, 4, 4, 4, 4, 4])
    rle_data = RLE Encoded Data List (ex: [3, 15, 6, 4])
    hex_string_data = Hexadecimal String Representation of Byte Data (Raw OR RLE Encoded) (ex: "3f64")
    
    '''

    while True:
        print(menu)
        option = int(input('Select a Menu Option: '))

        # 0. EXIT PROGRAM
        # Status: Works, Checked
        if option == 0:
            break

        # 1. LOAD FILE
        # Status: Works, Checked
        elif option == 1:
            filename = input('Enter name of file to load: ')
            image_data = ConsoleGfx.load_file(filename)  # Loads data as full length numerical list

        # 2. LOAD TEST IMAGE
        # Status: Works, Checked
        elif option == 2:
            print('Test image data loaded.')
            image_data = ConsoleGfx.test_image  # Loads data as full length numerical list

        # 3. READ RLE STRING (input ex: 28:10:6B:10:10B:10:2B:10:12B:10:2B:10:5B:20:11B:10:6B:10)
        # Status: Works, Not Checked
        elif option == 3:
            rle_decimal_string = input('Enter an RLE string to be decoded: ')
            rle_data_list = string_to_rle(rle_decimal_string)
            image_data = decode_rle(rle_data_list)

        # 4. READ RLE HEX STRING (input ex: 28106B10AB102B10CB102B105B20BB106B10)
        # Status: Works, Not Checked
        elif option == 4:
            rle_hex_string = input('Enter the hex string holding RLE data: ')
            rle_data_list = string_to_data(rle_hex_string)
            image_data = decode_rle(rle_data_list)

        # 5. READ DATA HEX STRING (input ex: 880bbbbbb0bbbbbbbbbb0bb0bbbbbbbbbbbb0bb0bbbbb00bbbbbbbbbbb0bbbbbb0)
        # Status: Works, Not Checked
        elif option == 5:
            flat_hex_string = input('Enter the hex string holding flat data: ')
            image_data = string_to_data(flat_hex_string)

        # 6. DISPLAY IMAGE: Works with FLAT NUMERICAL DATA (uncompressed byte data list).
        # Status: Works, Checked
        elif option == 6:
            print('Displaying image...')
            ConsoleGfx.display_image(image_data)

        # 7. DISPLAY RLE STRING (output ex: 28:10:6b:10:10b:10:2b:10:12b:10:2b:10:5b:20:11b:10:6b:10)
        # Status: Works
        elif option == 7:
            rle_data = encode_rle(image_data)
            rle_string = to_rle_string(rle_data)
            print(f'RLE representation: {rle_string}')

        # 8. DISPLAY HEX RLE DATA (output ex: 28106b10ab102b10cb102b105b20bb106b10)
        # Status: Works
        elif option == 8:
            rle_data = encode_rle(image_data)
            hex_rle_string = to_hex_string(rle_data)
            print(f'RLE hex values: {hex_rle_string}')

        # 9. DISPLAY HEX FLAT DATA (output ex:  880bbbbbb0bbbbbbbbbb0bb0bbbbbbbbbbbb0bb0bbbbb00bbbbbbbbbbb0bbbbbb0)
        # Status: Works
        elif option == 9:
            flat_hex_string = to_hex_string(image_data)
            print(f'Flat hex values: {flat_hex_string}')

        else:
            print("Invalid menu selection. Please enter another selection or enter 0 to exit the program.")


if __name__ == '__main__':
    main()