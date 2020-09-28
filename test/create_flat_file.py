import random
import string
import sys


def arg_validate():
    if len(sys.argv) < 3:
        print("Please pass valid arguments")
        print("Execution: python create_flat_file.py  <flat_file_input>  <number_of_lines_to_be_generated> \
        <columnoffset>")
        print("Example: create_flat_file.py '/opt/io_folder/flat_file.txt' 10 '5,12,3,2,13,7,10,13,20,13'")
        sys.exit(1)


def get_random_alphanumeric_character(length):
    """
    Return the random alphanumberic value based on the characeter length given to the parameter
    Parameter: length of character
    Example: get_random_alphanumeric_character(10)
    Returns: 'Pjt5BiY43G' #random value
    """
    try:
        alphanumeric_character = string.ascii_letters + string.digits
        result_str = ''.join((random.choice(alphanumeric_character) for i in range(int(length))))
        return result_str
    except:
        print("I/O Error")
        sys.exit(1)


def create_flat_file(file_name, number_of_lines, tot_num_char):
    """
    Create the flat file with random alphanumberic characters based on the number of character
    Parameters: file_name with complete path, number of lines, total number of characters to be generator
    Example: create_flat_file(r"/tmp/input_file.txt",10,98)
    Returns: create a file with random alphnumberic values with the mentioned characters per mentioned number of lines
    """
    try:
        with open(file_name, "w+") as f:
            for i in range(number_of_lines):
                val = get_random_alphanumeric_character(tot_num_char)
                f.write(val + "\n")
        print("File {} has been created Successfully with {} lines & {} characters per line"\
              .format(file_name,number_of_lines,tot_num_char))
    except:
        print("Error in Creating File {}".format(file_name))
        sys.exit(1)


def main():
    arg_validate()
    flat_file_input = str(sys.argv[1])
    number_of_records = int(sys.argv[2])
    offset = [int(i) for i in str(sys.argv[3]).split(',')]
    tot_num_char = sum(offset)
    try:
        create_flat_file(flat_file_input, number_of_records, tot_num_char)
    except:
        print('Exiting the main script')


if __name__ == "__main__":
    main()

