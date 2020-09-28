import csv
import random
import datetime
import sys


def arg_validate():
    """
    Validate the anumber of argument
    :return: if validateion fails, comes out of the script
    """
    if len(sys.argv) < 2:
        print("Please pass valid arguments")
        print("Execute: python create_csv.py  <file_input> <number_of_lines>")
        print("Example: python create_csv.py '/tmp/csv_file.csv' 10")
        sys.exit(1)


def random_first_last_name_dob(type_char):
    """
    Generate the random first name or last name or address or date of birth
    :param type_char: 'f' - first_name ,'l' - last_name,'a' - address ,'n' - date_of_birth
    :return: Random First name/Last name/ Address / Data of Birth based on the parameter
           : "Praveen' / 'Hill' / '8502 Madrone Avenue' / '22/11/1992'
    :example: random_first_last_name_dob(<type_char>
            : random_first_last_name_dob('f')
    """
    first_name = ('Andrew', 'John', 'Clifford', 'Jinna', 'Andy', 'Joe', 'Joesph', 'Thomas', 'Praveen', 'Edward')
    last_name = ('Johnson', 'Smith', 'Williams', 'Robinson', 'Walker', 'Allen', 'Hill', 'Scott', 'Adams', 'Carter')
    address = ('1745 T Street Southeast', '6007 Applegate Lane', '560 Penstock Drive', '150 Carter Street',
               '2721 Lindsay Avenue', '18 Densmore Drive', '1364 Capri Drive', '159 Downey Drive', '109 Summit Street',
               '8502 Madrone Avenue')
    year = ('1990','1992','1993','1994')
    try:
        if type_char == "f":
            choice_anc = random.choice(first_name)
        elif type_char == "l":
            choice_anc = random.choice(last_name)
        elif type_char == "a":
            choice_anc = random.choice(address)
        elif type_char == "n":
            date_str = str(random.randint(1,28))+"/"+str(random.randint(1,12))+"/"+str(random.choice(year))
            choice_anc = datetime.datetime.strptime(date_str, '%d/%m/%Y').date()
        else:
            print("Invalid type of characters choice")
        return choice_anc
    except:
        print("I/O Error")
        sys.exit(1)


def create_csv_file(file_name, number_of_lines):
    """
    create the csv file with the random first_name,last_name,address,date_of_birth
    :param file_name: provide the file_name which needs to be created
    :param number_of_lines: number of lines needs ot be generator
    :return: create a csv file
    :example: create_csv_file('random_csv_file.csv',10)
    """
    column_name = ['first_name','last_name','address','date_of_birth']
    try:
        with open(file_name, "w+",newline="") as csv_file:
            file_writer = csv.DictWriter(csv_file,fieldnames=column_name,delimiter=',')
            file_writer.writeheader()
            for i in range(number_of_lines):
                file_writer.writerow({column_name[0]:random_first_last_name_dob('f'),column_name[1]: \
                    random_first_last_name_dob('l'),column_name[2]:random_first_last_name_dob('a'),\
                                      column_name[3]:random_first_last_name_dob('n')})
        print("File {} has been created Successfully with {} lines ".format(file_name,number_of_lines))
    except:
        print("Error in Creating File {}".format(file_name))
        sys.exit(1)


def main():
    arg_validate()
    csv_file_input = str(sys.argv[1])
    number_of_lines = int(sys.argv[2])
    try:
        create_csv_file(csv_file_input,number_of_lines)
    except:
        print("main function failed")


if __name__ == "__main__":
    main()

