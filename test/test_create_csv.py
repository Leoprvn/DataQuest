"""
This module is to create a csv file based on the parameters
"""
import os
import datetime
import pytest
import create_csv


@pytest.fixture(name='input_value')
def parameter():
    """
    Initialise the parameters to use by other function
    :return: list of parameter to the other functions
    """
    first_name = ('Andrew', 'John', 'Clifford', 'Jinna', 'Andy', 'Joe', 'Joesph', 'Thomas'
                  , 'Praveen', 'Edward')
    last_name = ('Johnson', 'Smith', 'Williams', 'Robinson', 'Walker', 'Allen', 'Hill', 'Scott'
                 , 'Adams', 'Carter')
    address = ('1745 T Street Southeast', '6007 Applegate Lane', '560 Penstock Drive'
               ,'150 Carter Street', '2721 Lindsay Avenue', '18 Densmore Drive', '1364 Capri Drive'
               , '159 Downey Drive', '109 Summit Street', '8502 Madrone Avenue')
    type_char = ('f','l','a','n')
    ran_csv_gen_file = os.path.join(os.path.abspath('.'), 'create_csv.csv')
    number_of_lines = 100
    return [first_name,last_name,address,type_char,ran_csv_gen_file,number_of_lines]


def test_random_first_last_name_dob(input_value):
    """
    Test the random name , address and date of birth generation
    :param input_value: as list from the fixture
    """
    first_name = input_value[0]
    last_name = input_value[1]
    address = input_value[2]
    type_char = input_value[3]
    result = [create_csv.random_first_last_name_dob(type_c) for type_c in type_char]
    print(result)
    assert len(result) == 4,'Number of column generated is not correct'
    assert result[0] in first_name ,f"Generated value doesn't present in the {first_name} set"
    assert result[1] in last_name, f"Generated value doesn't present in the {last_name} set"
    assert result[2] in address, f"Generated value doesn't present in the {address} set"
    assert isinstance(result[3],datetime.date), 'date is not generated as datetime format'


def test_create_csv_file(input_value):
    """
    To the test the create csv file function
    :param input_value: as list from the fixture
    """
    file_name = input_value[4]
    number_of_lines = input_value[5]
    create_csv.create_csv_file(file_name, number_of_lines)
    assert os.path.exists(file_name) , "File doesn't created, please check the function" \
                                       " create_csv_file"
    cnt = 0
    for count in open(file_name):
        assert len(count.split(',')) == 4, 'Number of column is less than expected'
        cnt += 1
    assert cnt-1 == number_of_lines, 'Number of lines generated is not equal to the ' \
                                     'numnber of lines passed as parameter'
